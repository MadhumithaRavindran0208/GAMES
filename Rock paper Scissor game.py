print("----Rock paper Scissor game----")
import random
possibilities=["Rock"," paper ","Scissor"]
win=loss=0
n=1
while n!=0:
    for i in range (3):
        n=random.randint(0,2)
        comp=possibilities[n].lower()
        print("Rock , paper , Scissor")
        user=input("Enter your choice:")
        user=user.lower()
        while user not in ["rock","paper","scissor"]:
            print("Invalid input, please choose Rock, paper or Scissor")
            user=input("Enter your choice:")
            user=user.lower()
        if comp==user:
            print("User's choice=",user.title()," Computer's choice=",comp.title())
            print("Draw")
        elif comp=="rock" and user=="scissor":
            print("User's choice=",user.title()," Computer's choice=",comp.title())
            print("Computer wins")
            win+=1
        elif comp=="rock" and user=="paper":
            print("User's choice=",user.title()," Computer's choice=",comp.title())
            print("User wins")
            loss+=1
        elif comp=="paper" and user=="rock":    
            print("User's choice=",user.title()," Computer's choice=",comp.title())
            print("Computer wins")
            win+=1
        elif comp=="paper" and user=="scissor":
            print("User's choice=",user.title()," Computer's choice=",comp.title())
            print("User wins")
            loss+=1
        elif comp=="scissor" and user=="rock":
            print("User's choice=",user.title()," Computer's choice=",comp.title())
            print("User wins")
            loss+=1
        elif comp=="scissor" and user=="paper":
            print("User's choice=",user.title()," Computer's choice=",comp.title())
            print("Computer wins")
            win+=1
    if win>loss:
        print("Sorry! the computer has won the game")
    elif loss>win:
        print("Congrats! You have won the game")
    else:
        print("The game is a draw") 
    n=int(input("If you wanna play again enter any number other than 0:"))
