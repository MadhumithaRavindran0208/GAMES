import random
values=[]
N=1
while N==1:
    for i in range(3):
        a=random.choice(range(1,1001))
        values.append(str(a))
    print("The set of values are:")
    print(values)
    u_sorted=input("Enter the sorted value from the given set separated by commas:")
    u_sorted=list(u_sorted.split(","))
    if u_sorted==sorted(values):
        print("Congratulations! You have selected the correct sorted value.")
    else:
        print("Sorry, the correct sorted value is:", sorted(values))
    values.clear()
    N=int(input("Enter 1 to start the game of finding the sorted number:"))
