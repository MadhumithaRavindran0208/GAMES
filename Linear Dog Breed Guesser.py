import random
dog_breeds = {
    "easy": (
        "labradorretriever","goldenretriever",
        "pug"
    ),
    "medium": (         
        "goldendoodle","borderterrier",
        "australianshepherd","boxer"
    ),
    "hard": (
        "belgianmalinois","siberianhusky",
        "akita","bordercollie%"
    )
}
n=1
while n==1 :
    life=3
    guess=[]
    clue=[]
    print("===========================================")
    print("Welcome to the Linear Dog Breeds Guesser Game!")
    print("You have 3 lives to guess the dog breed correctly.")
    print("===========================================")
    difficulty=input("Choose a difficulty level (easy, medium, hard): ").lower()
    while difficulty not in dog_breeds:
        print("Invalid difficulty level. Please choose again.")
        difficulty=input("Choose a difficulty level (easy, medium, hard): ").lower()
    else:
        chosen_breed = random.choice(dog_breeds[difficulty])
        chosen_breed_t= list(chosen_breed)
        print(f"You have chosen {difficulty} difficulty.")
    while life >0:
        guess = ["_"] * len(chosen_breed)
        print(random.shuffle(chosen_breed_t))
        for i in range(len(chosen_breed)):
            a=random.choice(chosen_breed_t)
            clue.append(a)
            chosen_breed_t.remove(a)
        print("Clue:",clue)
        print(guess)
        for i in range(len(chosen_breed)):  
            letter = input("Enter the letter:").lower()
            if letter == chosen_breed[i]:
                    guess[i] = chosen_breed[i]  
                    print(guess)
            while letter != chosen_breed[i] or len(letter)!=1 or letter.isalpha()==False:
                if len(letter)!=1:
                    print("Please enter a single letter at a time.")
                    letter = input("Enter the letter:").lower()
                if letter == chosen_breed[i]:
                    guess[i] = chosen_breed [i]  
                    print(guess)
                elif letter.isalpha()==False:
                    print("Please enter a valid letter.")
                    letter = input("Enter the letter:").lower()
                    life-=1
                elif letter != chosen_breed[i]:  
                    print("Wrong guess. Try again.")
                    letter = input("Enter the letter:").lower()
                    life-=1
        if guess == list(chosen_breed):
            print("Congratulations! You've guessed the dog breed:", chosen_breed)
            guess=[] 
            life=3
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            n=0 
        elif play_again == "yes":
            n=1
    else:

        print("Sorry, you've run out of lives. The dog breed was:", chosen_breed)
