size = input("enter the size S, M and L : ")
add_pepper = input("do you required extra pepper Y or N : ")
add_cheese = input("do you want extra cheese Y or N : ")
if size == "S":
    bill=15
elif size == "M":
    bill=20
else:
    bill=25
if add_pepper == "Y":
    if size == "S":
        bill+=2
    else:
        bill+=3
if add_cheese == "Y":
    bill+=1
print(f"Your finel bill is: ${bill}")