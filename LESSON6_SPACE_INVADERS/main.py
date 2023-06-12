import pygame
import random

#Define window size
WIDTH = 480
HEIGHT = 600
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")
clock = pygame.time.Clock()

# Define player properties
player_rect = pygame.Rect(200, 450, 50, 40)
player_speedx = 0

# Define bullet properties
bullet_image = pygame.Surface((10, 20))#Tạo hình ảnh đạn có kích thước 10x20
bullet_image.fill(YELLOW)# Tô màu cho đạn
bullet_speedy = -10#Tốc độ di chuyển của đạn
bullets = []#Danh sách đạn

#Define font
start_font = pygame.font.Font(None, 36)
start_text = start_font.render("Click Start to Play", True, WHITE)
start_text_rect = start_text.get_rect(center=(WIDTH/2, HEIGHT/2))

###Task1: Tạo hình ảnh cho player thành player.png
###YOUR CODE HERE

###Task2: Đổi chữ "Click Start to Play" thành "Press SPACE to Play"
###YOUR CODE HERE

###Task4: Khởi tạo âm thanh bullet.wav
###YOUR CODE HERE

###Task6: Khởi tạo vật thể enemy.png gồm x, y, width, height
###YOUR CODE HERE

#Define hàm bắn đạn
def shoot(x, y):
    bullet_rect = bullet_image.get_rect() #Lấy hình chữ nhật bao quanh đạn
    bullet_rect.bottom = y #Đặt đạn ở vị trí y
    bullet_rect.centerx = x #Đặt đạn ở vị trí x
    bullet_speedy = -10 #Tốc độ di chuyển của đạn
    bullets.append(bullet_rect) #Thêm đạn vào danh sách đạn

#Define hàm bắt đầu game
def show_start_screen():
    screen.fill(BLACK)
    screen.blit(start_text, start_text_rect)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
			###Task3: Thêm sự kiện nhấn phím SPACE để bắt đầu game
			###YOUR CODE HERE
            elif event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False
                game_loop()
		
#Define hàm vòng lặp game
def game_loop():
	while True:
		#Vẽ màn hình
		screen.fill(BLACK)
		#Vòng lặp sự kiện
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE: #Nếu nhấn phím SPACE
					shoot(player_rect.centerx, player_rect.top) #Bắn đạn

					###Task5: Khi nhấn phím SPACE thì phát ra âm thanh bullet.wav
					###YOUR CODE HERE
		#Lấy input từ bàn phím
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			player_speedx = -8
		elif keys[pygame.K_RIGHT]:
			player_speedx = 8
		else:
			player_speedx = 0
		player_rect.x += player_speedx
		#Cố định player trong màn hình
		if player_rect.right > WIDTH:
			player_rect.right = WIDTH
		if player_rect.left < 0:
			player_rect.left = 0
		#Bắn đạn
		hits = [] #Danh sách đạn cần xóa
		for bullet_rect in bullets: #Duyệt qua danh sách đạn
			bullet_rect.y += bullet_speedy #Di chuyển đạn
			if bullet_rect.bottom < 0: #Nếu đạn bay ra khỏi màn hình
				hits.append(bullet_rect) #Thêm đạn vào danh sách cần xóa
		for hit in hits: #Duyệt qua danh sách đạn cần xóa
			bullets.remove(hit) #Xóa đạn khỏi danh sách đạn

		#Vẽ viên đạn
		for bullet_rect in bullets:#Duyệt qua danh sách đạn
			pygame.draw.rect(screen, YELLOW, bullet_rect)#Vẽ đạn
		#Vẽ player
		pygame.draw.rect(screen, GREEN, player_rect)

		###Task7: Vẽ enemy.png
		###YOUR CODE HERE

		###Task8: Cho enemy.png xuất hiện ngẫu nhiên trên màn hình theo chiều ngang và đi xuống
		###YOUR CODE HERE

		###Task9: Nếu enemy.png chạm vào player thì hiển thị màn hình kết thúc game
		###YOUR CODE HERE

		###Task10: Tạo điểm số, nếu enemy.png bị bắn trúng thì cộng 1 điểm và hiển thị điểm số lên màn hình, cho enemy.png biến mất
		###YOUR CODE HERE
		pygame.display.update()
		clock.tick(FPS)
#Gọi hàm bắt đầu game
show_start_screen()

