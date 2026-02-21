class A:
    def __init__(self):
        print("A")
        
class B(A):
    def __init__(self):
        print("B")
        super().__init__()

class C(A):
    def __init__(self):
        print("C")
        super().__init__()

class D:
    def __init__(self):
        print("D")
        super().__init__()


class G(B):
    def __init__(self):
        print("G")
        super().__init__()
    

class E(B,C):
    def __init__(self):
        print("E")
        super().__init__()

class F(B,D):
    def __init__(self):
        print("F")
        super().__init__()
        

class H(B,G): 
    def __init__(self):
        print("H")
        super().__init__()

e = E()
print("****")
f = F()
print("****")
h=H() #Error, B is an ancestor of G