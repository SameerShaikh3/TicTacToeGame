import random
print("The Snake Water Game\n")
inp_1=str(input("Enter \ns for snake \nw for water\ng for gun: "))
if inp_1=="s":
    lst=["snake","water","gun"]
    ran=random.choice(lst)
    if ran=="snake":
        print("oops try again! you lost the game ")
        print("the computer choosed snake")
    elif ran=="water":
        print("Congrats you won the game")
        print("the computer choosed water")
    elif ran=="gun":
        print("oops you lost the game")
        print("the computer choosed gun")
    else:
        print()
if inp_1=="w":
    
    lst=["snake","water","gun"]
    ran=random.choice(lst)
    if ran=="snake":
        print("oops try again! you lost the game ")
        print("the computer choosed snake")
    elif ran=="water":
        print("oops try! ")
        print("the computer choosed water")
    elif ran=="gun":
        print("Congrats you won the game")
        print("the computer choosed gun")
    else:
        print()
if inp_1=="g":
    
    lst=["snake","water","gun"]
    ran=random.choice(lst)
    if ran=="snake":
        print("Cngrats you won the game")
        print("the computer choosed snake")
    elif ran=="water":
        print("oops try! ")
        print("the computer choosed water")
    elif ran=="gun":
        print("oops you lost the game")
        print("the computer choosed gun")
    else:
        print()