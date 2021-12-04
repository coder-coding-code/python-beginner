# rock paper scissors
# ask user rock paper or scissors
# match with computer
# p-r, r-s, p-s
import random

computer = ['rock', 'paper', 'scissors']

user_points = 0
computer_points = 0

def ask():
    user_points = 0
    computer_points = 0
    on = True
    while on:
        print("type in 'rock', 'paper' or 'scissors' ")
        user_choice = input("You chose: ")
        computer_choice = computer[random.randint(0,2)]
        print(f'computer chose --- {computer_choice}')

        if user_choice != computer_choice:
            if user_choice == 'rock' and computer_choice == 'scissors':
                user_points += 1
            elif user_choice == 'scissors' and computer_choice == 'paper':
                user_points += 1
            elif user_choice == 'paper' and computer_choice == 'rock':
                user_points += 1
            elif user_choice == computer_choice:
                user_points += 0
            else:
                computer_points += 1
    
            if computer_points == 5:
                print('you lose!!!')
                on = False
            elif user_points == 5:
                print("you win!!!")
                on = False

ask()
