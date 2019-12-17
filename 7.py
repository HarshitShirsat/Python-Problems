id=int(input("ENter id- "))
allow=int(input("ENter allowance- "))
basic=int(input("ENter basic pay- "))
gross=allow+basic
if gross>20000:
    it=0.30*gross
elif gross>10000:
    it=0.20*gross
elif gross>5000:
    it=0.10*gross
else:
    it=0
net=gross-it
print("ID - ",id)
print("Basic Pay - ",basic)
print("Allowance - ",allow)
print("Income Tax - ",it)
print("Net Pay - ",net)
