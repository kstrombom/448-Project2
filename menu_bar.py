""""
@file: menu_bar.py
@author: Diego Soliz, Shane Chu, Michael Bechtel, Connor Welsh, Dustin Wendt
@date: 2016.02.14
@brief: Menu_bar class. Used to show options menu to the user.
"""

from settings import *
import math
import time
from feed_HMS import *

font = pygame.font.Font("Anita semi square.ttf", 20)
number = font.render("12", 1, BLACK)

######################################################################
############################# PRINT MENU #############################
######################################################################

# print menu options in console
def printMenu_console ():

	print ("Press a for analog clock display")
	print ("Press d for digital clock display")
	print ("press space to change between 24 or 12 hour mode")
	print ("Press s to set time")
	print ("Press m for menu options")
	print ("Press w to toggle through sounds")

# print menu options in display
def printMenu_display ():

	display.fill(PALE_BLUE)
	my_list = ("A for analog clock" , "D for digital clock" , "SPACE for 24/12 hr mode" , "S to set time" , "M for menu options","W to select tick sound")
	for i in range(len(my_list)):
		message = font.render(my_list[i], 1, WHITE)
		display.blit(message, (8, i*45 + 30))
	pygame.display.update()

# draw string given text and position
def draw_string (string_in,x,y):

	time_str = font.render(string_in, 1, WHITE)
	display.blit(time_str, (x, y))
	pygame.display.update()

######################################################################
############################# GET INPUTS #############################
######################################################################

# get time from user
def input_time_menu ():

	display.fill(PALE_BLUE)
	printMenu_display()

	i = 0
	input_time = list("00:00:00")
	while True:
		draw_string("Input Time (00:00:00-23:59:59):",10,6*45 + 30)
		draw_string(''.join(input_time),8,7*45 + 30)
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key in (pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9 ):
					if i <= 8:
						if input_time[i] == ':':
							i += 1
							input_time[i] = str(event.key-48)
							i += 1
						else:
							input_time[i] = str(event.key-48)
							i += 1
						display.fill(PALE_BLUE)
						printMenu_display()
						draw_string(''.join(input_time),8,7*45 + 30)
						print (input_time)
						if i == 8:
							if str_input_time_check(input_time)[0]:
								draw_string("Time Set Successfully!",130,7*45 + 30)
								i = 0
								time.sleep(0.9)
								return (str_input_time_check(input_time)[1])
							else:
								draw_string("Invalid input try again!",130,7*45 + 30)
								time.sleep(1.7)
								i = 0
								display.fill(PALE_BLUE)
								printMenu_display()
								input_time = list("00:00:00")
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

	curr_time += .1
	print("hello")
	time.sleep(0.1)

# get date from user
def input_date_menu ():

	display.fill(PALE_BLUE)
	printMenu_display()

	i = 0
	input_date = list("00/00")
	while True:
		draw_string("Input Date (01/01-12/31):",10,6*45 + 30)
		draw_string(''.join(input_date),8,7*45 + 30)
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key in (pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9 ):
					if i <= 5:
						if input_date[i] == '/':
							i += 1
							input_date[i] = str(event.key-48)
							i += 1
						else:
							input_date[i] = str(event.key-48)
							i += 1
						display.fill(PALE_BLUE)
						printMenu_display()
						draw_string(''.join(input_date),8,7*45 + 30)
						print (input_date)
						if i == 5:
							if str_input_date_check(input_date)[0]:
								draw_string("Date Set Successfully!",130,7*45 + 30)
								i = 0
								time.sleep(0.9)
								return (str_input_date_check(input_date)[1])
							else:
								
								draw_string("Invalid input try again!",130,7*45 + 30)
								time.sleep(1.7)
								i = 0
								display.fill(PALE_BLUE)
								printMenu_display()
								input_date = list("00/00")
			if event.type == QUIT:
				pygame.quit()
				sys.exit()


	curr_time += .1
	print("hello")
	time.sleep(0.1)




