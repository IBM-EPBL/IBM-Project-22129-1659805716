import random
list=[]
n=int(input("Enter the Inputs: "))
for i in range(0,n):
   a=int(input())
   list.append(a)
print(list)
temp=random.choice(list)
hum=random.choice(list)
print(temp,hum)
if temp>100:
    if hum>80:
       print("Hazar Predected")
    else:
           print("High Temperature")
elif temp==100:
    print("Attention needed !! no threat")
else:
    print("All good")