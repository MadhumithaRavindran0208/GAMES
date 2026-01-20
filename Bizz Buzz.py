import random
print("Bizz Buzz game")
n=1
while n==1:
    n=random.choice([3,5,7,9,11])
    print("The choosen number is :",n)
    u_loss="no"
    c_loss= "no"
    while u_loss!= "yes":
        computer=0
        print("LET'S START THE GAME")
        print(1)
        for i in range(1000):
            computer+=2
            if computer%n==0:
                temp=computer
                computer="Buzz"
                print("Computer:",computer)
                computer=temp
            else:
                print("Computer:",computer)
            user=input("User:")
            if user.isalpha():
                user=user.capitalize()
            check=computer+1
            if check%n==0 and user!="Buzz":
                print("User lost the game by not saying Buzz")
                u_loss= "yes"
                continue
            elif check%n==0 and user=="Buzz":
                continue
            elif int(user)!=check:
                print("User lost the game by enterning wrong number")
                u_loss= "yes"
                continue
            elif int(user)==check:
                continue
        n=int(input("Enter a 1 to continue or any other number to exit:"))
