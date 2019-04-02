import pygame, sys

pygame.init()


def start_screen():
    start_text = largeFont.render('Hit SPACE to Start', True, black)
    start_rect = start_text.get_rect()
    start_rect.center = size//2, size//2

    info_text1 = smallFont.render('Player 1: left click, 1 for delete', True, black)
    info_rect1 = info_text1.get_rect()
    info_rect1.center = size//2, size//2+40

    info_text2 = smallFont.render('Player 2: right click, 2 for delete', True, black)
    info_rect2 = info_text2.get_rect()
    info_rect2.center = size//2, size//2+60

    # info_text3 = smallFont.render('Q for quit, R for restart', True, black)
    # info_rect3 = info_text3.get_rect()
    # info_rect3.center = size // 2, size // 2 + 80

    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    start = False

        window.fill(white)
        window.blit(start_text, start_rect)
        window.blit(info_text1, info_rect1)
        window.blit(info_text2, info_rect2)
        # window.blit(info_text3, info_rect3)
        clock.tick(FPS)
        pygame.display.update()


def pause():
    pause = True

    pause_text = largeFont.render('Pause', True, black)
    pause_text_rect = pause_text.get_rect()
    pause_text_rect.center = size//2, size//2

    pause_text2 = smallFont.render('Press p to unpause, r to restart', True, black)
    pause_text2_rect = pause_text2.get_rect()
    pause_text2_rect.center = size//2, size//2+40

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_p:
                    pause = False
                elif event.key == pygame.K_r:
                    player_1_List.clear()
                    player_2_List.clear()
                    pause = False

        window.fill(white)
        window.blit(pause_text, pause_text_rect)
        window.blit(pause_text2, pause_text2_rect)
        clock.tick(5)
        pygame.display.update()


def player_1(x, y):
    pygame.draw.circle(window, black, (x+block//2, y+1+block//2), block//2-2, 1)

def player_2(x, y):
    pygame.draw.aaline(window, black, (x, y), (x+block, y+block))
    pygame.draw.aaline(window, black, (x, y+block), (x+block, y))

def board():
    pygame.draw.rect(window, black, (dist, dist, board_size, board_size), 2)

    pygame.draw.line(window, black, (dist, dist+block,), (5+board_size, dist+block))
    pygame.draw.line(window, black, (dist, dist+block*2,), (dist+board_size, dist+block*2))

    pygame.draw.line(window, black, (dist+block, dist,), (dist+block, dist+board_size))
    pygame.draw.line(window, black, (dist+block*2, dist,), (dist+block*2, dist+board_size))


largeFont = pygame.font.SysFont('Arial', 40)
smallFont = pygame.font.SysFont('Arial', 15)
white = (255,255,255)
black= (0,0,0)
block = 120
size = 370
window = pygame.display.set_mode((size, size))
clock = pygame.time.Clock()
board_size = 360
dist = 5
FPS = 15
# squares move from left to right, row by row
square_1_x, square_1_y = dist, dist
square_2_x, square_2_y = dist+block, dist
square_3_x, square_3_y = dist+block*2, dist
square_4_x, square_4_y = dist, dist+block
square_5_x, square_5_y = dist+block, dist+block
square_6_x, square_6_y = dist+block*2, dist+block
square_7_x, square_7_y = dist, dist+block*2
square_8_x, square_8_y = dist+block, dist+block*2
square_9_x, square_9_y = dist+block*2, dist+block*2
#
s1 = 0
s2 = 0
s3 = 0
s4 = 0
s5 = 0
s6 = 0
s7 = 0
s8 = 0
s9 = 0

player_1_List = []
player_2_List = []


def game_loop():
    done = False

    while not done:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        # for event in pygame.event.get():
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_p:
        #             pause()
        window.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN :
                if event.key == pygame.K_q:
                    done = True

                # DELETE OBJECT
                elif event.key == pygame.K_1:
                    if len(player_1_List) >= 1:
                        player_1_List.pop()
                elif event.key == pygame.K_2:
                    if len(player_2_List) >= 1:
                        player_2_List.pop()


                elif event.key == pygame.K_p:
                    pause()


        board()
        # square 1
        if square_1_x <= mouse[0] <= square_2_x and square_1_y < mouse[1] < square_4_y:
            if click[0] == 1:
                player_1_List.append((square_1_x, square_1_y))
                player_1(square_1_x, square_1_y)
            elif click[2] == 1:
                player_2_List.append((square_1_x, square_1_y))
                player_2(square_1_x, square_1_y)
        # square 2
        elif square_2_x <= mouse[0] <= square_3_x and square_1_y < mouse[1] < square_4_y:
            if click[0] == 1:
                player_1_List.append((square_2_x, square_2_y))
                player_1(square_2_x,square_2_y)
            elif click[2] == 1:
                player_2_List.append((square_2_x, square_2_y))
                player_2(square_2_x, square_2_y)
        # square 3
        elif square_3_x <= mouse[0] <= square_3_x+block and square_1_y < mouse[1] < square_4_y:
            if click[0] == 1:
                player_1_List.append((square_3_x, square_3_y))
                player_1(square_3_x, square_3_y)
            elif click[2] == 1:
                player_2_List.append((square_3_x, square_3_y))
                player_2(square_3_x, square_3_y)
        # square 4
        elif square_4_x <= mouse[0] <= square_5_x and square_4_y < mouse[1] < square_7_y:
            if click[0] == 1:
                player_1_List.append((square_4_x, square_4_y))
                player_1(square_4_x, square_4_y)
            elif click[2] == 1:
                player_2_List.append((square_4_x, square_4_y))
                player_2(square_4_x, square_4_y)
        # square 5
        elif square_5_x <= mouse[0] <= square_6_x and square_4_y < mouse[1] < square_7_y:
            if click[0] == 1:
                player_1_List.append((square_5_x, square_5_y))
                player_1(square_5_x, square_5_y)
            elif click[2] == 1:
                player_2_List.append((square_5_x, square_5_y))
                player_2(square_5_x, square_5_y)
        # square 6
        elif square_6_x <= mouse[0] <= square_6_x+block and square_4_y < mouse[1] < square_7_y:
            if click[0] == 1:
                player_1_List.append((square_6_x, square_6_y))
                player_1(square_6_x, square_6_y)
            elif click[2] == 1:
                player_2_List.append((square_6_x, square_6_y))
                player_2(square_6_x, square_6_y)
        # square 7
        elif square_7_x <= mouse[0] <= square_8_x and square_7_y < mouse[1] < square_7_y+block:
            if click[0] == 1:
                player_1_List.append((square_7_x, square_7_y))
                player_1(square_7_x, square_7_y)
            elif click[2] == 1:
                player_2_List.append((square_7_x, square_7_y))
                player_2(square_7_x, square_7_y)
        # square 8
        elif square_8_x <= mouse[0] <= square_9_x and square_7_y < mouse[1] < square_7_y+block:
            if click[0] == 1:
                player_1_List.append((square_8_x, square_8_y))
                player_1(square_8_x, square_8_y)
            elif click[2] == 1:
                player_2_List.append((square_8_x, square_8_y))
                player_2(square_8_x, square_8_y)
        # square 9
        elif square_9_x <= mouse[0] <= square_9_x+block and square_7_y < mouse[1] < square_7_y+block:
            if click[0] == 1:
                player_1_List.append((square_9_x, square_9_y))
                player_1(square_9_x, square_9_y)
            elif click[2] == 1:
                player_2_List.append((square_9_x, square_9_y))
                player_2(square_9_x, square_9_y)

        for i in player_1_List:
            player_1(i[0], i[1])
        for i in player_2_List:
            player_2(i[0], i[1])




        pygame.display.update()
        clock.tick(FPS)
start_screen()
game_loop()
pygame.quit()

