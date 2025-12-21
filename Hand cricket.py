import random
print("Hand cricket")
print("--------------")
list1=["BOWLING","BATTING"]
balls=int(input("Enter the number of balls:"))
odd_or_even=input("odd or even?")
n=random.randint(0,1)
print("The generated random number is ",n)
odd_or_even=odd_or_even.upper()
runs_u=0
runs_c=0
int_u=[]
int_u1=[]
int_c=[]
int_c1=[]

print("----------------*---------------")
if n%2==0 and odd_or_even=="EVEN":
    print("Congrats! You have won the toss")
    bowling_or_batting_u=input("Bowling or Batting?")
    bowling_or_batting_u=bowling_or_batting_u.upper()
elif n%2==1 and odd_or_even=="ODD":
    print("Congrats! You have won the toss")
    bowling_or_batting_u=input("Bowling or Batting?")
    bowling_or_batting_u=bowling_or_batting_u.upper()
else:
    print("Sorry!You have lost the toss")
    bowling_or_batting_u=list1[n]

def bowling():
    global runs_c
    print("You are now bowling")
    for i in range(balls):
        num_u=int(input("Enter your runs:"))
        if num_u<=10:
            int_u.append(num_u)
        else:
            raise ValueError("Enter a value less than 10")
        num_c=random.randint(0,10)
        print("Runs entered by the computer=",num_c)
        int_c.append(num_c)
        if int_c[i]==int_u[i]:
            break;
        elif int_c[i]==0 and int_u[i]>0:
            runs_c+=int_u[i]
        elif int_u[i]==0 and int_c[i]>0:
            runs_c+=int_c[i]
        else:
            runs_c+=int_c[i]
        print("Total runs=",runs_c)
        print("\n")

def bowling1():
    global runs_c
    print("You are now bowling")
    for i in range(balls):
        num_u=int(input("Enter your runs:"))
        if num_u<=10:
            int_u1.append(num_u)
        else:
            raise ValueError("Enter a value less than 10")
        num_c=random.randint(0,10)
        print("Runs entered by the computer=",num_c)
        int_c1.append(num_c)
        if int_c1[i]==int_u1[i]:
            break;
        elif int_c1[i]==0 and int_u1[i]>0:
            runs_c+=int_u1[i]
        elif int_u1[i]==0 and int_c1[i]>0:
            runs_c+=int_c1[i]
        else:
            runs_c+=int_c1[i]
        print("Total runs=",runs_c)
        print("\n")
        if runs_c>runs_u:
            break;
        else:
            continue

def batting():
    global runs_u
    print("You are now batting")
    for i in range(balls):
        num_u=int(input("Enter your runs:"))
        if num_u<=10:
            int_u.append(num_u)
        else:
            raise ValueError("Enter a value less than 10:")
        num_c=random.randint(0,10)
        print("Runs entered by the computer=",num_c)
        int_c.append(num_c)
        if int_u[i]==int_c[i]:
            break;
        elif int_u[i]==0 and int_c[i]>0:
            runs_u+=int_c[i]
        elif int_c[i]==0 and int_u[i]>0:
            runs_u+=int_u[i]
        else:
            runs_u+=int_u[i]
        print("Total runs=",runs_u)
        print("\n")

def batting1():
    global runs_u
    print("You are now batting")
    for i in range(balls):
        num_u=int(input("Enter your runs:"))
        if num_u<=10:
            int_u1.append(num_u)
        else:
            raise ValueError("Enter a value less than 10:") 
        num_c=random.randint(0,10)
        print("Runs entered by the computer=",num_c)
        int_c.append(num_c)
        if int_u1[i]==int_c1[i]:
            break;
        elif int_u1[i]==0 and int_c1[i]>0:
            runs_u+=int_c1[i]
        elif int_c1[i]==0 and int_u1[i]>0:
            runs_u+=int_u1[i]
        else:
            runs_u+=int_u1[i]
        print("Total runs=",runs_u)
        print("\n")
        if runs_u>runs_c:
            break;
        else:
            continue

if bowling_or_batting_u=="BOWLING":
    bowling()
    print("Total runs by the computer=",runs_c)
    print("\n")
    print("----------*----------")   
    batting1()
    print("Total runs by you=",runs_u)
    print("\n")
    print("----------*----------")    
    del(bowling_or_batting_u)

elif bowling_or_batting_u=="BATTING":
    batting()
    print("Total runs by you=",runs_u)
    print("\n")
    print("----------*----------")    
    bowling1()
    print("Total runs by the computer=",runs_c)
    print("\n")
    print("----------*----------")   
    del(bowling_or_batting_u)

else:
    print("Check your input")

print("----------*----------") 
print("Total runs by you=",runs_u)   
print("Total runs by the computer=",runs_c)  
print("----------*----------") 

if runs_u>runs_c:
    print("Congrats! You have won the game against the computer")
    print("----------*----------") 
elif runs_c>runs_u:
    print("Sorry!You have lost the game against the computer") 
    print("----------*----------") 
elif runs_c==runs_u:
    print("Oops!It's a draw")
    print("----------*----------") 