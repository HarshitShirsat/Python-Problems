class Account():
    def __init__(self):
        self.__accid=0
        self.__bal=100
        self.__airate=0
    def withdraw(self,amt):
        if (self.__bal-amt)<100:
            print("Low balance")
        else:
            self.__bal-=amt
    def deposit(self,amt):
        self.__bal+=amt
    def getAccid(self):
        return self.__accid
    def getBal(self):
        return self.__bal
    def getAir(self):
        return self.__airate
    def setAccid(self,a):
        self.__accid=a
    def setBal(self,b):
        self.__bal=b
    def setAir(self,air):
        self.__airate=air
    def getMir(self):
        return (self.__airate/12)
    def getMi(self):
        return self.__bal*self.getMir()

obj=Account()
obj.setAccid(1122)
obj.setBal(20000)
obj.setAir(0.045)
obj.withdraw(2500)
obj.deposit(3000)
print("id - ",obj.getAccid())
print("bal - ",obj.getBal())
print("Mir - ",obj.getMir())
print("Mi - ",obj.getMi())
