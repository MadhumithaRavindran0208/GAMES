import random
distribution_list = {
    "easy": ("bernoulli", "binomial", "normal", "poisson", "uniform"),
    "medium": ("beta", "exponential", "gamma", "lognormal", "logistic", "rayleigh"),
    "hard": ("Cauchy", "Dirichlet", "chisquare", "Pareto", "Weibull")}
n=1
while n==1 :
    life=3
    guess=[]
    clue=[]
    print("===========================================")
    print("Welcome to the Linear Distribution Guesser Game!")
    print("You have 3 lives to guess the distribution correctly.")
    print("===========================================")
    difficulty=input("Choose a difficulty level (easy, medium, hard): ").lower()
    while difficulty not in distribution_list:
        print("Invalid difficulty level. Please choose again.")
        difficulty=input("Choose a difficulty level (easy, medium, hard): ").lower()
    else:
        chosen_distribution = random.choice(distribution_list[difficulty])
        chosen_distribution_t= list(chosen_distribution)
        print(f"You have chosen {difficulty} level.")
    while life >0:
        guess = ["_"] * len(chosen_distribution)
        print(random.shuffle(chosen_distribution_t))
        for i in range(len(chosen_distribution)):
            a=random.choice(chosen_distribution_t)
            clue.append(a)
            chosen_distribution_t.remove(a)
        print("Clue:",clue)
        print(guess)
        for i in range(len(chosen_distribution)):  
            letter = input("Enter the letter:").lower()
            if letter == chosen_distribution[i]:
                    guess[i] = chosen_distribution[i]  
                    print(guess)
            while letter != chosen_distribution[i] or len(letter)!=1 or letter.isalpha()==False:
                if len(letter)!=1:
                    print("Please enter a single letter at a time.")
                    letter = input("Enter the letter:").lower()
                if letter == chosen_distribution[i]:
                    guess[i] = chosen_distribution[i]  
                    print(guess)
                elif letter.isalpha()==False:
                    print("Please enter a valid letter.")
                    letter = input("Enter the letter:").lower()
                    life-=1
                elif letter != chosen_distribution[i]:  
                    print("Wrong guess. Try again.")
                    letter = input("Enter the letter:").lower()
                    life-=1
        if guess == list(chosen_distribution):
            print("Congratulations! You've guessed the distribution:", chosen_distribution)
            guess=[] 
            life=3
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            n=0 
        elif play_again == "yes":
            n=1
    else:
        print("Sorry, you've run out of lives. The distribution was:", chosen_distribution)