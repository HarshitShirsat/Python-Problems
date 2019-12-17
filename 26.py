class A:
    def __init__(self, a):
        self.a = a

    def __add__(self, o):
        return self.a + o.a
    def  __sub__(self,o):
        return self.a-o.a
    def __mul__(self,o):
        return self.a*o.a
    def __lt__(self,o):
        if(self.a<o.a):
            return "ob1 is less than ob2"
        else:
            return "ob2 is less than ob1"
    def __gt__(self,o):
        if(self.a>o.a):
            return "ob1 is greater than ob2"
        else:
            return "ob2 is greater than ob1"
a=A(10)
b=A(20)
print(a>b)
print(a<b)
print(a+b)
print(a-b)
print(a*b)
