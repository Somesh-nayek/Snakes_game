import json
import pygame
import random
import os
pygame.mixer.init()
pygame.init()

# colours
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
maroon = (128, 0, 0)
teal = (0, 128, 128)
slate_grey = (112, 128, 144)
navy_blue = (0, 0, 128)
forest_green = (34, 139, 34)
dark_grey = (169, 169, 169)
coral = (255, 127, 80)
snake_size = 15
light_green = (136, 196, 38)
name = input("Enter player name:-")
if(name!=None):
    # creating window
    screen_width = 900
    screen_height = 500
    gamewindow = pygame.display.set_mode((screen_width, screen_height))
    bgimg = pygame.image.load('welcome.jpg')
    bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()
    gimg = pygame.image.load('game.jpg')
    gimg = pygame.transform.scale(gimg, (screen_width, screen_height)).convert_alpha()
    img = pygame.image.load('gameover.jpg')
    img = pygame.transform.scale(img, (screen_width, screen_height)).convert_alpha()

    pygame.display.set_caption("PYTHON PROJECT")
    pygame.display.update()
    clock = pygame.time.Clock()
    
    
    def text_screen(text, fontSize, colour, x, y):
        font = pygame.font.SysFont('bleeding', fontSize)
        screen_text = font.render(text, True, colour)
        gamewindow.blit(screen_text, [x, y])
    
    
    def plot_snake(gamewindow, color, snk_list, snk_size):
        for x, y in snk_list:
            pygame.draw.rect(gamewindow, teal, [x, y, snake_size, snake_size])
    
    
    def welcome():
        exit_gaame = False
        while not exit_gaame:
            gamewindow.fill(teal)
            gamewindow.blit(bgimg, (0, 0))
            text_screen("welcome to snakes game", 60, light_green, 190, 280)
            text_screen("Press space bar to play", 60, light_green, 215, 320)
            # text_screen("somesh nayek",forest_green,200,170)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_gaame = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_loop()
            pygame.display.update()
            clock.tick(60)
    
    
    def game_loop():
        pygame.mixer.music.load('back.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
    
        # game specific variables
    
        exit_game = False
        game_over = False
        snake_x = 45
        snake_y = 45
        velocity_x = 0
        velocity_y = 0
        snk_list = []
        snk_length = 1
        count=0
        with open("high_score.txt", "r") as f:
            highscore = f.read()
        food_x = random.randint(100, 700)
        food_y = random.randint(50, 400)
        score = 0
        food_size = 10
        init_velocity = 5
        snake_size = 50
        fps = 60
    
        # check if highscore file exists
    
        if (not os.path.exists("high_score.txt")):
            with open("high_score.txt", "w") as f:
                f.write("0")
        with open("high_score.txt", "r") as f:
            highscore = f.read()
        while not exit_game:
            if game_over:
                with open("high_score.txt", "w") as f:
                    f.write(str(highscore))
                if(count==0):
                    player_data={"name":name,"score":score}
                    with open("Players.txt","a") as f:
                        f.write(str(player_data))
                        f.write('\n')
                    count=count+1
                gamewindow.fill(black)
                gamewindow.blit(img, (0, 0))
                text_screen("Press Enter to continue...", 50, dark_grey, 260, 310)
    
                text_screen("score:-" + str(score), 30, white, 5, 5)
    
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit_game = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            welcome()
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit_game = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT and velocity_x != -5:
                            velocity_x = 5
                            velocity_y = 0
                        if event.key == pygame.K_LEFT and velocity_x != 5:
                            velocity_x = -5
                            velocity_y = 0
                        if event.key == pygame.K_UP and velocity_y != 5:
                            velocity_y = -5
                            velocity_x = 0
                        if event.key == pygame.K_DOWN and velocity_y != -5:
                            velocity_y = 5
                            velocity_x = 0
                snake_x += velocity_x
                snake_y += velocity_y
                if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
                    pygame.mixer.Sound('beep.mp3').play()
                    score += 10
                    food_x = random.randint(100, 700)
                    food_y = random.randint(50, 400)
                    snk_length += 10
                    if score > int(highscore):
                        highscore = score
                gamewindow.fill(forest_green)
                gamewindow.blit(gimg, (0, 0))
                text_screen("score:-" + str(score) + "  Hi-score:-" + str(highscore), 30, white, 5, 5)
                pygame.draw.rect(gamewindow, coral, [food_x, food_y, food_size, food_size])
    
                head = []
                head.append(snake_x)
                head.append(snake_y)
                snk_list.append(head)
                if len(snk_list) > snk_length:
                    del snk_list[0]
                if head in snk_list[:-1]:
                    pygame.mixer.music.load('gameover.mp3')
                    pygame.mixer.music.play()
                    game_over = True
                if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                    pygame.mixer.music.load('gameover.mp3')
                    pygame.mixer.music.play()
                    game_over = True
                plot_snake(gamewindow, forest_green, snk_list, snake_size)
            pygame.display.update()
            clock.tick(60)
        pygame.quit()
        quit()
    
    
    welcome()
