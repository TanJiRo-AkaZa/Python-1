class A:
    def __init__(self,a):
        self.a = a
    def __lt__(self,other):
        if (self.a < other.a):
            return "ob 1 is less than obj 2"   
        else:
            return "ob 1 is not less than obj 2"
    def __eq__(self,other):
        if (self.a == other.a):
            return "obj 1 is equal to obj 2"   
        else:
            return "obj 1 is not equal to obj 2"
ob1 = A(5)
ob2 = A(10)
print(ob1 < ob2)
ob3 = A(3)
ob4 = A(3)
print(ob3 == ob4)
