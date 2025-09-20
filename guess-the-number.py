import random
def play_game(limit):
    try :
        with open ("score.txt" , "r") as file :
            last_score = file .read()
            print("Last time you try " , last_score , " times !")
    except FileNotFoundError :
        print("This is your first time !")
    computer_choice = random.randint(0 , limit)
    count = 0
    print(f"I picked a number between 0 and {limit}. Try to guess the number.")
    while True:
        user_choice = int(input("Please guess the Number ! :"))
        count += 1
        if user_choice == computer_choice :
            print("Congratulations")
            print("You try " , count , " times !" )
            with open ("score.txt" , "w") as file :
                file . write(str(count))
            play_again = input("Do you want to play again ? ( Yes / No )")
            if play_again . lower() != "yes" :
                print ("Thanks for palating my game !")
                break
            else :
                computer_choice = random . randint (0 , limit)
                count = 0
                continue
        elif user_choice > computer_choice :
            print("--Smaller !--")
        else :
            print("--Bigger !--")
while True :
    game_level = input(" Please select difficulity level : 1-Easy (0 , 50 ) 2-Normal (0 , 100) 3-Hard (0 , 200) (Just write number !)")
    if game_level == "1" :
        play_game(50)
    elif game_level == "2" :
        play_game(100)
    elif game_level == "3" :
        play_game(200)
    else :
        print(" You wrote wrong number ! Try again !")
        continue

