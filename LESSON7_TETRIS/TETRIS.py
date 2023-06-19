import pygame,random# cài đặt pygame
pygame.init()# khởi tạo pygame
size = (400, 500)# kích thước màn hình
screen = pygame.display.set_mode(size)# khởi tạo màn hình
pygame.display.set_caption("Tetris")# Tạo một đối tượng clock để quản lý tốc độ trò chơi
clock = pygame.time.Clock()
fps = 30
colors = ('gray', 'red', 'green', 'blue', 'cyan', 'yellow', 'orange', 'purple')
# List các hình
I= [[1, 5, 9, 13], [4, 5, 6, 7]]
Z= [[4, 5, 9, 10], [2, 6, 5, 9]]
S= [[6, 7, 9, 10], [1, 5, 6, 10]]
L= [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]]
J= [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]]
T= [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]]
O= [[1, 2, 5, 6]]
figures = [I, Z, S, T, O, L, J]
class Figure:
    def __init__(self, x, y):# Hàm khởi tạo figure
        self.x = x# tọa độ x
        self.y = y# tọa độ y
        self.type = random.randint(0, len(figures) - 1)# random kiểu hình
        self.color = random.randint(1, len(colors) - 1)# random màu
        self.rotation = 0 # 0, 1, 2, 3# Hàm trả về hình ảnh của figure
    def image(self):# Hàm trả về hình ảnh và xoay của figure
        return figures[self.type][self.rotation]
    def rotate(self):# Hàm xoay figure
        self.rotation = (self.rotation + 1) % len(figures[self.type])
class GAME:
    score = 0# Điểm
    state = "start"# Trạng thái
    field = [] # lưới
    x = 100# tọa độ x
    y = 60# tọa độ y
    zoom = 20#kích thước mỗi ô
    figure = None# Khởi tạo figure
    def __init__(self, height, width):# Hàm khởi tạo lưới với tất cả các ô bằng 0
        self.height = height# chiều cao
        self.width = width# chiều rộng
        for i in range(self.height):# Tạo lưới
            new_line = []# Tạo một hàng mới
            for j in range(self.width):# Tạo một cột mới
                new_line.append(0)# Thêm 0 vào hàng mới
            self.field.append(new_line)# Thêm hàng mới vào lưới
    def new_figure(self):# Hàm tạo figure mới
        self.figure = Figure(3, 0)# Tạo figure mới
    def show_figure(self):# Hàm hiển thị figure
        for i in range(4):# Duyệt hàng
            for j in range(4):# Duyệt cột
                if i * 4 + j in self.figure.image():# Nếu ô đang xét có trong hình ảnh của figure
                    pygame.draw.rect(screen, colors[self.figure.color], (self.x + (j + self.figure.x) * self.zoom, self.y + (i + self.figure.y) * self.zoom, self.zoom, self.zoom), 0)
    def go_down(self):# Hàm di chuyển figure xuống dưới
        self.figure.y += 1# Tăng tọa độ y của figure
        if self.intersects():# Nếu figure va chạm
            self.figure.y -= 1# Trả lại tọa độ y của figure
            self.freeze()# Đóng băng figure
    def go_side(self, dx):# Hàm di chuyển figure sang trái hoặc sang phải
        old_x = self.figure.x# Lưu lại tọa độ x của figure
        self.figure.x += dx# Tăng hoặc giảm tọa độ x của figure
        if self.intersects():# Nếu figure va chạm
            self.figure.x = old_x# Trả lại tọa độ x của figure
    def rotate(self):# Hàm xoay figure
        old_rotation = self.figure.rotation# Lưu lại góc xoay của figure
        self.figure.rotate()# Xoay figure
        if self.intersects():# Nếu figure va chạm
            self.figure.rotation = old_rotation  # Trả lại góc xoay của figure
    def go_space(self):# Hàm di chuyển figure xuống dưới cùng
        while not self.intersects():# Nếu figure không va chạm
            self.figure.y += 1# Tăng tọa độ y của figure
        self.figure.y -= 1# Trả lại tọa độ y của figure
        self.freeze()  # Đóng băng figure
    def intersects(self):# Hàm kiểm tra va chạm
        intersection = False# Khởi tạo biến kiểm tra va chạm
        for i in range(4):# Duyệt hàng
            for j in range(4):# Duyệt cột
                if i * 4 + j in self.figure.image():# Nếu ô đang xét có trong hình ảnh của figure
                    if i + self.figure.y > self.height - 1 or \
                            j + self.figure.x > self.width - 1 or \
                            j + self.figure.x < 0 or \
                            self.field[i + self.figure.y][j + self.figure.x] > 0:
                        intersection = True# Trả về kết quả
        return intersection# Trả về kết quả
    def freeze(self):# Hàm đóng băng figure
        for i in range(4):# Duyệt hàng
            for j in range(4):# Duyệt cột
                if i * 4 + j in self.figure.image():# Nếu ô đang xét có trong hình ảnh của figure
                    self.field[i + self.figure.y][j + self.figure.x] = self.figure.color# Đóng băng figure
        self.break_lines()# Xóa các hàng đã đầy
        self.new_figure()# Tạo figure mới
        if self.intersects():# Nếu figure va chạm
            game.state = "gameover"# Trạng thái gameover
    def break_lines(self):# Hàm xóa các hàng đã đầy
        lines = 0# Khởi tạo biến đếm số hàng đã xóa
        for i in range(1, self.height):# Duyệt hàng
            zeros = 0# Khởi tạo biến đếm số ô trống
            for j in range(self.width):# Duyệt cột
                if self.field[i][j] == 0:# Nếu ô đang xét trống
                    zeros += 1# Tăng biến đếm
            if zeros == 0:# Nếu hàng đang xét đã đầy
                lines += 1# Tăng biến đếm
                for i1 in range(i, 1, -1):# Duyệt hàng
                    for j in range(self.width):# Duyệt cột
                        self.field[i1][j] = self.field[i1 - 1][j]# Di chuyển hàng trên xuống hàng dưới
        self.score += lines ** 2# Cộng điểm
    def display_message(self, message,x,y):# Hàm hiển thị thông báo
        font=pygame.font.Font('freesansbold.ttf', 30)# Khởi tạo font chữ
        text=font.render(message, True, (255, 255, 255), (0, 0, 0))# Khởi tạo thông báo
        screen.blit(text, (x, y))# Hiển thị thông báo
game = GAME(20, 10)# Khởi tạo game với kích thước 20 hàng và 10 cột
counter = 0# Khởi tạo biến đếm
pressing_down = False# Khởi tạo biến kiểm tra phím xuống
gameloop=True# Khởi tạo biến kiểm tra game
while gameloop:
    screen.fill('white')# Đặt màu nền
    for i in range(game.height):# Duyệt hàng
        for j in range(game.width):# Duyệt cột
            pygame.draw.rect(screen, 'black', [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
            if game.field[i][j] > 0:
                pygame.draw.rect(screen, colors[game.field[i][j]],
                                 [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom])
    if game.figure is None:# Nếu figure không tồn tại
        game.new_figure()# Tạo figure mới
    game.show_figure()# Hiển thị figure
    counter += 5# Tốc độ di chuyển figure
    if counter > 100000:# Đặt lại tốc độ di chuyển figure
        counter = 0# Đặt lại tốc độ di chuyển figure
    if counter % fps== 0 or pressing_down:# Nếu đủ tốc độ di chuyển figure
        if game.state == "start":# Nếu trạng thái là start
            game.go_down()# Di chuyển figure xuống
    for event in pygame.event.get():# Lấy sự kiện
        if event.type == pygame.QUIT:# Nếu sự kiện là thoát
            gameloop=False# Thoát game
        if event.type == pygame.KEYDOWN:# Nếu sự kiện là nhấn phím
            if event.key == pygame.K_UP:# Nếu phím là mũi tên lên
                game.rotate()# Xoay figure
            if event.key == pygame.K_DOWN:# Nếu phím là mũi tên xuống
                pressing_down = True# Đặt biến kiểm tra phím xuống
            if event.key == pygame.K_LEFT:# Nếu phím là mũi tên trái
                game.go_side(-1)# Di chuyển figure sang trái
            if event.key == pygame.K_RIGHT:# Nếu phím là mũi tên phải
                game.go_side(1)# Di chuyển figure sang phải
            if event.key == pygame.K_SPACE:# Nếu phím là phím cách
                game.go_space()# Di chuyển figure xuống đến khi va chạm
            if event.key == pygame.K_r:# Nếu phím là phím R
                game.state = "start"# Đặt trạng thái là start
                game.score = 0# Đặt điểm là 0
                for i in range(game.height):# Duyệt hàng
                    for j in range(game.width):# Duyệt cột
                        game.field[i][j] = 0# Đặt ô trống
        if event.type == pygame.KEYUP:# Nếu sự kiện là nhả phím
            if event.key == pygame.K_DOWN:# Nếu phím là mũi tên xuống
                pressing_down = False# Đặt biến kiểm tra phím xuống
    game.display_message("Score: " + str(game.score), 10, 10)# Hiển thị điểm
    if game.state == "gameover":# Nếu trạng thái là gameover
        game.display_message("GAME OVER", 100, 100)# Hiển thị thông báo gameover
        game.display_message("Press R to restart", 70, 130)# Hiển thị thông báo nhấn R để chơi lại
    pygame.display.flip()# Cập nhật màn hình
    clock.tick(fps)# Đặt tốc độ game

