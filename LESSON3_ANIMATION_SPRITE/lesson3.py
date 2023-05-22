import pygame, random
pygame.init()
screen_width = 900
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Animation Sprite")
#Define clock
clock = pygame.time.Clock()
FPS = 27
#Load background
bg = pygame.image.load("images/bg.png")
bg = pygame.transform.scale(bg, (screen_width, screen_height))
bg_x = 0
#Load animation
walk_left=[pygame.image.load("images/L"+str(x)+".png") for x in range(1,10)]
walk_left=[pygame.transform.scale(x,(200,200)) for x in walk_left]
#Flip animation
walk_right=[pygame.transform.flip(x,True,False) for x in walk_left]
#Load animation
player_x=200
player_y=300
vel=5
jump=False
left=False
right=False
walkCount=0
jumpCount=10
#Task3: Load saw animation
### Your code here ###

#Task4: Define x_saw, y_saw, sawCount
### Your code here ###

#Task5: Load spike 
### Your code here ###

#Task6: Define x_spike, y_spike
### Your code here ###

#Draw screen
def redrawWindow():
	#Draw background
	global walkCount,bg_x
	screen.blit(bg,(bg_x,0))
	screen.blit(bg,(bg_x+screen_width,0))
	bg_x-=1
	if bg_x<=-screen_width:
		bg_x=0
	#Draw player
	walkCount+=1
	if walkCount>=26:
		walkCount=0
	if left:
		screen.blit(walk_left[walkCount//3],(player_x,player_y))
		
	#Task1: Draw player when he moves right
	### Your code here ###

	else:
		screen.blit(walk_right[0],(player_x,player_y))
	#Task7: Draw saw and animate it
	### Your code here ###

	#Task8: if position of saw out of screen, random position of saw
	### Your code here ###

	#Task9: Draw spike
	### Your code here ###

	#Task10: if position of spike out of screen, random position of spike
	### Your code here ###

#Task13: Define function show_text (text, x, y, color)
### Your code here ###

while True:
	#Call function redrawWindow
	redrawWindow()
	#Move player left or right
	keys=pygame.key.get_pressed()
	if keys[pygame.K_LEFT] and player_x>0:
		player_x-=vel
		left=True
		right=False

	#Task2: Move player right
	### Your code here ###

	else:
		left=False
		right=False
		walkCount=0
	#Jump
	if not jump:
		if keys[pygame.K_SPACE]:
			jump=True
	else:
		if jumpCount>=-10:
			player_y-=(jumpCount*abs(jumpCount))*0.5
			jumpCount-=1
		else:
			jumpCount=10
			jump=False

	#Task11: Check collision between player and saw
	# If collision, quit game
	### Your code here ###

	#Task12: Check collision between player and spike
	# If collision, quit game
	### Your code here ###	

	#Quit game
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()

	#Task14. Create score variable and show it on screen with function show_text
	### Your code here ###

	#Task15. Call function show_text to show "Game Over" when player die
	### Your code here ###
	
	#Update screen
	clock.tick(FPS)
	pygame.display.update()
pygame.quit()
