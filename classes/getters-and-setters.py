class Student:
    __age = None #internal variable
    
    @property
    def age(self):
        # getter
        if self.__age==None:
            raise "Age not set"
        return self.__age
    
    @age.setter
    def age(self, value):
        # setter
        if value<18:
            raise "cannot set the age. The student is underaged"
        self.__age = value

s1 = Student()
s1.age = 20
print(s1.age)
        
    
    