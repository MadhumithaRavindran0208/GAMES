import random
data=set()
values=[]
N=1
for i in range (1001):
        data.add(i)
while N==1:
    for i in range(10):
        a=random.choice(list(data))
        values.append(a)
    print("The set of values are:")
    print(values)
    u_largest=int(input("Enter the largest value from the given set:"))
    if u_largest==max(values):
        print("Congratulations! You have selected the correct largest value.")
    else:
        print("Sorry, the correct largest value is:", max(values))
    values.clear()
    N=int(input("Enter 1 to start the game of finding the largest number:"))
