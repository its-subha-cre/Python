import random
r=random.randint(1,100)
for i in range(1,11):
    
    number=int(input("enter the number"))
    if(r>number):
        print("lower number please")
    elif(r<number):
        print("higher number please")
    elif(r==number):
        print("your guess is correct")
    else:
        print("well done")