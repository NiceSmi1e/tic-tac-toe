# -*- coding: utf-8 -*-

board = list(range(1,10)) #defining board from 1 to 9

#Function that draws the board
def draw_board(board):
    print("-------------")
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("-------------")

#Function that takes the input from the player
def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Where should we place " + player_token+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print("Incorrect input. Are you sure that you entered number?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True
            else:
                print("This square is occupied")
        else:
            print("Incorrect input. Enter the number from 1 to 9.")

#Function that check if the game is won
def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)) #combination of places for the win
    for each in win_coord: #going through every possible winning combo
        #print("DEBUG: ",board[each[0]],board[each[1]],board[each[2]],"   ",each[0],each[1],each[2])
        if board[each[0]] == board[each[1]] == board[each[2]]: #if the character are the same -> win
            return board[each[0]] #returning who won
    return False

#Main function
def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, "won!")
                win = True
                break
        if counter == 9:
            print("Draw!")
            break
    draw_board(board)                

main(board)
