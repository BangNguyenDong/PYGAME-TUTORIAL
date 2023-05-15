import pygame,random
pygame.init()

#Create screen
screen_width=500
screen_height=700
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Racing Game")

#Load background
bg=pygame.image.load("bg.jpg").convert_alpha()
bg=pygame.transform.scale(bg,(screen_width,screen_height))
bg_y=0

#Load player
player=pygame.image.load("player.png").convert_alpha()
player=pygame.transform.scale(player,(100,200))
player=pygame.transform.rotate(player,180)
player_x=screen_width/2-50
player_y=screen_height-200

#Load enemy
enemy=pygame.image.load("enemy.png").convert_alpha()
enemy=pygame.transform.scale(enemy,(100,200))
enemy_x=random.randrange(100,screen_width-100,100)
enemy_y=random.randrange(-500,-100,100)

run=True
FPS=60
clock=pygame.time.Clock()
score=0
#Function create text
def display_message(text,size,color,x,y):
	font=pygame.font.SysFont("arial",size)#font and size
	text=font.render(text,True,color)#render text
	screen.blit(text,(x,y))#show text

#Loop game
while run: 
	#Show background
	screen.blit(bg,(0,bg_y))
	screen.blit(bg,(0,bg_y-screen_height))
	#Move background
	bg_y+=10
	if bg_y>=screen_height:
		bg_y=0

	#Show player
	screen.blit(player,(player_x,player_y))
	#Show enemy
	screen.blit(enemy,(enemy_x,enemy_y))
	enemy_y+=10
	#Move enemy
	if enemy_y>=screen_height:
		enemy_x=random.randrange(100,screen_width-100,100)
		enemy_y=random.randrange(-500,-100,100)

	#Create rect
	player_rect=pygame.Rect(player_x,player_y,100,200) 
	enemy_rect=pygame.Rect(enemy_x,enemy_y,100,200)

	#Check collision
	if player_rect.colliderect(enemy_rect):
		display_message("Game Over",100,(255,0,0),screen_width/2-250,screen_height/2-50)
		pygame.time.delay(2000)
		run=False
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False

		#Move player
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_LEFT and player_x>100:
				player_x-=100
			if event.key==pygame.K_RIGHT and player_x<screen_width-200:
				player_x+=100

	#Show score
	score+=1 
	display_message("Score: "+str(score),30,(255,255,255),10,10)
	#Task1. If score > 1000, show "You win", delay 2s and exit game

	#Task2. Add enemy_1.png and random enemy in game

	'''Task3.Make the player's life 3, if you touch the enemy, reduce the number of lives, 
	if the number of lives goes to 0 then show the game over, wait 2s and exit the game
	'''

	clock.tick(FPS)
	pygame.display.update()
