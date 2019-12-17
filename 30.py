class country():
    def __init__(self,cn,cc,cp):
        self.cn=cn
        self.cc=cc
        self.cp=cp
    def getcn(self):
        return self.cn
    def displayc(self):
        print("Country Name - ",self.cn,"\nCountry Capital - ",self.cc,"\nCountry Population - ",self.cp)
    def getcp(self):
        return self.cp

clist=[]
while(True):
    print("\nChoose an option below")
    print("1)Add country details\n2)Display country details\n3)Max population\n4)Exit")
    op=int(input("Enter your option - "))
    if op==1:
        cn=input("\nCountry name - ")
        cc=input("Country capital - ")
        cp=int(input("Country population - "))
        obj=country(cn,cc,cp)
        clist.append(obj)
    elif op==2:
        cn=input("\nCountry name - ")
        found=0
        for i in clist:
            if i.getcn()==cn :
                i.displayc()
                found=1
        if found==0 :
            print("\nCountry name not found!!")
    elif op==3:
        popl=[]
        for i in clist:
            popl.append(i.getcp())
        x=popl.index(max(popl))
        print("\nCountry with max population - ",clist[x].getcn())
        break
    elif op==4:
        Exit
        break
    else:
        print("\nEnter a valid choice!!")
