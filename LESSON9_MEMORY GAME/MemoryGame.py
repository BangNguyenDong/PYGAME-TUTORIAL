#import thư viện
import pygame,sys
import time
import random
#Khởi tạo module cho game
pygame.init()
#Khai báo chiều rộng  và chiều cao của màn hình
display_width = 800
display_height = 700

# Khởi tạo màu sắc
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)

# Khởi tạo âm nhạc
pygame.mixer.music.load('Bionic Commando (2009) - 18 - Piano Theme.mp3')#Mở âm thanh
pygame.mixer.music.set_volume(0.1) #Âm lượng
pygame.mixer.music.play(-1) #Chạy vô hạn, -1 là vô hạn
 
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Picture Puzzle Game')
clock = pygame.time.Clock()

# Khởi tạo background
background = pygame.image.load('small_irregular_cubes-wallpaper-1366x768.jpg')
backgroundGameLoop = pygame.image.load('light_green_2-wallpaper-1366x768.jpg')

# Khởi tạo ảnh trong game cấp 1
spring = pygame.image.load('Seasons-Spring.jpg')
winter = pygame.image.load('Seasons-Winter.jpg')
fall = pygame.image.load('Seasons-Fall.jpg')
summer = pygame.image.load('Seasons-Summer.jpg')

# Khởi tạo ảnh trong game cấp 2

# Khởi tạo icon và caption trong game
gameIcon = pygame.image.load('teky.png')
pygame.display.set_icon(gameIcon)

# Hàm thoát game
def quitgame():
        pygame.quit()#Tắt cửa sổ
        sys.exit()#Thoát chương trình
#Hàm button trong game
def button(msg,x,y,w,h,ib_c,ab_c,it_c,at_c,action=None):
    pos = pygame.mouse.get_pos()#Lấy tọa độ chuột
    click = pygame.mouse.get_pressed()#Lấy trạng thái của chuột
    if x+w > pos[0] > x and y+h > pos[1] > y:#Nếu tọa độ chuột nằm trong khoảng x,y,w,h
        pygame.draw.rect(gameDisplay, ab_c,(x,y,w,h))#Vẽ hình chữ nhật màu ab_c
        text(msg,x+(w/2),y+(h/2),50,at_c,'LittleLordFontleroyNF.ttf')#Vẽ text màu at_c
        if click[0] == 1 and action != None:#Nếu click chuột và action != None
            action()#Thực hiện action         
    else:#Nếu tọa độ chuột không nằm trong khoảng x,y,w,h
        pygame.draw.rect(gameDisplay, ib_c,(x,y,w,h))#Vẽ hình chữ nhật màu ib_c
        text(msg,x+(w/2),y+(h/2),50,it_c,'LittleLordFontleroyNF.ttf')# Hàm game_intro trong menu
def text(msg, x, y, size, color, font, sysfont = False):#Hàm text trong game
    if sysfont:#Nếu sysfont = True
        font = pygame.font.SysFont(font,size)#Khai báo font
    else: font = pygame.font.Font(font,size)#Khai báo font
    TextSurf = font.render(msg, True, color)#Vẽ text
    TextRect = TextSurf.get_rect()#Lấy kích thước của text
    TextRect.center = ((x),(y))# Tọa độ text
    gameDisplay.blit(TextSurf, TextRect)# Hàm game_intro trong menu
def about():# Hàm About trong menu
    intro = True#Khởi tạo intro = True
    while intro:#Vòng lặp cho intro = True
        for event in pygame.event.get():#Lặp vòng lặp cho event
            if event.type == pygame.QUIT:#Nếu bấm nút X
                pygame.quit()#Tắt cửa sổ
                sys.exit()#Thoát chương trình
        gameDisplay.blit(background, (00,00))#Vẽ background
        text('References:',display_width/2,display_height/1.25,15,white,'coolvetica rg.ttf')#Vẽ text
        text('--------',display_width/2,display_height/1.2,15,white,'coolvetica rg.ttf')#Vẽ text
        button("Back",(display_width/2)-100,(display_height/2)-50,200,100,white,red,red,white,game_intro)#Vẽ button
        pygame.display.update()#Cập nhật màn hình
        clock.tick(15)#Tạo 15 fps
def game_intro():#Hàm intro trong menu    
    pygame.mixer.music.pause()#Dừng bản nhạc
    intro = True#Khởi tạo intro = True
    while intro:#Vòng lặp cho intro = True
        for event in pygame.event.get():#Lặp vòng lặp cho event
            if event.type == pygame.QUIT:#Nếu bấm nút X
                pygame.quit()#Tắt cửa sổ
                sys.exit()#Thoát chương trình
        gameDisplay.blit(background, (00,00))#Vẽ background
        text('Picture Puzzle Game',display_width/2,display_height/7,50,red,'crackman.ttf')#Vẽ text
        text('----------',display_width/2,display_height/5,25,white,'coolvetica rg.ttf')#Vẽ text
        button("Start Game",(display_width/2)-100,200,200,100,white,red,red,white,game_loop)#Vẽ button
        button("About",(display_width/2)-100,325,200,100,white,red,red,white,about)#Vẽ button
        button("Quit",(display_width/2)-100,450,200,100,white,red,red,white,quitgame)#Vẽ button
        pygame.display.update()#Cập nhật màn hình
        clock.tick(15)#Tạo 15 fps
def check_same(tile, choosen):#Kiểm tra các hình có giống nhau hay không
    l = []#Khởi tạo list l rỗng để lưu các hình giống nhau
    for i in range(len(tile)):#Lặp vòng lặp cho i trong khoảng từ 0 đến len(tile)
            if tile[i] == True:#Nếu tile[i] = True
                l.append(choosen[i])#Thêm choosen[i] vào list l
    if len(l) == 2:#Nếu list l có 2 phần tử
        return len(list(set(l))) != len(l)#Trả về True nếu list l có 2 phần tử khác nhau
    if len(l) == 4:#Nếu list l có 4 phần tử
        return len(list(set(l))) != len(l) - 1#Trả về True nếu list l có 4 phần tử khác nhau
    elif len(l) == 6:#Nếu list l có 6 phần tử
        return len(list(set(l))) != len(l) - 2#Trả về True nếu list l có 6 phần tử khác nhau
    else:#Nếu list l có 8 phần tử
        return len(list(set(l))) != len(l) - 3#Trả về True nếu list l có 8 phần tử khác nhau
def l_random(level = 1):#Tạo ra các hình ảnh ngẫu nhiên
    # 3 x 2
    # 4 x 2
    l1 = [spring,winter,fall]#Khai báo list l1 chứa các hình ảnh
    l2 = [spring,winter,fall,summer]#Khai báo list l2 chứa các hình ảnh
    l3=[] # Thêm hình ảnh vào list l3
    l=[l1,l2,l3]#Khai báo list l chứa các list l1 và l2
    l_final =[]#Khởi tạo list l_final rỗng
    while len(l_final) != len(l[level-1])*2:#Lặp vòng lặp cho len(l_final) != len(l[level-1])*2
        choice = l[level-1][random.randint(0,len(l[level-1])-1)]#Khởi tạo choice = l[level-1][random.randint(0,len(l[level-1])-1)]
        if l_final.count(choice) <= 1 : l_final.append(choice)#Nếu l_final có chứa choice <= 1 thì thêm choice vào l_final
    return l_final#Trả về l_final
#Hàm chính trong game
def game_loop(level = 1, oldchoosen = None, oldtile = None, old_x = None):#Hàm game_loop để chạy game
    pygame.mixer.music.unpause()#Chạy bản nhạc
    choosen = None#Khởi tạo choosen = None để kiểm tra xem có hình được chọn hay không
    time.sleep(0.1)#Thời gian chờ khi chạy game
    if old_x != None:#Nếu có hình được chọn
        x = old_x#Lấy hình được chọn
    else:#Nếu không có hình được chọn
        x = 1#Khởi tạo x = 1 để chạy game
    Won = None#Khởi tạo Won = None để kiểm tra xem đã thắng hay chưa
    gameExit = False#Khởi tạo gameExit = False để kiểm tra xem đã thoát game hay chưa
    if oldtile != None:#Nếu có hình được chọn
        tile = oldtile[:]#Lấy hình được chọn
    else:#Nếu không có hình được chọn
        tile = [False, False, False, False, False, False, False, False]#Hình ngẫu nhiên
    tile1 = tile[0]#Lấy hình được chọn
    tile2 = tile[1]#Lấy hình được chọn
    tile3 = tile[2]#Lấy hình được chọn
    tile4 = tile[3]#Lấy hình được chọn
    tile5 = tile[4]#Lấy hình được chọn
    tile6 = tile[5]#Lấy hình được chọn
    tile7 = tile[6]#Lấy hình được chọn
    tile8 = tile[7]#Lấy hình được chọn
    if oldchoosen != None:#Kiểm tra xem có hình được chọn hay không
        choosen = oldchoosen[:]#Lấy hình được chọn
    else:#Nếu không thì lấy hình ngẫu nhiên
        choosen = l_random(level)#Hình ngẫu nhiên
    while not gameExit:#Kiểm tra xem có thoát game hay không
        for event in pygame.event.get():#Lặp vòng lặp cho event có sự kiện
            if event.type == pygame.QUIT:#Nếu sự kiện là click vào nút thoát
                pygame.quit()#Tắt cửa sổ
                sys.exit()#Thoát chương trình
        if level == 1:# Nếu là level 1
            gameDisplay.blit(backgroundGameLoop,(0,0))#Vẽ background
            text('Level 1',display_width/2,display_height/10,35,white,'zerovelo.ttf')# Vẽ level 1 dạng text
            gameDisplay.blit(choosen[0],(100,100))#Vẽ hình ảnh cho hình được chọn tại vị trí (100,100)
            gameDisplay.blit(choosen[1],(300,100))#Vẽ hình ảnh cho hình được chọn tại vị trí (300,100)
            gameDisplay.blit(choosen[2],(500,100))#Vẽ hình ảnh cho hình được chọn tại vị trí (500,100)
            gameDisplay.blit(choosen[3],(100,300))#Vẽ hình ảnh cho hình được chọn tại vị trí (100,300)
            gameDisplay.blit(choosen[4],(300,300))#Vẽ hình ảnh cho hình được chọn tại vị trí (300,300)
            gameDisplay.blit(choosen[5],(500,300))#Vẽ hình ảnh cho hình được chọn tại vị trí (500,300)
        elif level == 2:# Nếu là level 2
            gameDisplay.blit(backgroundGameLoop,(0,0))#Vẽ background
            text('Level 2',display_width/2,display_height/10,35,white,'zerovelo.ttf')# Vẽ level 2 dạng text
            #Vẽ hình ảnh cho hình được chọn tại vị trí (x,y)
            gameDisplay.blit(pygame.transform.scale(choosen[0], (150, 150)),(175,100))#Vẽ hình ảnh cho hình được chọn
            gameDisplay.blit(pygame.transform.scale(choosen[1], (150, 150)),(325,100))#Vẽ hình ảnh cho hình được chọn
            gameDisplay.blit(pygame.transform.scale(choosen[2], (150, 150)),(475,100))#Vẽ hình ảnh cho hình được chọn
            gameDisplay.blit(pygame.transform.scale(choosen[3], (150, 150)),(175,250))#Vẽ hình ảnh cho hình được chọn
            gameDisplay.blit(pygame.transform.scale(choosen[4], (150, 150)),(325,250))#Vẽ hình ảnh cho hình được chọn
            gameDisplay.blit(pygame.transform.scale(choosen[5], (150, 150)),(475,250))#Vẽ hình ảnh cho hình được chọn
            gameDisplay.blit(pygame.transform.scale(choosen[6], (150, 150)),(250,400))#Vẽ hình ảnh cho hình được chọn
            gameDisplay.blit(pygame.transform.scale(choosen[7], (150, 150)),(400,400))#Vẽ hình ảnh cho hình được chọn
        else:# Nếu là level 3
            gameDisplay.blit(backgroundGameLoop,(0,0))#Vẽ background
            text('Level 3',display_width/2,display_height/10,35,white,'zerovelo.ttf')# Vẽ level 3 dạng text
            #Học sinh vẽ hình ảnh cho hình được chọn tại vị trí (x,y)
        if (Won == True):# Nếu thắng
            if level == 1 and tile.count(True) == 6:# Nếu là level 1 và đã chọn đủ hình 6
                game_loop(2)# Chạy lại game với level 2
            elif level == 2 and tile.count(True) == 8:# Nếu là level 2 và đã chọn đủ hình 8
                game_loop(3)# Chạy lại game với level 3
            else:# Nếu không
                #Thêm level mới
                pass
            #Chạy hết level thì chạy lại level 1
            game_loop(level, choosen, tile, x)# Chạy lại game với level hiện tại
            Won = None# Xóa biến Won
        if (Won == False):# Nếu thua
            time.sleep(0.4)#Thời gian chờ khi chạy game
            game_loop(level, choosen)# Chạy lại game với level hiện tại
        pos = pygame.mouse.get_pos()#Lấy tọa độ chuột
        click = pygame.mouse.get_pressed()#Lấy trạng thái chuột
        #Xữ lý bấm chuột
        if level == 1:# Nếu là level 1 thì xử lý bấm chuột tại vị trí (x,y)
            #row1
            if 300 > pos[0] > 100 and 300 > pos[1] > 100 and click[0] == 1:# Nếu click vào hình 1
                 tile1 = True#Tile1 được chọn 
            if 500 > pos[0] > 300 and 300 > pos[1] > 100 and click[0] == 1:# Nếu click vào hình 2
                 tile2 = True#Tile2 được chọn
            if 700 > pos[0] > 500 and 300 > pos[1] > 100 and click[0] == 1:# Nếu click vào hình 3
                 tile3 = True#Tile3 được chọn
            #row 2
            if 300 > pos[0] > 100 and 500 > pos[1] > 300 and click[0] == 1:# Nếu click vào hình 4
                 tile4 = True#Tile4 được chọn 
            if 500 > pos[0] > 300 and 500 > pos[1] > 300 and click[0] == 1:# Nếu click vào hình 5
                 tile5 = True#Tile5 được chọn
            if 700 > pos[0] > 500 and 500 > pos[1] > 300 and click[0] == 1:# Nếu click vào hình 6
                 tile6 = True#Tile6 được chọn
        elif level == 2:# Nếu là level 2, học sinh có thể thêm vào và xữ lý tọa độ chuột
            if 325 > pos[0] > 175 and 250 > pos[1] > 100 and click[0] == 1:# Nếu click vào hình 1
                 tile1 = True# Hình được chọn
            if 475 > pos[0] > 325 and 250 > pos[1] > 100 and click[0] == 1:# Nếu click vào hình 2
                 tile2 = True# Hình được chọn
            if 625 > pos[0] > 475 and 250 > pos[1] > 100 and click[0] == 1:# Nếu click vào hình 3
                 tile3 = True# Hình được chọn
            #row 2
            if 325 > pos[0] > 175 and 400 > pos[1] > 250 and click[0] == 1:# Nếu click vào hình 4
                 tile4 = True# Hình được chọn
            if 475 > pos[0] > 325 and 400 > pos[1] > 250 and click[0] == 1:# Nếu click vào hình 5
                 tile5 = True# Hình được chọn
            if 625 > pos[0] > 475 and 400 > pos[1] > 250 and click[0] == 1:# Nếu click vào hình 6
                 tile6 = True# Hình được chọn
            #row3
            if 400 > pos[0] > 250 and 550 > pos[1] > 400 and click[0] == 1:# Nếu click vào hình 7
                 tile7 = True# Hình được chọn
            if 550 > pos[0] > 400 and 550 > pos[1] > 400 and click[0] == 1:# Nếu click vào hình 8
                 tile8 = True# Hình được chọn
        else:# Nếu là level 3, học sinh có thể thêm vào
            pass
        tile = [tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8]# Lấy tất cả các hình được chọn
        #Xữ lý khi chọn đủ hình, thắng hoặc thua
        if tile.count(True) > x:# # Nếu số hình được chọn lớn hơn số hình được chọn trước đó
            if check_same(tile, choosen) == True:# Nếu các hình được chọn giống nhau
                if level == 1:# Nếu là level 1
                    text('Nice !!!',display_width/2,display_height/1.15,30,blue,'coolvetica rg.ttf')# In ra thông báo
                else:# Nếu là level 2 hoặc 3
                    text('Nice !!!',display_width/2,display_height/1.05,30,blue,'coolvetica rg.ttf')# In ra thông báo
                Won = True# Thắng
                x += 2# Tăng số hình được chọn trước đó lên 2  
            else:# Nếu không trùng
                if level == 1:# Nếu là level 1
                    text('Nope !!!',display_width/2,display_height/1.15,30,red,'coolvetica rg.ttf')# In ra thông báo
                else:# Nếu là level 2 hoặc 3
                    text('Nope !!!',display_width/2,display_height/1.05,30,red,'coolvetica rg.ttf')# In ra thông báo
                Won = False# Thua
        #Xử lý khi chưa chọn hình 
        if level == 1:# Nếu là level 1
            if not tile1: pygame.draw.rect(gameDisplay, white, (100,100,200,200))#Nếu hình 1 chưa được chọn thì vẽ hình chữ nhật che hình 1
            if not tile2: pygame.draw.rect(gameDisplay, white, (300,100,200,200))#Nếu hình 2 chưa được chọn thì vẽ hình chữ nhật che hình 2
            if not tile3: pygame.draw.rect(gameDisplay, white, (500,100,200,200))#Nếu hình 3 chưa được chọn thì vẽ hình chữ nhật che hình 3
            if not tile4: pygame.draw.rect(gameDisplay, white, (100,300,200,200))#Nếu hình 4 chưa được chọn thì vẽ hình chữ nhật che hình 4
            if not tile5: pygame.draw.rect(gameDisplay, white, (300,300,200,200))#Nếu hình 5 chưa được chọn thì vẽ hình chữ nhật che hình 5
            if not tile6: pygame.draw.rect(gameDisplay, white, (500,300,200,200))#Nếu hình 6 chưa được chọn thì vẽ hình chữ nhật che hình 6
        elif level == 2:# Nếu là level 2,học sinh có thể thêm vào
            if not tile1: pygame.draw.rect(gameDisplay, white, (175,100,150,150))# Vẽ hình 1
            if not tile2: pygame.draw.rect(gameDisplay, white, (325,100,150,150))# Vẽ hình 2
            if not tile3: pygame.draw.rect(gameDisplay, white, (475,100,150,150))# Vẽ hình 3
            if not tile4: pygame.draw.rect(gameDisplay, white, (175,250,150,150))# Vẽ hình 4
            if not tile5: pygame.draw.rect(gameDisplay, white, (325,250,150,150))# Vẽ hình 5
            if not tile6: pygame.draw.rect(gameDisplay, white, (475,250,150,150))# Vẽ hình 6
            if not tile7: pygame.draw.rect(gameDisplay, white, (250,400,150,150))# Vẽ hình 7
            if not tile8: pygame.draw.rect(gameDisplay, white, (400,400,150,150))# Vẽ hình 8
        else:# Nếu là level 3, học sinh có thể thêm vào
            pass
        #Vẽ các đường thẳng để tạo nên các ô vuông
        if level == 1:# Nếu là level 1 thì vẽ các đường kẻ
            # horizontal
            pygame.draw.line(gameDisplay, black, (100,100),(700,100),5)# Vẽ đường ngang
            pygame.draw.line(gameDisplay, black, (100,300),(700,300),5)# Vẽ đường ngang
            pygame.draw.line(gameDisplay, black, (100,500),(700,500),5)# Vẽ đường ngang
            # vertical
            pygame.draw.line(gameDisplay, black, (100,100),(100,500),5)# Vẽ đường dọc
            pygame.draw.line(gameDisplay, black, (300,100),(300,500),5)# Vẽ đường dọc
            pygame.draw.line(gameDisplay, black, (500,100),(500,500),5)# Vẽ đường dọc
            pygame.draw.line(gameDisplay, black, (700,100),(700,500),5)# Vẽ đường dọc
        elif level == 2:# Nếu là level 2, học sinh có thể thêm vào
            # horizontal
            pygame.draw.line(gameDisplay, black, (175,100),(625,100),5)# Vẽ đường ngang
            pygame.draw.line(gameDisplay, black, (175,250),(625,250),5)# Vẽ đường ngang
            pygame.draw.line(gameDisplay, black, (175,400),(625,400),5)# Vẽ đường ngang
            pygame.draw.line(gameDisplay, black, (250,550),(550,550),5)# Vẽ đường ngang
            # vertical
            pygame.draw.line(gameDisplay, black, (175,100),(175,400),5)# Vẽ đường dọc
            pygame.draw.line(gameDisplay, black, (325,100),(325,400),5)# Vẽ đường dọc
            pygame.draw.line(gameDisplay, black, (475,100),(475,400),5)# Vẽ đường dọc
            pygame.draw.line(gameDisplay, black, (625,100),(625,400),5)# Vẽ đường dọc
            pygame.draw.line(gameDisplay, black, (250,400),(250,550),5)# Vẽ đường dọc
            pygame.draw.line(gameDisplay, black, (400,400),(400,550),5)# Vẽ đường dọc
            pygame.draw.line(gameDisplay, black, (550,400),(550,550),5)# Vẽ đường dọc
        else:# Nếu là level 3, học sinh có thể thêm vào
            pass
        pygame.display.update()# Cập nhật màn hình
        clock.tick(60)# Tốc độ 60 frame/s
game_intro()# Chạy game intro

