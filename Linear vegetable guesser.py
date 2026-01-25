import random
vegetable_list = {
    "easy": ("corn", "peas", "kale", "okra", "yam", "onion"),
    "medium": ("carrot", "potato", "radish", "tomato", "celery", "garlic"),
    "hard": ("zucchini", "broccoli", "eggplant", "asparagus", "artichoke", "beetroot")
}
n=1
while n==1 :
    life=3
    guess=[]
    clue=[]
    print("===========================================")
    print("Welcome to the Linear Vegetable Guesser Game!")
    print("You have 3 lives to guess the vegetable correctly.")
    print("===========================================")
    difficulty=input("Choose a difficulty level (easy, medium, hard): ").lower()
    while difficulty not in vegetable_list:
        print("Invalid difficulty level. Please choose again.")
        difficulty=input("Choose a difficulty level (easy, medium, hard): ").lower()
    else:
        chosen_vegetable= random.choice(vegetable_list[difficulty])
        chosen_vegetable_t= list(chosen_vegetable)
        print(f"You have chosen {difficulty} difficulty.")
    while life >0:
        guess = ["_"] * len(chosen_vegetable)
        for i in range(len(chosen_vegetable)):
            a=random.choice(chosen_vegetable_t)
            clue.append(a)
            chosen_vegetable_t.remove(a)
        print("Clue:",clue)
        print(guess)
        for i in range(len(chosen_vegetable)):  
            letter = input("Enter the letter:").lower()
            if letter == chosen_vegetable[i]:
                    guess[i] = chosen_vegetable[i]  
                    print(guess)
            while letter != chosen_vegetable[i] or len(letter)!=1 or letter.isalpha()==False:
                if len(letter)!=1:
                    print("Please enter a single letter at a time.")
                    letter = input("Enter the letter:").lower()
                if letter == chosen_vegetable[i]:
                    guess[i] = chosen_vegetable[i]  
                    print(guess)
                elif letter.isalpha()==False:
                    print("Please enter a valid letter.")
                    letter = input("Enter the letter:").lower()
                    life-=1
                elif letter != chosen_vegetable[i]:  
                    print("Wrong guess. Try again.")
                    letter = input("Enter the letter:").lower()
                    guess[i] = chosen_vegetable[i]  
                    life-=1
                    print(guess)
        if guess == list(chosen_vegetable):
            print("Congratulations! You've guessed the vegetable:", chosen_vegetable)
            guess=[] 
            life=3
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            n=0 
        elif play_again == "yes":
            n=1
    else:
        print("Sorry, you've run out of lives. The vegetable was:", chosen_vegetable)