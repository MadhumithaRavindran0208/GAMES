import random
print("Thief and the values game")
print("Default number of items is 5")
print("""How the game works:
      1.The player gets to enter the product's weight and the value and the weight of it which willbe given as an input to the dictionary
      2.The snapsack in which the products will be placed will have a default weight limit 
      3.The products from the dictionary will be placed in the knapsack by genrating a random number.
      4.If the maximum value is gained by the snapsack within it's default weight limit then the player gets announced as the winner or the user will be announced as the loser 
      5.The user gets to play the game as many times as they wish for""")
dict1={}
weight1=[]
value1=[]
weight_s=0
value_s=0
weightcheck=0
print("Make sure there is no repetition of the values in weight")
for i in range (5):
    value=int(input("Enter the value of the product:"))
    weight=int(input("Enter the weight of the product:"))
    dict1[weight]=value
    weight1.append(weight)
    value1.append(value)
print(dict1)
snapsack=int(input("Enter the weight limit of the sack:"))
max_value=int(input("Enter the max value that can be collected by the thief:"))
N=1
while N==1 :
    for i in range (5):
            n=random.randint(0,4)
            print(f"n={n}")
            weightcheck+=weight1[n]
            if weightcheck<snapsack:
                weight_s+=weight1[n]
                value_s+=value1[n]
            else:
                break
    print("The value of the products that have been theft under the weight limit of snapsack=",value_s)
    if value_s>=max_value:
        print("Congrats! You have won the game")
    else:
        print("Sorry! Better luck next time")
    weightcheck=0
    weight_s=0
    value_s=0
    N=int(input("Enter 1 if you wanna try again or any other number if wanna exit the game:")) 