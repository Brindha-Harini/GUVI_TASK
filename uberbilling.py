p1=int(input("enter from"))
p2=int(input("enter dest"))
e=str(input("cab or auto or mini"))
def fare(e):
        c=p1-p2
        if(e=="cab"):
                f=c*10
                return f
        elif(e=="auto"):
                f=c*5
                return f
        elif(e=="mini"):
                f=c*7
                return f
        else:
            return 0
print("********************************************************")
print("********************************************************")
print("FARE")
print("from: ",p1)
print("Destination",p2)
print("Mode of Transport",e)
print("total cost:",fare(e))
