import random
fruit_list = {
    "easy": ("apple", "banana", "cherry", "dragonfruit", "elderberry"),
    "medium": ("fig", "grape", "honeydew", "kiwi", "lemon", "mango"),
    "hard": ("nectarine", "orange", "papaya", "quince", "raspberry", "starfruit", "tangerine")}
n=1
while n==1 :
    life=3
    guess=[]
    clue=[]
    print("===========================================")
    print("Welcome to the Linear Fruits Guesser Game!")
    print("You have 3 lives to guess the fruit correctly.")
    print("===========================================")
    difficulty=input("Choose a difficulty level (easy, medium, hard): ").lower()
    while difficulty not in fruit_list:
        print("Invalid difficulty level. Please choose again.")
        difficulty=input("Choose a difficulty level (easy, medium, hard): ").lower()
    else:
        chosen_fruit = random.choice(fruit_list[difficulty])
        chosen_fruit_t= list(chosen_fruit)
        print(f"You have chosen {difficulty} difficulty.")
    while life >0:
        guess = ["_"] * len(chosen_fruit)
        print(random.shuffle(chosen_fruit_t))
        for i in range(len(chosen_fruit)):
            a=random.choice(chosen_fruit_t)
            clue.append(a)
            chosen_fruit_t.remove(a)
        print("Clue:",clue)
        print(guess)
        for i in range(len(chosen_fruit)):  
            letter = input("Enter the letter:").lower()
            if letter == chosen_fruit[i]:
                    guess[i] = chosen_fruit[i]  
                    print(guess)
            while letter != chosen_fruit[i] or len(letter)!=1 or letter.isalpha()==False:
                if len(letter)!=1:
                    print("Please enter a single letter at a time.")
                    letter = input("Enter the letter:").lower()
                if letter == chosen_fruit[i]:
                    guess[i] = chosen_fruit[i]  
                    print(guess)
                elif letter.isalpha()==False:
                    print("Please enter a valid letter.")
                    letter = input("Enter the letter:").lower()
                    life-=1
                elif letter != chosen_fruit[i]:  
                    print("Wrong guess. Try again.")
                    letter = input("Enter the letter:").lower()
                    life-=1
        if guess == list(chosen_fruit):
            print("Congratulations! You've guessed the fruit:", chosen_fruit)
            guess=[] 
            life=3
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            n=0 
        elif play_again == "yes":
            n=1
    else:
        print("Sorry, you've run out of lives. The fruit was:", chosen_fruit)