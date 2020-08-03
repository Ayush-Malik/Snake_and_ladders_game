import pygame
import random
import math
from pygame import mixer

pygame.init()
mainclock = pygame.time.Clock()



# COLOURS 
RED_COLOR = (255 , 0 , 0)
GREEN_COLOR = (0 , 255 , 0)
BLUE_COLOR = (0 , 0 , 255)
YELLOW_COLOR = (255 , 255 , 0)
BLACK_COLOR = (0 , 0 , 0)
WHITE_COLOR = (255 , 255 , 255)



SCREEN = pygame.display.set_mode( (600 , 700) )

BOARD_IMG = pygame.image.load('BOARD_IMG.jpg')

START_X_VAL = 10
START_Y_VAL = 550

HOME_RED_X = 10
HOME_RED_Y = 610

HOME_GREEN_X = 60
HOME_GREEN_Y = 610


HOME_YELLOW_X = 10
HOME_YELLOW_Y = 655

HOME_BLUE_X = 60
HOME_BLUE_Y = 655


# [ CH_TO_BE_PRINTED , 'COLOR' , X_CO-ORDINATE , Y_CO-ORDINATE , CURRENT_POSITION_NUMBER , X_CHANGE_VAL , upward_shifter ]

PLAYERS_LIS = [ ['R' , RED_COLOR , HOME_RED_X , HOME_RED_Y , 0 , +60 , 1] , ['G' , GREEN_COLOR , HOME_GREEN_X , HOME_GREEN_Y , 0 , +60 , 1] , ['Y' , YELLOW_COLOR , HOME_YELLOW_X , HOME_YELLOW_Y , 0 , +60 , 1 ] , ['B' , BLUE_COLOR , HOME_BLUE_X , HOME_BLUE_Y , 0 , +60 , 1] ]

index_of_players_lis = 3

def GAME_OVER_SCREEN():

    SCREEN.fill(RED_COLOR)
    game_over_font = pygame.font.SysFont('comicsansms', 70)
    game_over_text = game_over_font.render("GAME_OVER" , True , BLACK_COLOR)
    my_text_1 = game_over_font.render("DEVELOPED BY : " , True , BLACK_COLOR)
    my_text_2 = game_over_font.render("MALIK (^_^)" , True , BLACK_COLOR)

    SCREEN.blit(game_over_text , (50 , 150))
    SCREEN.blit(my_text_1 , (30 , 300))
    SCREEN.blit(my_text_2 , (60 , 400))
    pygame.display.update()
    return


def player_drawer():
    SCREEN.blit(BOARD_IMG , (0 , 0))
    
    for i in range(4): 
        CH_TO_BE_PRINTED , COLOR , x , y , CURRENT_POSITION_NUMBER , X_CHANGE_VAL , upward_shifter = PLAYERS_LIS[i]
        pygame.draw.rect(SCREEN , BLACK_COLOR , (x - 3 , y - 3 , 46 , 46))
        pygame.draw.rect(SCREEN , COLOR , (x , y , 40 , 40))
        ch_font = pygame.font.SysFont('cominsansms' , 30 )
        ch_text = ch_font.render(CH_TO_BE_PRINTED , True , BLACK_COLOR)
        SCREEN.blit(ch_text , (x + 2 , y + 2))
    pygame.display.update()
    

    

def COLLISION():
    global index_of_players_lis

    k = index_of_players_lis
    x_1 , y_1 = PLAYERS_LIS[k][2] , PLAYERS_LIS[k][3]

    for i in range(len(PLAYERS_LIS)):
        if i != k:
            x_2 , y_2 = PLAYERS_LIS[i][2] , PLAYERS_LIS[i][3]
            distance = math.sqrt( (y_2 - y_1)**2 + (x_2 - x_1)**2 )
            if distance <= 20:
                CH_TO_BE_PRINTED , COLOR , x , y , CURRENT_POSITION_NUMBER , X_CHANGE_VAL , upward_shifter = PLAYERS_LIS[i]
                
                CURRENT_POSITION_NUMBER = 0
                upward_shifter = 1
                X_CHANGE_VAL = +60
 
                if i == 0 :
                    x = HOME_RED_X
                    y = HOME_RED_Y
                elif i == 1 :
                    x = HOME_GREEN_X
                    y = HOME_GREEN_Y
                elif i == 2 :
                    x = HOME_YELLOW_X
                    y = HOME_YELLOW_Y
                elif i == 3 :
                    x = HOME_BLUE_X
                    y = HOME_BLUE_Y
                
                PLAYERS_LIS[i] = CH_TO_BE_PRINTED , COLOR , x , y , CURRENT_POSITION_NUMBER , X_CHANGE_VAL , upward_shifter
                player_drawer()
                
            









def LADDER():
    
    CH_TO_BE_PRINTED , COLOR , x , y , CURRENT_POSITION_NUMBER , X_CHANGE_VAL , upward_shifter = PLAYERS_LIS[index_of_players_lis]
    X = CURRENT_POSITION_NUMBER
    

    if X == 4:
        x += 60 
        y += 2*(-60)
        CURRENT_POSITION_NUMBER = 25
        upward_shifter = 21

    elif X == 13:
        x += 2*(-60)
        y += 3*(-60)
        CURRENT_POSITION_NUMBER = 46
        upward_shifter = 41
        X_CHANGE_VAL =-X_CHANGE_VAL

    elif X == 33:
        x += 60
        y += (-60)
        CURRENT_POSITION_NUMBER = 49
        upward_shifter = 41
        X_CHANGE_VAL = -X_CHANGE_VAL

    elif X == 42:
        x += 60
        y += 2*(-60)
        CURRENT_POSITION_NUMBER = 63
        upward_shifter = 61

    elif X == 50:
        x += (-60)
        y += 2*(-60)
        CURRENT_POSITION_NUMBER = 69
        upward_shifter = 61
    
    elif X == 62:
        x += (-60)
        y += 2*(-60)
        CURRENT_POSITION_NUMBER = 81
        upward_shifter = 81
    
    elif X == 74:
        x += 2*(60)
        y += 2*(-60)
        CURRENT_POSITION_NUMBER = 92
        upward_shifter = 91
    

    PLAYERS_LIS[index_of_players_lis] = [CH_TO_BE_PRINTED , COLOR , x , y , CURRENT_POSITION_NUMBER , X_CHANGE_VAL , upward_shifter]
    
def SNAKE():
    
    CH_TO_BE_PRINTED , COLOR , x , y , CURRENT_POSITION_NUMBER , X_CHANGE_VAL , upward_shifter = PLAYERS_LIS[index_of_players_lis]
    X = CURRENT_POSITION_NUMBER
   
    if X == 27:
        x += 2*(-60)
        y += 2*(60)
        CURRENT_POSITION_NUMBER = 5
        upward_shifter = 1

    elif X == 40:
        x += 2*(60)
        y += 3*(60)
        CURRENT_POSITION_NUMBER = 3
        upward_shifter = 1
        X_CHANGE_VAL = -X_CHANGE_VAL
    
    elif X == 43:
        x += 0
        y += 3*(60)
        CURRENT_POSITION_NUMBER = 18
        upward_shifter = 11
        X_CHANGE_VAL = -X_CHANGE_VAL

    elif X == 54:
        x += 3*(60)
        y += 2*(60)
        CURRENT_POSITION_NUMBER = 31
        upward_shifter = 31

    elif X == 66:
        x += (-60)
        y += 2*(-60) 
        CURRENT_POSITION_NUMBER = 45
        upward_shifter = 41
    
    elif X == 76:
        x += 2*(-60)
        y += 2*(60)
        CURRENT_POSITION_NUMBER = 58
        upward_shifter = 51
    
    elif X == 89:
        x += (-60)
        y += 3*(60)
        CURRENT_POSITION_NUMBER = 53
        upward_shifter = 51
        X_CHANGE_VAL = -X_CHANGE_VAL
    
    elif X == 99:
        x += (-60)
        y += 5*(60)
        CURRENT_POSITION_NUMBER = 41
        upward_shifter = 41
        X_CHANGE_VAL = -X_CHANGE_VAL

    
    PLAYERS_LIS[index_of_players_lis] = [CH_TO_BE_PRINTED , COLOR , x , y , CURRENT_POSITION_NUMBER , X_CHANGE_VAL , upward_shifter]
    print("After " , CURRENT_POSITION_NUMBER , upward_shifter )
    

    




total_rand_num = 0
rand_num = 1
def random_num_printer():
    global rand_num
    global index_of_players_lis 
    global total_rand_num 
    global button_state

    # ROTATION OF PLAYERS FOR THEIR TURNS
    

    
    if rand_num != 6:
        index_of_players_lis += 1
        index_of_players_lis = index_of_players_lis % 4
        
    COLOR = PLAYERS_LIS[index_of_players_lis][1]

    rand_num = random.randint(1 , 6)
    pygame.draw.rect(SCREEN , BLACK_COLOR , (440 , 620 , 70 , 70))
    font = pygame.font.SysFont('comicsansms' , 40)
    text = font.render("Random number : " + str(rand_num) , True , COLOR)
    SCREEN.blit(text , (120 , 620))




    CH_TO_BE_PRINTED , COLOR , x , y , CURRENT_POSITION_NUMBER , X_CHANGE_VAL , upward_shifter = PLAYERS_LIS[index_of_players_lis]
    
    if (rand_num == 6 or rand_num == 1) and CURRENT_POSITION_NUMBER == 0:
        CURRENT_POSITION_NUMBER = 1
        x = START_X_VAL
        y = START_Y_VAL

        if index_of_players_lis == 0 :
            a = HOME_RED_X
            b = HOME_RED_Y
        elif index_of_players_lis == 1 :
            a = HOME_GREEN_X
            b = HOME_GREEN_Y
        elif index_of_players_lis == 2 :
            a = HOME_YELLOW_X
            b = HOME_YELLOW_Y
        elif index_of_players_lis == 3 :
            a = HOME_BLUE_X
            b = HOME_BLUE_Y

        pygame.draw.rect(SCREEN , BLACK_COLOR , (a - 3 , b - 3 , 46 , 46))
        
        PLAYERS_LIS[index_of_players_lis] = [CH_TO_BE_PRINTED , COLOR , x , y , CURRENT_POSITION_NUMBER , X_CHANGE_VAL , upward_shifter]

        
        button_state = True
        player_drawer()
        return
    elif CURRENT_POSITION_NUMBER == 0 and rand_num != 6 and rand_num != 1:
        button_state = True
        player_drawer()
        return

    

    total_rand_num += rand_num
    

    if total_rand_num == 18:
        rand_num = 1
        total_rand_num = 0
        button_state = True
        return

    if rand_num == 6:
        button_state = True
        return

    if rand_num != 6:
        rand_num = total_rand_num
        total_rand_num = 0

    
    





    MOVE_DECIDER()



def MOVE_DECIDER():
    global COLOR
    global index_of_players_lis
    global upward_shifter
    global button_state


    
    
    CH_TO_BE_PRINTED , COLOR , x , y , CURRENT_POSITION_NUMBER , X_CHANGE_VAL , upward_shifter = PLAYERS_LIS[index_of_players_lis]
    

    counter = 0

    Target = CURRENT_POSITION_NUMBER + rand_num 
    if Target > 100:
        button_state = True
        return
        
    while CURRENT_POSITION_NUMBER < Target:
        player_move_sound = mixer.Sound('PLAYER_MOVE.wav')
        player_move_sound.play()

        counter += 1
        CURRENT_POSITION_NUMBER += 1
        
        if upward_shifter + 10 == CURRENT_POSITION_NUMBER:
            X_CHANGE_VAL = -X_CHANGE_VAL
            y -= 60
            upward_shifter += 10

        if CURRENT_POSITION_NUMBER != upward_shifter: # when goti is shifted upward the x don't change once
            x += X_CHANGE_VAL 

        PLAYERS_LIS[index_of_players_lis] = [CH_TO_BE_PRINTED , COLOR , x , y , CURRENT_POSITION_NUMBER , X_CHANGE_VAL , upward_shifter]
        
        player_drawer() # blit the players onto the screen
        # time_wasting_function()
        mainclock.tick(1)
        if counter == 6 :
            counter = 0 
            COLLISION()
        if CURRENT_POSITION_NUMBER == 100 :
            GAME_OVER_SCREEN()
            button_state = False
            return
        
                
        
    
    X = CURRENT_POSITION_NUMBER

    if X == 4 or X == 13 or X == 33 or X == 42 or X == 50 or X == 62 or X == 74 : # LADDERS_STARTING_NUM
        LADDER()
        player_drawer()
    elif X == 27 or X == 40 or X == 43 or X == 54 or X == 66 or X == 76 or X == 89 or X == 99: # SNAKE_STARTING_NUM
        SNAKE()
        player_drawer()


    COLLISION()



    
    



    button_state = True

    





RUNNING = True
button_state = True 
SCREEN.blit(BOARD_IMG , (0 , 0))
player_drawer()



while RUNNING :
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_KP_ENTER and button_state  :
                dice_sound = mixer.Sound('DICE_THROW.wav')
                dice_sound.play()
                button_state = False
                random_num_printer()
    

    pygame.display.update()

