# Name - Rohit Bej
# Roll no - 24ME10135
# Role - Trainee Developer

import random 

# Gamebox to store and show the game 
game_box = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

# Box to show user what to input
user_box = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]


# Printing the Game
def print_game(a):
    print(a[0][0] + " | " + a[0][1] + " | " + a[0][2])
    print("--+---+--")
    print(a[1][0] + " | " + a[1][1] + " | " + a[1][2])
    print("--+---+--")
    print(a[2][0] + " | " + a[2][1] + " | " + a[2][2])


# Winning conditions
def check_win(a):
    for row in a:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return True
    for i in range(3):
        if a[0][i] == a[1][i] == a[2][i] and a[0][i] != ' ':
            return True
    if a[0][0] == a[1][1] == a[2][2] and a[0][0] != ' ':
        return True
    if a[0][2] == a[1][1] == a[2][0] and a[0][2] != ' ':
        return True
    return False


# Check Draw
def check_draw(a):
    for row in a:
        for col in row:
            if col == " ":
                return False
    return True


# Mapping to coordinates
def map_to_coordinates(ch):
    row = (ch - 1) // 3
    col = (ch - 1) % 3
    return row, col


# User input
def user_input(c):
    print("Your Turn!")
    print_game(user_box)
    while True:
        try:
            ch = int(input("Enter the number on the box to play your move: "))
            if 1 <= ch <= 9:
                row, col = map_to_coordinates(ch)
                if game_box[row][col] == ' ':
                    game_box[row][col] = c
                    user_box[row][col] = c
                    break
                else:
                    print("Already Filled Box, Try another Box")
            else:
                print("Invalid Box")
        except ValueError:
            print("Please enter a valid integer")
    print("You Played")
    print_game(game_box)


# Computer input
def com_input(c):
    print("Computer's Turn")
    while True:
        ch = random.randint(1, 9)
        row, col = map_to_coordinates(ch)
        if game_box[row][col] == ' ':
            game_box[row][col] = c
            user_box[row][col] = c
            break
    print("Computer played!")
    print_game(game_box)


# Main Game Loop
print("------Welcome to Tic Tac Toe------")
print("1. Play as 'X'")
print("2. Play as 'O'")

while True:
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            while True:
                user_input("X")
                if check_win(game_box):
                    print("You won!")
                    break
                if check_draw(game_box):
                    print("It's a draw!")
                    break
                com_input("O")
                if check_win(game_box):
                    print("Computer won!")
                    break
                if check_draw(game_box):
                    print("It's a draw!")
                    break
            break
        elif choice == 2:
            while True:
                com_input("X")
                if check_win(game_box):
                    print("Computer won!")
                    break
                if all(cell != ' ' for row in game_box for cell in row):
                    print("It's a draw!")
                    break
                user_input("O")
                if check_win(game_box):
                    print("You won!")
                    break
                if all(cell != ' ' for row in game_box for cell in row):
                    print("It's a draw!")
                    break
            break
        else:
            print("Invalid choice!")
    except ValueError:
        print("Please enter a valid integer")
