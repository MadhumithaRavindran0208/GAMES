import random
print("Guess the secret number game")
n=random.randint(0,100)
def guess():
    num=int(input("Guess the secret number b/w (0,100):"))
    if -1<num<101:
        return (num)
    else:
        raise ValueError("The given value isn't in the range required")
num=guess()
count=0
while num!=n and count<3:
    if num<n:
        print("The secret number is greater than the given number")
        num=guess()
    elif num>n:
        print("The secret number is lesser than the given number")
        num=guess()
    count+=1
else:
    if num==n:
        print("Congrats you have found the secret number")
    else:
        print("Sorry you have failed to find the secret number")
       