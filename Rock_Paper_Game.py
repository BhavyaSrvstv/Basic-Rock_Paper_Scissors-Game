import random 
list=[0,-1,1]

print("---------------------------------ROCK_PAPER_SCISSORS---------------------------------")
print("The rules of the game are:")
print("------------1 is for Paper------------\n------------0 is for Rock------------\n------------ -1 is for Scissors------------")

score=0
def game():
 global score 
 for i in range(3):
    user_choice = int(input("Enter a value: "))
    # while not user_choice:
    #    print("Input cannot be empty.")
    #    user_choice=int(input(print("Enter your choice:->")))


    if user_choice<=1 and user_choice>=-1:
     random_num = random.choice(list)
     if user_choice == 0:
        if random_num == 1:
            print("You chose Rock, Computer chose Paper")
            print("You lost this round")
            if score !=0:
             score = score - 1
        elif random_num == -1:
            print("You chose Rock, Computer chose Scissors")
            print("You won this round")
            score=score+1
        else:
            print("You chose Rock, Computer chose Rock")
            print("It's a tie")
     elif user_choice == 1:
        if random_num == 0:
            print("You chose Paper, Computer chose Rock")
            print("You won this round")
            score=score+1
        elif random_num == -1:
            print("You chose Paper, Computer chose Scissors")
            print("You lost this round")
            if score !=0:
             score = score - 1
        else:
            print("You chose Paper, Computer chose Paper")
            print("It's a tie")
     else:
        if random_num == 0:
            print("You chose Scissors, Computer chose Rock")
            print("You lost this round")
            if score !=0:
             score = score - 1
        elif random_num == 1:
            print("You chose Scissors, Computer chose paper ")
            print("You won this round")
            score=score+1
        else:
            print("You chose Scissors, Computer chose Scissors ")
            print("It's a tie")
    else:
       print("Invalid Input")
    print(f"-----------||Your total score is:{score}||-----------")





game()

decide=input("Do you want to play again? (y/n)") #need to fix the none value which this is returning

if(decide=='y'):
    game()
else:
    exit


        
    
