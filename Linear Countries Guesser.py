import random
countries_list = {
    "easy": (
        'australia', 'brazil', 'canada', 'china', 'egypt', 'france', 'germany', 'india', 'italy', 'japan', 'mexico', 'russia', 'south africa', 'spain', 'thailand', 'turkey'
    ),
    "medium": (
        'algeria', 'belgium', 'chile', 'croatia', 'denmark', 'finland', 'hungary', 'indonesia', 'ireland', 'kenya', 'malaysia', 'morocco', 'new zealand', 'norway', 'peru', 'philippines', 'poland', 'portugal', 'sweden', 'vietnam'
    ),
    "hard": (
         'burkina faso', 'comoros', 'djibouti', 'eritrea', 'gabon', 'guinea-bissau', 'kiribati', 'lesotho', 'mauritania', 'micronesia', 'nauru', 'palau', 'sao tome and principe', 'suriname', 'timor-leste', 'togo', 'tuvalu', 'vanuatu'
    )
}
while n==1 :
    life=3
    guess=[]
    clue=[]
    print("===========================================")
    print("Welcome to the Linear Countries Guesser Game!")
    print("You have 3 lives to guess the country correctly.")
    print("===========================================")
    difficulty=input("Choose a difficulty level (easy, medium, hard): ").lower()
    while difficulty not in countries_list:
        print("Invalid difficulty level. Please choose again.")
        difficulty=input("Choose a difficulty level (easy, medium, hard): ").lower()
    else:
        chosen_country = random.choice(countries_list[difficulty])
        chosen_country_t= list(chosen_country)
        print(f"You have chosen {difficulty} difficulty.")
    while life >0:
        guess = ["_"] * len(chosen_country)
        print(random.shuffle(chosen_country_t))
        for i in range(len(chosen_country)//3):
            a=random.choice(chosen_country_t)
            clue.append(a)
            chosen_country_t.remove(a)
        print("Clue:",clue)
        print(guess)
        for i in range(len(chosen_country)):  
            letter = input("Enter the letter:").lower()
            if letter == chosen_country[i]:
                    guess[i] = chosen_country[i]  
                    print(guess)
            while letter != chosen_country[i] or len(letter)!=1 or letter.isalpha()==False:
                if len(letter)!=1:
                    print("Please enter a single letter at a time.")
                    letter = input("Enter the letter:").lower()
                if letter == chosen_country[i]:
                    guess[i] = chosen_country[i]  
                    print(guess)
                elif letter.isalpha()==False:
                    print("Please enter a valid letter.")
                    letter = input("Enter the letter:").lower()
                    life-=1
                elif letter != chosen_country[i]:  
                    print("Wrong guess. Try again.")
                    letter = input("Enter the letter:").lower()
                    life-=1
        if guess == list(chosen_country):
            print("Congratulations! You've guessed the country:", chosen_country)
            guess=[] 
            life=3
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            n=0 
        elif play_again == "yes":
            n=1
    else:
        print("Sorry, you've run out of lives. The country was:", chosen_country)   