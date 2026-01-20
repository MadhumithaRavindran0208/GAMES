import random
values=[]
N=1
while N==1:
    for i in range(10):
        a=random.choice(range(1,1001))
        values.append(a)
    print("The set of values are:")
    print(values)
    u_smallest=int(input("Enter the smallest value from the given set:"))
    if u_smallest==min(values):
        print("Congratulations! You have selected the correct smallest value.")
    else:
        print("Sorry, the correct smallest value is:", min(values))
    values.clear()
    N=int(input("Enter 1 to start the game of finding the smallest number:"))
