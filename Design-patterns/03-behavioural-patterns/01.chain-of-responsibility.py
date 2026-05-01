from __future__ import annotations
from abc import ABC, abstractmethod

class HeaderChain(ABC):
    def __init__(self, next_header: HeaderChain):
        self.next_header = next_header
    
    @abstractmethod
    def add_header(self, input_header: str):
        pass

    def do_next(self, input_header: str):
        if self.next_header:
            return self.next_header.add_header(input_header)
        return input_header


class AuthenticationHeader(HeaderChain):
    def __init__(self, token: str, next_header: HeaderChain = None):
        super().__init__(next_header)
        self.token = token
    
    def add_header(self, input_header: str):
        h = f"{input_header}\nAuthorization: {self.token}"
        return self.do_next(h)

class ContentTypeHeader(HeaderChain):
    def __init__(self, content_type: str, next_header: HeaderChain = None):
        super().__init__(next_header)
        self.content_type = content_type
    
    def add_header(self, input_header):
        h = f"{input_header}\nContent-Type: {self.content_type}"
        return self.do_next(h)

class AddBody(HeaderChain):
    def __init__(self, body: str, next_header: HeaderChain = None):
        super().__init__(next_header)
        self.body = body

    def add_header(self, input_header: str):
        h = f"{input_header}\nBody: {self.body}"
        return self.do_next(h)

if __name__ == "__main__":
    authentication_header = AuthenticationHeader("1234")
    content_type_header = ContentTypeHeader("application/json")
    body = AddBody("{\"username\": \"aniket\"}")

    # Chaining

    authentication_header.next_header = content_type_header
    content_type_header.next_header = body 

    headers_with_authentication = authentication_header.add_header("")
    headers_without_authentication = content_type_header.add_header("")

    print(headers_with_authentication)
    print()
    print(headers_without_authentication)

