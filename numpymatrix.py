import numpy as np
import random
import pygame
import sys
import pdb

##COLOR USED FOR THE ON SCREEN ELEMENTS
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

def who_goes_first():
	randinteger= random.randint(1,10)
	print("In order to decide who starts this game. We will calculate a random number and see who can come closest to guessing it.")
	player0_number = int(input("Player 0, Please select a number from 1 to 10:"))
	player1_number = int(input("Player 1, Please select a number from 1 to 10:"))
	player0_diff = abs(player0_number - randinteger)
	player1_diff = abs(player1_number - randinteger)

	if (player0_diff < player1_diff): 
		return 0

	else:
		return 1


def create_board():
	board = np.zeros((ROW_LENGTH, COLUMN_LENGTH), dtype = int)
	return board

def modify_board(col, val):
	if col >= COLUMN_LENGTH:
		raise ValueError("This column value is NOT between 0 and 6. Please Try Again.")
	i = ROW_LENGTH - 1
	while board[i][col] != 0:
		i = i - 1
		if i < 0:
			raise ValueError("This column is full. Please Try Another column.")
	board[i][col] = val

def get_user_input (player_number):

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			print ("")

	# if player_number != 0 and player_number != 1:
	# 	raise ValueError("This is only a two player game.")
	# user_coordinates = input("Player " + str(player_number) + " , Please add the column number of where you would like to place your piece:")
	# col = int(user_coordinates[0])
	# return col
	return 0

def set_game_over(player):
	global game_over, winner
	game_over = True
	winner = player

def is_game_over():
	#horizontal determination
	for r in range(ROW_LENGTH):
		for c in range(COLUMN_LENGTH-3):
			window = [board[r][c], board[r][c+1], board[r][c+2], board[r][c+3]]
			if(window.count(1) == 4):
				set_game_over(0)
				return
			elif(window.count(2) == 4):
				set_game_over(1)
				return

	#vertical determination			
	for c in range(COLUMN_LENGTH):
		for r in range(ROW_LENGTH-3):
			window = [board[r][c], board[r+1][c], board[r+2][c], board[r+3][c]]
			if(window.count(1) == 4):
				set_game_over(0)
				return
			elif(window.count(2) == 4):
				set_game_over(1)
				return

	#positive slope diagonal
	for r in range(ROW_LENGTH-3, ROW_LENGTH, 1):
		for c in range(COLUMN_LENGTH-3):
			window = [board[r][c], board[r-1][c+1], board[r-2][c+2], board[r-3][c+3]]
			if window.count(1) == 4:
				set_game_over(0)
				return
			elif window.count(2) == 4:
				set_game_over(1)
				return

	#negative slope diagonal
	for r in range(ROW_LENGTH-3):
		for c in range(COLUMN_LENGTH-3):
			window = [board[r][c], board[r+1][c+1], board[r+2][c+2], board[r+3][c+3]]
			if window.count(1) == 4:
				set_game_over(0)
				return
			elif window.count(2) == 4:
				set_game_over(1)
				return

def draw_board():
	for c in range(COLUMN_LENGTH):
		for r in range(ROW_LENGTH):
			xcoor = c*SQUARESIZE
			ycoor = (r*SQUARESIZE)+SQUARESIZE
			xcc = xcoor + int(SQUARESIZE/2)
			ycc = ycoor + int(SQUARESIZE/2)
			pygame.draw.rect(screen, BLUE, pygame.Rect((xcoor, ycoor), (SQUARESIZE, SQUARESIZE)))			
			pygame.draw.circle(screen, BLACK, (xcc, ycc), int(SQUARESIZE/2.5))



#MAIN FUNCTION
ROW_LENGTH = 6
COLUMN_LENGTH = 7

#before the game
board = create_board()
winner = random.randint(0,2)
game_over = False
turn = who_goes_first()

pygame.init()

SQUARESIZE = 100
width = COLUMN_LENGTH * SQUARESIZE
height = (ROW_LENGTH + 1) * SQUARESIZE

size = (width, height)

screen = pygame.display.set_mode(size)
draw_board()
pygame.display.update()

print ("This is the starting board. A clean slate.")
print(board)

pdb.set_trace()

# #game portion
# while not game_over:
# 	if turn == 0:
# 		player_0_input = get_user_input (0)
# 		modify_board (player_0_input, 1)
# 		print ("This is the new board")
# 		print(board)
# 		is_game_over()
# 		turn = 1
# 	elif turn == 1:
# 		player_1_input = get_user_input (1)
# 		modify_board (player_1_input, 2)
# 		print ("This is the new board")
# 		print(board)
# 		is_game_over()
# 		turn = 0

# #once the game is complete
# print("The game is over now. Congratulations to player " + str(winner) + " Thanks for playing.")