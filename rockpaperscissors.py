p1={"a1":"rock","a2":"paper","a3":"scissor"}
p2={"a1":"rock","a2":"paper","a3":"scissor"}
a=input("Enter for player 1:")
b=input("Enter for player 2:")
count=0
def action(a,b):
    if (a==p1["a1"] and b==p2["a1"]):
        print("Draw")
        return 0
    if (a==p1["a1"] and b==p2["a2"]):
        print("Player2 WON")
        return 0
    if (a==p1["a1"] and b==p2["a3"]):
        print("Player1 WON")
        return 0
    if (a==p1["a2"] and b==p2["a1"]):
        print("Player1 WON")
        return 0
    if (a==p1["a2"] and b==p2["a2"]):
        print("Draw")
        return 0
    if (a==p1["a2"] and b==p2["a3"]):
        print("Player2 WON")
        return 0
    if (a==p1["a3"] and b==p2["a1"]):
        print("Player1 WON")
        return 0
    if (a==p1["a3"] and b==p2["a2"]):
        print("Player1 WON")
        return 0
    if (a==p1["a3"] and b==p2["a3"]):
        print("Draw")
        return 0
    else:
        print("Invalid Match")
        return o
while True:
    action(a,b)
    count+=1
    e=input("Do u want to continue(yes/no)")
    if (e=="yes"):
        a=input("Enter for player 1:")
        b=input("Enter for player 2:")
    else:
        break
print("No of plays: ",count)        

