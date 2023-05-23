import pygame, random #Thêm thư viện random, pygame
pygame.init() #khởi tao pygame
screen_width = 900 #Đặt kích thước màn hình chiều rộng
screen_height = 600 #Đặt kích thước màn hình chiều cao
screen = pygame.display.set_mode((screen_width, screen_height))#Tạo màn hình
pygame.display.set_caption("Animation Sprite")#Đặt tiêu đề cho màn hình
#Define clock
clock = pygame.time.Clock() #Định nghĩa đồng hồ để đếm fps
FPS = 27 #Đặt fps=27, nghĩa là game sẽ chạy 27 khung hình mỗi giây
#Load background
bg = pygame.image.load("images/bg.png") #Load ảnh background
bg = pygame.transform.scale(bg, (screen_width, screen_height)) #Thay đổi kích thước ảnh background
bg_x = 0 #Đặt tọa độ x của background
#Load animation
walk_left=[pygame.image.load("images/L"+str(x)+".png") for x in range(1,10)] 
#Load 9 ảnh L1.png, L2.png, L3.png, L4.png, L5.png, L6.png, L7.png, L8.png, L9.png
#và tên tên là walk_left
walk_left=[pygame.transform.scale(x,(200,200)) for x in walk_left]
#Thay đổi kích thước 9 ảnh trên thành 200x200
#Flip animation
walk_right=[pygame.transform.flip(x,True,False) for x in walk_left]
#Lật ngược 9 ảnh trên theo chiều ngang, tạo thành 9 ảnh walk_right
#flip(x, True, False),x là ảnh cần lật, True là lật theo chiều ngang, False là không lật theo chiều dọc
#Load animation
player_x=200 #Đặt tọa độ x của player
player_y=300 #Đặt tọa độ y của player
vel=5 #Đặt vận tốc của player khi di chuyển,5 pixel mỗi lần di chuyển
jump=False #Đặt biến jump=False, nghĩa là player chưa nhảy
left=False #Đặt biến left=False, nghĩa là player chưa di chuyển sang trái
right=False #Đặt biến right=False, nghĩa là player chưa di chuyển sang phải
walkCount=0 #Đặt biến walkCount=0, nghĩa là đếm số frame của animation
jumpCount=10 #Đặt biến jumpCount=10, nghĩa là đếm số frame của animation khi nhảy
#Task3: Load saw animation
### Your code here ###

#Task4: Define x_saw, y_saw, sawCount=0
### Your code here ###

#Task5: Load spike 
### Your code here ###

#Task6: Define x_spike, y_spike
### Your code here ###

#Draw screen
def redrawWindow():
	#Draw background
	global walkCount,bg_x #Khai báo biến toàn cục để sử dụng
	screen.blit(bg,(bg_x,0)) #Vẽ background
	screen.blit(bg,(bg_x+screen_width,0)) #Vẽ background
	bg_x-=1 #Di chuyển background sang trái 1 pixel
	if bg_x<=-screen_width: #Nếu background di chuyển hết màn hình
		bg_x=0 #Đặt lại background về vị trí ban đầu
	#Draw player
	walkCount+=1 #Biến đếm số frame của animation tăng lên 1
	if walkCount>=26: #Nếu đếm đủ 26 frame
		walkCount=0 #Đặt lại biến đếm về 0
	if left==True: #Nếu player di chuyển sang trái
		screen.blit(walk_left[walkCount//3],(player_x,player_y)) 
		#Vẽ animation player di chuyển sang trái
		# Sau 3 frame thì chuyển sang 1 ảnh khác	
	#Task1: Draw player when he moves right
	elif right==True:
		pass ### Your code here ###

	else: #Nếu player không di chuyển sang trái hoặc phải	
		screen.blit(walk_right[0],(player_x,player_y)) 
	#Player sẽ xoay mặt sang phải
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
	redrawWindow() #Gọi hàm vẽ màn hình để show background, player, saw, spike
	#Move player left or right
	keys=pygame.key.get_pressed() #Lấy phím được nhấn
	if keys[pygame.K_LEFT] and player_x>0: 
	#Nếu nhấn phím mũi tên trái và player chưa đến biên trái
		player_x-=vel #Di chuyển player sang trái
		left=True #Đặt biến left=True, nghĩa là player di chuyển sang trái
		right=False #Đặt biến right=False, nghĩa là player không di chuyển sang phải

	#Task2: Move player right
	elif keys[pygame.K_RIGHT] and player_x<screen_width-200:
		pass	### Your code here ###


	else: #Nếu không nhấn phím mũi tên trái hoặc phải
		left=False #Đặt biến left=False
		right=False #Đặt biến right=False
		walkCount=0 #Đặt biến đếm frame về 0
	#Jump
	if not jump: #Nếu player chưa nhảy
		if keys[pygame.K_SPACE]: #Nếu nhấn phím space
			jump=True #Đặt biến jump=True, nghĩa là player đang nhảy
	else: #Nếu player đang nhảy
		if jumpCount>=-10: #Nếu chưa đạt độ cao nhảy tối đa
			player_y-=(jumpCount*abs(jumpCount))*0.5 #Di chuyển player lên trên
			jumpCount-=1 #Giảm biến đếm frame xuống 1
		else: #Nếu đã đạt độ cao nhảy tối đa
			jumpCount=10 #Đặt biến đếm frame về 10
			jump=False #Đặt biến jump=False, nghĩa là player không nhảy

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
