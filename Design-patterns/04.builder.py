class Network:
    def __init__(self, url="", auth ="", cache=0):
        self.__components = dict()
        if url:
            self.__components["URL"] = url
        if auth:
            self.__components["Authorization"] = auth
        if cache:
            self.__components["Cache-Control"] =  cache
    def show(self):
        return self.__components

v1 = Network(url="google.com")
v2 = Network(url="youtube.com", auth= "Bearer sahjcascv", cache=3600)
print(v1.show())
print(v2.show())