print("Snake ,Water ,Gun game")
import random
possibilities=["Snake","Water","Gun"]
win=loss=0
n=1
while n!=0:
    for i in range (3):
        n=random.randint(0,2)
        comp=possibilities[n].lower()
        print("Snake","Water","Gun")
        user=input("Enter your choice:")
        user=user.lower()
        while user not in ["snake","water","gun"]:
            print("Invalid input, please choose Snake, Water or Gun")
            user=input("Enter your choice:")
            user=user.lower()
        if comp==user:
            print("User's choice=",user.upper," Computer's choice=",comp)
            print("Draw")
        elif comp=="snake" and user=="gun":
            print("User's choice=",user.upper," Computer's choice=",comp)
            print("Computer wins")
            win+=1
        elif comp=="snake" and user=="water":
            print("User's choice=",user.upper," Computer's choice=",comp)
            print("User wins")
            loss+=1
        elif comp=="water" and user=="snake":    
            print("User's choice=",user.upper," Computer's choice=",comp)
            print("Computer wins")
            win+=1
        elif comp=="water" and user=="gun":
            print("User's choice=",user.upper," Computer's choice=",comp)
            print("User wins")
            loss+=1
        elif comp=="gun" and user=="snake":
            print("User's choice=",user.upper," Computer's choice=",comp)
            print("User wins")
            loss+=1
        elif comp=="gun" and user=="water":
            print("User's choice=",user.upper," Computer's choice=",comp)
            print("Computer wins")
            win+=1
    if win>loss:
        print("Sorry! the computer has won the game")
    elif loss>win:
        print("Congrats! You have won the game")
    else:
        print("The game is a draw") 
    n=int(input("If you wanna play again enter any number other than 0:"))