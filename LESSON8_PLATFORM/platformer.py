import pygame
pygame.init()
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platformer')
clock = pygame.time.Clock()
fps = 60
world_data = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1], 
[1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 1], 
[1, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
class World():
	def __init__(self, data):
		self.tile_list = [] #Tạo list chứa các tile
		self.title_size = 40 #Kích thước của tile
		self.sun_img = pygame.image.load('img/sun.png')
		self.bg_img = pygame.image.load('img/sky.png')
		self.dirt_img = pygame.image.load('img/dirt.png')
		self.dirt_img = pygame.transform.scale(self.dirt_img, (self.title_size, self.title_size))
		self.grass_img = pygame.image.load('img/grass.png')
		self.grass_img = pygame.transform.scale(self.grass_img, (self.title_size, self.title_size))
		row_count = 0 #Tạo biến đếm hàng
		for row in data: #Duyệt qua từng hàng
			col_count = 0 #Tạo biến đếm cột
			for tile in row: #Duyệt qua từng cột
				if tile == 1: #Nếu tile là 1
					img = self.dirt_img #Lấy ảnh của dirt
					img_rect = img.get_rect() #Lấy hình chữ nhật của ảnh
					img_rect.x = col_count * self.title_size #Tính toán vị trí x của ảnh
					img_rect.y = row_count * self.title_size #Tính toán vị trí y của ảnh
					tile = (img, img_rect) #Tạo tuple chứa ảnh và hình chữ nhật
					self.tile_list.append(tile) #Thêm tuple vào list
				if tile == 2: #Nếu tile là 2
					img = self.grass_img #Lấy ảnh của grass
					img_rect = img.get_rect() #Lấy hình chữ nhật của ảnh
					img_rect.x = col_count * self.title_size #Tính toán vị trí x của ảnh
					img_rect.y = row_count * self.title_size #Tính toán vị trí y của ảnh
					tile = (img, img_rect) #Tạo tuple chứa ảnh và hình chữ nhật
					self.tile_list.append(tile) #Thêm tuple vào list
				col_count += 1 #Tăng biến đếm cột lên 1
			row_count += 1 #Tăng biến đếm hàng lên 1
	def draw(self):
		screen.blit(self.bg_img, (0, 0)) #Vẽ ảnh nền
		screen.blit(self.sun_img, (120, 120)) #Vẽ ảnh mặt trời
		for tile in self.tile_list: #Duyệt qua từng tile
			screen.blit(tile[0], tile[1]) #Vẽ tile 
			#pygame.draw.rect(screen, (255, 255, 255), tile[1], 2)#Vẽ hình chữ nhật bao quanh tile
class Player():
	def __init__(self, x, y):
		self.images_right = [] #Tạo list chứa ảnh của người chơi đi sang phải
		self.images_left = [] #Tạo list chứa ảnh của người chơi đi sang trái
		self.index = 0 #Tạo biến đếm ảnh
		self.counter = 0 #Tạo biến đếm thời gian
		for num in range(1, 5): #Duyệt qua từng ảnh
			img_right = pygame.image.load(f'img/guy{num}.png') #Lấy ảnh của người chơi đi sang phải
			img_right = pygame.transform.scale(img_right, (40, 80)) #Thay đổi kích thước ảnh
			img_left = pygame.transform.flip(img_right, True, False) #Lấy ảnh của người chơi đi sang trái
			self.images_right.append(img_right) #Thêm ảnh vào list
			self.images_left.append(img_left) #Thêm ảnh vào list
		self.image = self.images_right[self.index] #Lấy ảnh đầu tiên của list
		self.rect = self.image.get_rect() #Lấy hình chữ nhật của ảnh
		self.rect.x = x #Tính toán vị trí x của ảnh
		self.rect.y = y #Tính toán vị trí y của ảnh
		self.width = self.image.get_width() #Lấy chiều rộng của ảnh
		self.height = self.image.get_height() #Lấy chiều cao của ảnh
		self.vel_y = 0 #Tạo biến vận tốc theo chiều y
		self.jumped = False #Tạo biến kiểm tra người chơi có đang nhảy hay không
		self.direction = 0 #Tạo biến kiểm tra người chơi đang đi sang phải hay trái
	def update(self): #Hàm cập nhật
		dx = 0 #Tạo biến độ dời theo chiều x
		dy = 0 #Tạo biến độ dời theo chiều y
		walk_cooldown = 5 #Tạo biến thời gian chờ giữa các bước đi
		key = pygame.key.get_pressed() #Lấy các phím được nhấn
		if key[pygame.K_SPACE] and self.jumped == False: #Nếu phím space được nhấn và người chơi không đang nhảy
			self.vel_y = -15 #Thiết lập vận tốc theo chiều y
			self.jumped = True #Thiết lập người chơi đang nhảy
		if key[pygame.K_SPACE] == False: #Nếu phím space không được nhấn
			self.jumped = False #Thiết lập người chơi không đang nhảy
		if key[pygame.K_LEFT]: #Nếu phím mũi tên trái được nhấn
			dx -= 5 #Thiết lập độ dời theo chiều x
			self.counter += 1 #Tăng biến đếm thời gian lên 1
			self.direction = -1 #Thiết lập người chơi đang đi sang trái
		if key[pygame.K_RIGHT]: #Nếu phím mũi tên phải được nhấn
			dx += 5 #Thiết lập độ dời theo chiều x
			self.counter += 1 #Tăng biến đếm thời gian lên 1
			self.direction = 1 #Thiết lập người chơi đang đi sang phải
		if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False: #Nếu không có phím nào được nhấn
			self.counter = 0 #Thiết lập biến đếm thời gian về 0
			self.index = 0 #Thiết lập biến đếm ảnh về 0
			if self.direction == 1: #Nếu người chơi đang đi sang phải
				self.image = self.images_right[self.index] #Lấy ảnh đầu tiên của list ảnh đi sang phải
			if self.direction == -1: #Nếu người chơi đang đi sang trái
				self.image = self.images_left[self.index] #Lấy ảnh đầu tiên của list ảnh đi sang trái
		if self.counter > walk_cooldown: #Nếu biến đếm thời gian lớn hơn biến thời gian chờ
			self.counter = 0	 #Thiết lập biến đếm thời gian về 0
			self.index += 1 #Tăng biến đếm ảnh lên 1
			if self.index >= len(self.images_right): #Nếu biến đếm ảnh lớn hơn số lượng ảnh trong list
				self.index = 0 #Thiết lập biến đếm ảnh về 0
			if self.direction == 1: #Nếu người chơi đang đi sang phải
				self.image = self.images_right[self.index] #Lấy ảnh theo biến đếm ảnh của list ảnh đi sang phải
			if self.direction == -1: #Nếu người chơi đang đi sang trái
				self.image = self.images_left[self.index] #Lấy ảnh theo biến đếm ảnh của list ảnh đi sang trái
		self.vel_y += 1 #Tăng vận tốc theo chiều y lên 1
		if self.vel_y > 10: #Nếu vận tốc theo chiều y lớn hơn 10
			self.vel_y = 10 #Thiết lập vận tốc theo chiều y về 10
		dy += self.vel_y #Thiết lập độ dời theo chiều y bằng vận tốc theo chiều y
		for tile in world.tile_list: #Duyệt qua các tile trong list tile
			if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):#Kiểm tra va chạm theo chiều x
				dx = 0#Nếu có va chạm thì không cho nhân vật di chuyển theo chiều x
			if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):#Kiểm tra va chạm theo chiều y
				if self.vel_y < 0:#Nếu nhân vật đang rơi
					dy = tile[1].bottom - self.rect.top#Cho dy bằng vị trí của tile dưới nhân vật
					self.vel_y = 0#Không cho nhân vật rơi xuống
				elif self.vel_y >= 0:#Nếu nhân vật đang nhảy
					dy = tile[1].top - self.rect.bottom#Cho dy bằng vị trí của tile trên nhân vật
					self.vel_y = 0#Không cho nhân vật rơi xuống
		self.rect.x += dx #Cập nhật vị trí theo chiều x
		self.rect.y += dy #Cập nhật vị trí theo chiều y
		if self.rect.bottom > screen_height: #Nếu nhân vật rơi xuống đáy màn hình
			self.rect.bottom = screen_height #Thiết lập vị trí của nhân vật ở dưới cùng của màn hình
			dy = 0 #Không cho nhân vật rơi xuống
		screen.blit(self.image, self.rect) #Vẽ nhân vật lên màn hình
player= Player(100, screen_height - 130)
world = World(world_data)
def main():
	run = True
	while run:
		world.draw()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		player.update()
		clock.tick(fps)
		pygame.display.update()
main()