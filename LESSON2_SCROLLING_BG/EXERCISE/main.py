import pygame, random
pygame.init()
screen_width = 300
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")
bg=pygame.image.load("bg.png")
bg=pygame.transform.scale(bg,(screen_width,screen_height))
FPS = 60
gravity = 1
bird_movement = 0
run=True
score = 0
clock = pygame.time.Clock()
player=pygame.image.load("player.png")
player=pygame.transform.scale(player,(30,30))
player_y = 150
#Task1. Thêm base.png vào game

#Task4. Thêm ống nước vào game

while True:
	screen.blit(bg,(0,0))
	#Task2. Cho base dịch chuyển liên tục sang trái

	screen.blit(player,(50,player_y))
	player_y += gravity

	#Task5. Cho ống nước di chuyển sang trái

	#Task6. Kiểm tra va chạm giữa chim và ống nước, nếu có va chạm thì kết thúc game

	#Task7. Kiểm tra va chạm giữa chim và base, nếu có va chạm thì kết thúc game

	#Task8. Công 1 điểm khi có ống nước sang trái và hiên điểm

	#Task9. Hiển thị điểm lên màn hình

	#Task10. Hiển thị game over khi kết thúc game
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			run=False
		#Task3. Thêm sự kiện nhấn phím UP để cho chim bay lên

	pygame.display.update()
	clock.tick(FPS)
pygame.quit()