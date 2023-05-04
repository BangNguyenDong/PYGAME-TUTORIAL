#Full course pygame
#1. Creating a window
#2. Drawing objects
#3. Moving objects
import pygame #importing pygame module
pygame.init() #initializing pygame
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height)) #creating a window
pygame.display.set_caption("My first game") #setting a caption for the window
pygame.display.set_icon(pygame.image.load("icon.png")) #setting an icon for the window
#icon from https://www.flaticon.com/free-icon
#Color: Hex, RGB, name
#RGB: 0-255
#Hex: 0x000000 - 0xFFFFFF
#Name: "black", "white", "red", "green", "blue"
#Colors: https://www.w3schools.com/colors/colors_names.asp
#Colors: https://www.rapidtables.com/web/color/RGB_Color.html
background=pygame.image.load("background.jpg") #loading the background image
background=pygame.transform.scale(background, (screen_width, screen_height)) #scaling the background image

player=pygame.image.load("player.png").convert_alpha() #loading the player image
player=pygame.transform.scale(player, (50, 50)) #scaling the player image
#player=pygame.transform.rotate(player, 90) #rotating the player image
player_x=250 #player x coordinate
player_y=400 #player y coordinate

run=True #variable to control the main loop
while run: #main loop
	screen.fill((0,0,0)) #filling the screen with black color
	screen.blit(background, (0,0)) #drawing the background image
	#screen.blit(image, (x,y))
	#drawing objects
	#drawing a rectangle
	pygame.draw.rect(screen, (255,0,0), (0,0,50,50), 2) #drawing a red rectangle
	#pygame.draw.rect(screen, color, (x,y,width,height), thickness)
	#drawing a circle
	pygame.draw.circle(screen, (0,255,0), (100,100), 50, 1) #drawing a green circle
	#pygame.draw.circle(screen, color, (x,y), radius, thickness)
	#drawing a line
	pygame.draw.line(screen, (0,0,255), (0,0), (screen_width, screen_height)) #drawing a blue line
	#pygame.draw.line(screen, color, (x1,y1), (x2,y2))
	#drawing a polygon
	pygame.draw.polygon(screen, (255,255,0), ((0,0), (50,0), (50,50), (0,50))) #drawing a yellow polygon
	#pygame.draw.polygon(screen, color, ((x1,y1), (x2,y2), (x3,y3), (x4,y4)))
	#drawing an ellipse
	pygame.draw.ellipse(screen, (255,0,255), (0,0,50,100)) #drawing a pink ellipse
	#pygame.draw.ellipse(screen, color, (x,y,width,height))
	#drawing an arc
	pygame.draw.arc(screen, (0,255,255), (0,0,50,50), 0, 3.14) #drawing a cyan arc
	#pygame.draw.arc(screen, color, (x,y,width,height), start_angle, end_angle)
	#drawing a text
	font=pygame.font.SysFont("comicsans", 30, True) #creating a font
	text=font.render("Game Over", 1, (255,255,255)) #creating a text
	screen.blit(text, (250,250)) #drawing a text
	
	#Task1. Draw picture1.png

	#Moving objects
	screen.blit(player, (player_x, player_y)) #drawing the player image

	for event in pygame.event.get(): #getting all events
		if event.type == pygame.QUIT: #if the event is quit
			run=False #stop the loop
		#Moving objects with keys
		if event.type == pygame.KEYDOWN: #if a key is pressed
			if event.key == pygame.K_LEFT: #if the key is left arrow
				player_x-=5 #move the player to the left
			if event.key == pygame.K_RIGHT: #if the key is right arrow
				player_x+=5 #move the player to the right
			if event.key == pygame.K_UP: #if the key is up arrow
				player_y-=5 #move the player up
			if event.key == pygame.K_DOWN: #if the key is down arrow
				player_y+=5 #move the player down
		# #Moving objects with mouse motion
		if event.type == pygame.MOUSEMOTION: #if a mouse is moved
			player_x, player_y = event.pos #move the player to the mouse position
	
	#Task2. add boy.png on the screen and move it with keys or mouse motion
	pygame.display.update() #updating the screen
pygame.quit() #quitting pygame

