day=0
for i in range(2010,2021):
    if i%4==0 and i%100!=0 or i%400==0 :
        day+=366
    else:
        day+=365
print("No of days = ",day)
