import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Khởi tạo màn hình
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Ping Pong')

# Khởi tạo màu sắc
white = (255, 255, 255)
black = (0, 0, 0)

# Tạo biến tọa độ của thanh trượt người chơi và máy tính
player_paddle_x = 20
player_paddle_y = height // 2
computer_paddle_x = width - 30
computer_paddle_y = height // 2

# Tạo biến tọa độ và tốc độ di chuyển của bóng
ball_x = width // 2
ball_y = height // 2
ball_dx = random.choice([-2, 2])
ball_dy = random.choice([-2, 2])

# Tạo biến điểm số
score_player = 0
score_computer = 0

fps = 120
clock = pygame.time.Clock()

# Hàm vẽ thanh trượt người chơi và máy tính
def draw_paddles():
    pygame.draw.rect(screen, white, [player_paddle_x, player_paddle_y, 10, 80])
    pygame.draw.rect(screen, white, [computer_paddle_x, computer_paddle_y, 10, 80])

# Hàm vẽ bóng
def draw_ball():
    pygame.draw.circle(screen, white, (ball_x, ball_y), 10)

# Hàm hiển thị điểm số
def display_scores():
    display_message('Player: ' + str(score_player), 10, 10, white, 30)
    display_message('Computer: ' + str(score_computer), width - 150, 10, white, 30)

# Hàm hiển thị chữ lên màn hình
def display_message(text, x, y, color, font_size):
    font = pygame.font.SysFont('Arial', font_size)
    screen_text = font.render(text, True, color)
    screen.blit(screen_text, [x, y])

# Hàm thiết lập lại vị trí ban đầu của bóng
def reset_ball():
    global ball_x, ball_y, ball_dx, ball_dy
    ball_x = width // 2
    ball_y = height // 2
    ball_dx = random.choice([-2, 2])
    ball_dy = random.choice([-2, 2])

# Vòng lặp game
running = True
while running:
	screen.fill(black)
	
	# Kiểm tra sự kiện trong game
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	keys=pygame.key.get_pressed()
	if keys[pygame.K_w]:
		player_paddle_y -= 5
	if keys[pygame.K_s]:
		player_paddle_y += 5
			
	
	# Di chuyển thanh trượt máy tính
	if ball_y < computer_paddle_y and computer_paddle_y > 0:
		computer_paddle_y -= 10
	elif ball_y > computer_paddle_y + 80 and computer_paddle_y < height - 80:
		computer_paddle_y += 10
	
	# Di chuyển bóng
	ball_x += ball_dx
	ball_y += ball_dy
	
	# Kiểm tra va chạm của bóng với thanh trượt người chơi
	if player_paddle_x + 10 >= ball_x >= player_paddle_x and player_paddle_y <= ball_y <= player_paddle_y + 80:
		ball_dx = -ball_dx
	
	# Kiểm tra va chạm của bóng với thanh trượt máy tính
	if computer_paddle_x <= ball_x <= computer_paddle_x + 10 and computer_paddle_y <= ball_y <= computer_paddle_y + 80:
		ball_dx = -ball_dx
	
	# Kiểm tra va chạm của bóng với tường trên và dưới
	if ball_y <= 0 or ball_y >= height:
		ball_dy = -ball_dy
	
	# Kiểm tra va chạm của bóng với tường trái và phải (điểm số)
	if ball_x <= 0:
		score_player += 1
		reset_ball()
	
	if ball_x >= width:
		score_computer += 1
		reset_ball()
	
	# Vẽ thanh trượt và bóng lên màn hình
	draw_paddles()
	draw_ball()
	
	# Hiển thị điểm số
	display_scores()
	clock.tick(fps)
	pygame.display.update()

	# Kết thúc Pygame
pygame.quit()
