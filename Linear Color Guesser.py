import random
color = {
    "easy": (
        "red", 
        "yellow", 
        "white", 
        "black", 
        "blue", 
        "green"
    ),
    "medium": ( 
        "indigo", 
        "magenta", 
        "peach", 
        "crimson"
    ),
    "hard": (
        "chartreuse", 
        "teal", 
        "cyan", 
        "turquoise", 
        "taupe", 
        "mauve"
    )  
}
n=1
while n==1 :
    life=3
    guess=[]
    clue=[]
    print("===========================================")
    print("Welcome to the Linear Colors Guesser Game!")
    print("You have 3 lives to guess the color correctly.")
    print("===========================================")
    difficulty=input("Choose a difficulty level (easy, medium, hard): ").lower()
    while difficulty not in color:
        print("Invalid difficulty level. Please choose again.")
        difficulty=input("Choose a difficulty level (easy, medium, hard): ").lower()
    else:
        chosen_color = random.choice(color[difficulty])
        chosen_color_t= list(chosen_color)
        print(f"You have chosen {difficulty} difficulty.")
    while life >0:
        guess = ["_"] * len(chosen_color)
        print(random.shuffle(chosen_color_t))
        for i in range(len(chosen_color)):
            a=random.choice(chosen_color_t)
            clue.append(a)
            chosen_color_t.remove(a)
        print("Clue:",clue)
        print(guess)
        for i in range(len(chosen_color)):  
            letter = input("Enter the letter:").lower()
            if letter == chosen_color[i]:
                    guess[i] = chosen_color[i]  
                    print(guess)
            while letter != chosen_color[i] or len(letter)!=1 or letter.isalpha()==False:
                if len(letter)!=1:
                    print("Please enter a single letter at a time.")
                    letter = input("Enter the letter:").lower()
                if letter == chosen_color[i]:
                    guess[i] = chosen_color[i]  
                    print(guess)
                elif letter.isalpha()==False:
                    print("Please enter a valid letter.")
                    letter = input("Enter the letter:").lower()
                    life-=1
                elif letter != chosen_color[i]:  
                    print("Wrong guess. Try again.")
                    letter = input("Enter the letter:").lower()
                    life-=1
        if guess == list(chosen_color):
            print("Congratulations! You've guessed the color:", chosen_color)
            guess=[] 
            life=3
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            n=0 
        elif play_again == "yes":
            n=1
    else:
        print("Sorry, you've run out of lives. The color was:", chosen_color)