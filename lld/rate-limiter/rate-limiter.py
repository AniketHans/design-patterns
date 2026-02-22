from abc import ABC, abstractmethod
from user import UserTier, User
import time
import threading


Rate_Limiter_Config = {
    UserTier.FREE : {
        "token_bucket": {"capacity": 10, "refil_rate": 1, "max_tokens": 20},
        "sliding_window": {"capacity": 10, "window": 1}
    },
    UserTier.PREMIUM:{
        "token_bucket": {"capacity": 50, "refil_rate": 10, "max_tokens": 100},
        "sliding_window": {"capacity": 100, "window": 60} 
    }
    
}


class RateLimiterStrategy(ABC):
    @abstractmethod
    def allowRequest(self, user_id)->bool:
        pass


class TokenBucketRateLimiter(RateLimiterStrategy):
    def __init__(self, capacity, refil_rate, max_tokens):
        self.tokens = capacity
        self.last_refil = time.time()
        self.capacity = capacity
        self.refil_rate = refil_rate
        self.lock =  threading.Lock()
        self.max_tokens = max_tokens
    
    def allowRequest(self):
        with self.lock:
            now = time.time()
            elapsed_time = now - self.last_refil
            refil = int(elapsed_time) * self.refil_rate
            
            if refil>0:
                self.tokens = min(self.max_tokens, self.tokens+refil)
                self.last_refil = now
            
            if self.tokens>=1:
                self.tokens-=1
                return True
            return False

class SlidingWindowRateLimiter(RateLimiterStrategy):
    def __init__(self, capacity, window):
        self.capacity = capacity
        self.window = window
        self.request_queue_timestamp = []
        self.total_requests = 0
        self.lock = threading.Lock()
    
    def allowRequest(self):
        with self.lock:
            now = time.time()
            checktill =  now - self.window
            i = self.total_requests-1
            total_request_in_window = 0
            while i>-1 and self.request_queue_timestamp[i]>checktill:
                total_request_in_window +=1
                i-=1
            if total_request_in_window+1 < self.capacity:
                self.request_queue_timestamp.append(now)
                self.total_requests+=1
                return True
            return False
    
    
class RateLimiterFactory:
    @staticmethod
    def create( userTier: UserTier, strategy: str) -> RateLimiterStrategy:
        if strategy == "token_bucket":
            rate_limiter_configs = Rate_Limiter_Config[userTier][strategy]
            return TokenBucketRateLimiter(rate_limiter_configs["capacity"], rate_limiter_configs["refil_rate"], rate_limiter_configs["max_tokens"])
        elif strategy == "sliding_window":
            rate_limiter_configs = Rate_Limiter_Config[userTier][strategy]
            return SlidingWindowRateLimiter(rate_limiter_configs["capacity"], rate_limiter_configs["window"])
        else:
            raise f"{strategy} not available for the user tier"
        

class RateLimiter:
    def __init__(self, strategy:str):
        self.strategy = strategy
        self.limiter = {}
    
    def allow(self, user: User) -> bool:
        user_id = user.userid
        tier = user.tier
        key = (user_id, tier)
        if self.limiter.get(key) == None:
            rate_limiter = RateLimiterFactory.create(tier, self.strategy)
            self.limiter[key] = rate_limiter
        return self.limiter[key].allowRequest()


if __name__ == "__main__":
    u1 = User("1",UserTier.FREE)
    u2 = User("2", UserTier.PREMIUM)
    TokenBucketRTLM = RateLimiter("token_bucket")
    SlidingWindowRTLM = RateLimiter("sliding_window")
    # for x in range(15):
    #     for user in [u1,u2]:
    #         status = TokenBucketRTLM.allow(user)
    #         print(f"{user.userid}'s request {x+1} is {'allowed' if status else 'Disallowed'} TokenBucket")
            # if user.tier== UserTier.PREMIUM:
            #     status = SlidingWindowRTLM.allow(user)
            #     print(f"{user.userid}'s request {x+1} is {'allowed' if status else 'Disallowed'} SlidingWindow")
    
    for x in range(15):
        status = TokenBucketRTLM.allow(u1)
        print(f"{u1.userid}'s request {x+1} is {'allowed' if status else 'Disallowed'} TokenBucket")
    
    for x in range(120):
        status = TokenBucketRTLM.allow(u2)
        print(f"{u1.userid}'s request {x+1} is {'allowed' if status else 'Disallowed'} TokenBucket")
        
                
            
        
        