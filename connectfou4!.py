import numpy as np
import pygame
import button
import math
pygame.init()

SQUARE_SIZE=70
RADIUS=int(SQUARE_SIZE/2-5)
WIDTH=500
HIEGHT=600
screen=pygame.display.set_mode((WIDTH,HIEGHT))
pygame.display.set_caption("Connect Fou4 !")

font=pygame.font.SysFont("Berlin Sans FB",60)
play_img=pygame.image.load("play.png").convert_alpha()
play_button=button.Button(170,275,play_img,1)
exit_img=pygame.image.load("exitt.png").convert_alpha()
exit_button=button.Button(170,375,exit_img,1)
exit_button1=button.Button(5,10,exit_img,1)
home_img=pygame.image.load("menu.png").convert_alpha()
home_button=button.Button(335,10,home_img,1)
newgame_img=pygame.image.load("newgame.png").convert_alpha()
newgame_button=button.Button(170,10,newgame_img,1)
connect4_img=pygame.image.load("connect4img.jpg").convert_alpha()
background=pygame.image.load("backg.jpg")

def create_board(ROW,COLUMN):
    board = np.zeros((ROW,COLUMN))
    return board

def drop_piece(board,selction,row,player):
    board[row][selction]=player
    return board

def is_valid(board,selection):
    if board[0][selection]==0:
        return True
    else:
        return False    

def available_row(board,selection):
    ava_row=0
    for i in range(ROW):
        if board[i][selection]==0:
            ava_row=i
    return ava_row

def did_win(board,piece):
    for i in range(ROW):
        for j in range(COLUMN-3):
            if board[i][j]==piece and board[i][j+1]==piece and board[i][j+2]==piece and board[i][j+3]==piece:
                return True
    for j in range(COLUMN):
        for i in range(ROW-3):
            if board[ROW-i-1][j]==piece and board[ROW-i-2][j]==piece and board[ROW-i-3][j]==piece and board[ROW-i-4][j]==piece:
                return True
    for i in range(ROW-3):
        for j in range(COLUMN-3):
            if board[ROW-i-1][j]==piece and board[ROW-i-2][j+1]==piece and board[ROW-i-3][j+2]==piece and board[ROW-i-4][j+3]==piece:
                return True
    for i in range(ROW-3):
        for j in range(COLUMN-3):
            if board[ROW-i-1][COLUMN+j-4]==piece and board[ROW-i-2][COLUMN+j-5]==piece and board[ROW-i-3][COLUMN+j-6]==piece and board[ROW-i-4][COLUMN+j-7]==piece:
                return True 

def game_on(board):
    game=False
    for i in range(ROW):
        for j in range(COLUMN):
            if board[i][j]==0:
                game=True
                return game
    return game


def draw_board(board):
    for c in range(COLUMN):
        for r in range(ROW+1):            
            pygame.draw.rect(screen,(0,50,155),(c*SQUARE_SIZE+5, r*SQUARE_SIZE+2*SQUARE_SIZE+30,SQUARE_SIZE,SQUARE_SIZE))
            if r!=ROW:
                if board[r][c]==0:
                    pygame.draw.circle(screen,(0,0,0),(int(c*SQUARE_SIZE+5+SQUARE_SIZE/2),int(r*SQUARE_SIZE+5*SQUARE_SIZE/2)+30),RADIUS)
                elif board[r][c]==1:
                    pygame.draw.circle(screen,(255,0,0),(int(c*SQUARE_SIZE+5+SQUARE_SIZE/2),int(r*SQUARE_SIZE+5*SQUARE_SIZE/2)+30),RADIUS)
                elif board[r][c]==2:
                    pygame.draw.circle(screen,(255,255,0),(int(c*SQUARE_SIZE+5+SQUARE_SIZE/2),int(r*SQUARE_SIZE+5*SQUARE_SIZE/2)+30),RADIUS)
    pygame.display.update()
   
ROW=6
COLUMN=7
def main_game():
    board=create_board(ROW,COLUMN)
    turn=0 
    GAMEOVER=False
    screen.blit(background,(0,0))
    draw_board(board)
    for c in range(COLUMN):
        pygame.draw.rect(screen,(0,0,0),(c*SQUARE_SIZE+5, 0*SQUARE_SIZE+2*SQUARE_SIZE-40,SQUARE_SIZE,SQUARE_SIZE))
    # pygame.display.flip()
    while GAMEOVER==False:
        for event in pygame.event.get():
            if event.type==pygame.MOUSEMOTION:
                pygame.draw.rect(screen,(0,0,0),(0,100,WIDTH,SQUARE_SIZE))
                posx=event.pos[0]
                if turn==0:
                    pygame.draw.circle(screen,(255,0,0),(posx,int(SQUARE_SIZE/2)+100),RADIUS)
                else:
                    pygame.draw.circle(screen,(255,255,0),(posx,int(SQUARE_SIZE/2)+100),RADIUS)
                pygame.display.update()
            if home_button.draw(screen):
                menu_()
            if newgame_button.draw(screen):
                main_game()
            if event.type == pygame.QUIT:
                GAMEOVER=False
                raise SystemExit
            if exit_button1.draw(screen):
                raise SystemExit
            if event.type==pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen,(0,0,0),(0,100,WIDTH,SQUARE_SIZE))
                if turn==0:
                    posx=event.pos[0]
                    selection=int(math.floor(posx/SQUARE_SIZE))
                    if is_valid(board,selection):
                        row=available_row(board,selection)
                        board=drop_piece(board,selection,row,1)
                        if did_win(board,1):
                            label=font.render("Player 1 wins!",1,(255,0,0))
                            screen.blit(label,(110,115))
                            GAMEOVER=True
                        elif not game_on(board):
                            label=font.render("Match Tied!!",1,(0,155,0))
                            screen.blit(label,(120,100))
                            GAMEOVER=True
                        else:
                            turn=1    
                elif turn==1:
                    posx=event.pos[0]
                    selection=int(math.floor(posx/SQUARE_SIZE))
                    if is_valid(board,selection):
                        row=available_row(board,selection)
                        board=drop_piece(board,selection,row,2)
                        if did_win(board,2):
                            label=font.render("Player 2 wins!",1,(255,255,0))
                            screen.blit(label,(80,100))
                            GAMEOVER=True
                        elif not game_on(board):
                            label=font.render("Match Tied!",1,(0,155,0))
                            screen.blit(label,(120,100))
                            GAMEOVER=True
                        else:
                            turn=0
                print(board)
                draw_board(board)
        pygame.display.update()
            
def menu_():
    screen.blit(background,(0,0))
    screen.blit(connect4_img,(0,0))
    run=True
    while run:
        if play_button.draw(screen):
            main_game()
        if exit_button.draw(screen):
            raise SystemExit
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                raise SystemExit
        pygame.display.update()        
menu_()           




