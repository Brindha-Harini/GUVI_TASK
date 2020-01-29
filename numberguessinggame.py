import random
a= random.randint(1, 999)
b = int(input("Enter a number from 1 to 999: "))
while a!= "b":
    print("")
    if b < a:
        print ("guess is low")
        b = int(input("Enter a number from 1 to 999: "))
    elif b > a:
        print ("guess is high")
        b = int(input("Enter a number from 1 to 999: "))
    else:
        print ("you guessed it!")
        break
    print("")
