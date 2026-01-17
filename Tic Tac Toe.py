import random
print("Tic Tac Toe Game")
entry=["X","O"]
valid=[1,2,3,4,5,6,7,8,9]
user_l=[0]
comp_l=[0]
display_l=[" "," "," "," "," "," "," "," "," "," "]

def display(c_pos,u_pos,c_choose,u_choose):
    display_l[c_pos]=c_choose
    display_l[u_pos]=u_choose
    print(display_l[1],"\t|",display_l[2],"\t|",display_l[3])
    print("---------------------------")
    print(display_l[4],"\t|",display_l[5],"\t|",display_l[6])
    print("---------------------------")
    print(display_l[7],"\t|",display_l[8],"\t|",display_l[9])
    print("---------------------------")

def checking(user_c,comp_c):
    win=[(1,2,3),(4,5,6),(7,8,9),(1,5,9),(3,5,7),(1,4,7),(2,5,8),(3,6,9)]
    for i in win:
        count_user=count_comp=0
        for j in range(3):
            if display_l[i[j]] == user_c:
                count_user+=1
            if display_l[i[j]] == comp_c:
                count_comp+=1
        if count_user==3:
            return"Congrats! You have won against the computer"
        elif count_comp==3:
            return"Computer has won the game against you"
    count_user=count_comp=0
    return ""

n=0   
while n==0:
    user_choice=input("Enter your choice X or O: ")
    user_choice=user_choice.upper()
    if user_choice=="X":
        comp_choice="O"
    elif user_choice=="O":
        comp_choice="X"
    elif user_choice not in entry:
        while (user_choice not in entry):
            print("Your input seems to have an error")
            user_choice=input("Enter your choice X or O: ")
    for i in range(1,10):
        user=int(input("Enter the position: "))
        while (user not in valid):
            print("The position seems to be taken")
            user=int(input("Enter the position: "))
            user_l.append(user)
            valid.remove(user)
        else:
            user_l.append(user)
            valid.remove(user)
        comp=random.choice(valid)
        comp_l.append(comp)
        valid.remove(comp)
        display(comp,user,comp_choice,user_choice)
        print(checking(user_choice,comp_choice))
        if i==9 and checking(user_choice,comp_choice) =="":
            print("This match is a draw")
        elif checking(user_choice,comp_choice) !="":
            break
    #input checking
    n=int(input("Enter 0 to play the game once again else enter someother number:"))   
    if n==0:
        valid=[1,2,3,4,5,6,7,8,9]
        user_l=[]
        comp_l=[]
        display_l=[" "," "," "," "," "," "," "," "," "," "]