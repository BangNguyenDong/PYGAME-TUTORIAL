import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Khởi tạo màn hình
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Khởi tạo màu sắc
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

#Task7: Load ảnh apple.png scale về kích thước 40x40
### YOUR CODE HERE ###

#Task8: Load ảnh background.jpg scale về kích thước 800x800
### YOUR CODE HERE ###

# Khởi tạo FPS
FPS = 30
clock = pygame.time.Clock()

# Khởi tạo biến tọa độ x, y và biến tốc độ dx, dy của rắn
x, y = 200, 200
dx, dy = 0, 0
# Khởi tạo list chứa tọa độ x, y của các khối thân rắn
body_list = [[x, y]]


# Khởi tạo tọa độ x, y của thức ăn
food_x, food_y = random.randint(0, width - 40), random.randint(0, height - 40)

# Hàm vẽ tất cả nhân vật lên màn hình
def draw_window():
	# Khai báo biến toàn cục để sử dụng trong hàm
	global x, y, dx, dy, food_x, food_y, body_list

	#Task9: Vẽ background lên màn hình thay cho màu nền
	# Vẽ màu nền
	### YOUR CODE HERE ###
	screen.fill(black)
	#Cập nhật tọa độ x, y của rắn
	x += dx
	y += dy
	#Thêm tọa độ x, y vào list body_list
	body_list.append([x, y])
	#Vẽ các khối thân rắn
	for i, j in body_list:
		pygame.draw.rect(screen, red, [i, j, 40, 40])

	#Task10: Vẽ thức ăn lên màn hình thay cho hình chữ nhật màu trắng
	### YOUR CODE HERE ###

	#Vẽ thức ăn
	pygame.draw.rect(screen, white, [food_x, food_y, 40, 40])
	#Tạo hình chữ nhật chứa rắn và thức ăn
	food_rect = pygame.Rect(food_x, food_y, 40, 40)
	snake_rect = pygame.Rect(x, y, 40, 40)
	#Kiểm tra va chạm giữa rắn và thức ăn

	#Task4: Tạo điểm số và hiển thị lên màn hình

	if food_rect.colliderect(snake_rect):
		#Tạo thức ăn mới
		food_x, food_y = random.randint(0, width - 40), random.randint(0, height - 40)
		#Thêm tọa độ x, y vào list body_list
		body_list.append([x, y])
		#Vẽ thức ăn
		pygame.draw.rect(screen, white, [food_x, food_y, 40, 40])
	#Xóa tọa độ x, y của khối thân rắn đầu tiên để tạo hiệu ứng di chuyển
	else:
		#Xóa tọa độ x, y của khối thân rắn đầu tiên
		body_list.pop(0)

	#Task2: Kiểm tra va chạm giữa rắn và tường gọi hàm game_over()
	### YOUR CODE HERE ###

# Hàm kết thúc game                        
def game_over():
	print('Game Over')

	#Task5: Hiển thị chữ Game Over lên màn hình
	### YOUR CODE HERE ###

	#Vòng lặp game over
	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			if event.type == pygame.KEYDOWN:
				#restart game
				if event.key == pygame.K_SPACE:
					print('Restart Game')
					global x, y, dx, dy, food_x, food_y, body_list
					x, y = 200, 200
					dx, dy = 0, 0
					body_list = [[x, y]]
					food_x, food_y = random.randint(0, width - 40), random.randint(0, height - 40)
					return
		#Cập nhật lại màn hình
		clock.tick(FPS)
		pygame.display.update()

		#Task6: Thay sự kiện nhấn phím bằng sự kiện nhấn nút chuột để restart game

#Task3. Tạo hàm vẽ chữ và điểm số
### YOUR CODE HERE ###

# Vòng lặp game
while True:
	#Gọi hàm vẽ tất cả nhân vật lên màn hình
	draw_window()
	#Kiểm tra sự kiện trong game
	for event in pygame.event.get():
		#Kiểm tra sự kiện nhấn nút thoát
		if event.type == pygame.QUIT:
			quit()
		#Kiểm tra sự kiện nhấn phím
		if event.type == pygame.KEYDOWN:
			#Kiểm tra sự kiện nhấn phím mũi tên và hướng di chuyển của rắn
			if event.key == pygame.K_LEFT and dx != 5:
				dx = -5
				dy = 0

			#Task1: Di chuyển theo các hướng còn lại

			#Kiểm tra sự kiện nhấn phím mũi tên và hướng di chuyển của rắn
			elif event.key == pygame.K_RIGHT and dx != -5:
				### YOUR CODE HERE ###
				pass
			#Kiểm tra sự kiện nhấn phím mũi tên và hướng di chuyển của rắn
			elif event.key == pygame.K_UP and dy != 5:
				### YOUR CODE HERE ###
				pass
			#Kiểm tra sự kiện nhấn phím mũi tên và hướng di chuyển của rắn
			elif event.key == pygame.K_DOWN and dy != -5:
				### YOUR CODE HERE ###
				pass

	#Cập nhật lại màn hình
	clock.tick(FPS)
	pygame.display.update()
