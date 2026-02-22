from enum import Enum

class UserTier(Enum):
    FREE = "free"
    PREMIUM = "premium"
    
class User:
    def __init__(self, userid, tier: str):
        self.userid = userid
        self.tier = tier