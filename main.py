import random
# user win counter
user_win = 0
# computer win counter
computer_win = 0
# game options list
options = ["rock", "paper", "scissors"]

# loop to run the game
while True:
    print("welcome to the game")
    # user input in converted in lower case to match options and if statements
    user_input = input("please write (rock) or (paper) or (scissors) or (q) to quit\n").lower()
    # it will break the loop and go to the last line
    if user_input == "q":
        break
    # if user enter something not in the options list restart loop
    elif user_input not in options:
        continue
    # create the random number in the range of option list
    random_number = random.randint(0, len(options)-1)
    # computer random select from options list
    computer_select = options[random_number]
    # print the computer selection
    print(f"computer: {computer_select}")
    # in case the user input is winning the computer select
    if user_input == "rock" and computer_select == "scissors" or user_input == "paper" and computer_select == "rock" or\
            user_input == "scissors" and computer_select == "paper":
        print("you win")
        # add one to user win counter
        user_win += 1
    # in case the user and computer equal
    elif user_input == computer_select:
        print("tie")
    # in case computer select winning the user input
    else:
        print("computer wins")
        # add to computer win counter
        computer_win += 1
    # print the total score
    print(f"score is: you {user_win} , computer {computer_win} .")
# end game
print("goodbye")