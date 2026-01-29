import random
game_list = {
    "easy": ("soccer", "tennis", "catch", "hiking","cricket","football","baseball"),
    "medium": ("frisbee", "croquet", "kickball", "archery", "softball", "cycling"),
    "hard": ("badminton", "lacrosse", "paintball", "pickleball", "rounders", "cornhole", "handball")
}
n=1
while n==1 :
    life=3
    guess=[]
    clue=[]
    print("===========================================")
    print("Welcome to the Linear  Outdoor Games Guesser Game!")
    print("You have 3 lives to guess the game correctly.")
    print("===========================================")
    difficulty=input("Choose a difficulty level (easy, medium, hard): ").lower()
    while difficulty not in game_list:
        print("Invalid difficulty level. Please choose again.")
        difficulty=input("Choose a difficulty level (easy, medium, hard): ").lower()
    else:
        chosen_game = random.choice(game_list[difficulty])
        chosen_game_t= list(chosen_game)
        print(f"You have chosen {difficulty} difficulty.")
    while life >0:
        guess = ["_"] * len(chosen_game)
        print(random.shuffle(chosen_game_t))
        for i in range(len(chosen_game)//2):
            a=random.choice(chosen_game_t)
            clue.append(a)
            chosen_game_t.remove(a)
        print("Clue:",clue)
        print(guess)
        for i in range(len(chosen_game)):  
            letter = input("Enter the letter:").lower()
            if letter == chosen_game[i]:
                    guess[i] = chosen_game[i]  
                    print(guess)
            while letter != chosen_game[i] or len(letter)!=1 or letter.isalpha()==False:
                if len(letter)!=1:
                    print("Please enter a single letter at a time.")
                    letter = input("Enter the letter:").lower()
                if letter == chosen_game[i]:
                    guess[i] = chosen_game[i]  
                    print(guess)
                elif letter.isalpha()==False:
                    print("Please enter a valid letter.")
                    letter = input("Enter the letter:").lower()
                    life-=1
                elif letter != chosen_game[i]:  
                    print("Wrong guess. Try again.")
                    letter = input("Enter the letter:").lower()
                    life-=1
        if guess == list(chosen_game):
            print("Congratulations! You've guessed the game:", chosen_game)
            guess=[] 
            life=3
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            n=0 
        elif play_again == "yes":
            n=1
    else:
        print("Sorry, you've run out of lives. The game was:", chosen_game)