#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame
import time
#可從參數化設定這邊更改所要更改的值
WIN_WIDTH = 1024
WIN_HEIGHT = 600
ENEMY_WIDTH=50
ENEMY_HEIGHT=50
BTN_WIDTH = 80
BTN_HEIGHT = 80
HP_WIDTH = 40
HP_HEIGHT = 40
FPS = 30
TIME_SIZE=26
# color (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# initialization#pygame初始化
pygame.init()
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
# load image (background, enemy, buttons)
#建立圖片庫並轉成想要格式
background_image = pygame.transform.scale(pygame.image.load("images/Map.png"), (WIN_WIDTH, WIN_HEIGHT))
enemy_image = pygame.transform.scale(pygame.image.load("images/enemy.png"), (ENEMY_WIDTH, ENEMY_HEIGHT))

hp_gray_image = pygame.transform.scale(pygame.image.load("images/hp_gray.png"), (HP_WIDTH, HP_HEIGHT))
hp_image = pygame.transform.scale(pygame.image.load("images/hp.png"), (HP_WIDTH, HP_HEIGHT))

continue_image = pygame.transform.scale(pygame.image.load("images/continue.png"), (BTN_WIDTH, BTN_HEIGHT))
muse_image = pygame.transform.scale(pygame.image.load("images/muse.png"), (BTN_WIDTH, BTN_HEIGHT))
pause_image = pygame.transform.scale(pygame.image.load("images/pause.png"), (BTN_WIDTH, BTN_HEIGHT))
sound_image = pygame.transform.scale(pygame.image.load("images/sound.png"), (BTN_WIDTH, BTN_HEIGHT))

# 設定視窗
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

# set the title#繪圖視窗標題
pygame.display.set_caption("My first game")
# clock
clock = pygame.time.Clock()
#時間顯示宣告(進入遊戲時間)
start_time=time.time()
#時間字形大小宣告
font = pygame.font.Font(None, TIME_SIZE)

class Game:
    def __init__(self):
        # window
        # 將所有圖像庫輸入到class
        self.background=background_image
        self.enemy=enemy_image
        self.pause=pause_image
        self.continueplay=continue_image
        self.muse=muse_image
        self.sound=sound_image
        self.hp_pic=hp_image
        self.hp_gray_pic=hp_gray_image
        
        # 將所有血量值輸入到class(血量值可以從這邊做調整)
        # hp
        
        self.hp = 7
        self.max_hp = 10
        self.grayhp=self.max_hp-self.hp
        # 將所有時間顯示和時間輸入到class(時間顯示自行可以從參數化設定那邊做調整)
        self.start_time=start_time
        self.font = font
        

    def game_run(self):
        # game loop
        run = True
        while run:#無窮迴圈
            clock.tick(FPS)
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:#使用者按右上角的關閉鈕
                    run = False

           

            # draw background
            win.blit(self.background,(0,0))
            
            # draw enemy and health bar
            win.blit(self.enemy,(25,270))
            pygame.draw.rect(win, RED, [25, 260, 50, 5])
            # draw menu (and buttons)#使用參數化設定
            pygame.draw.rect(win, BLACK, [0, 0, WIN_WIDTH, 80])
            win.blit(self.pause,(WIN_WIDTH-BTN_WIDTH,0))
            win.blit(self.continueplay,(WIN_WIDTH-2*BTN_WIDTH,0))
            win.blit(self.sound,(WIN_WIDTH-3*BTN_WIDTH,0))
            win.blit(self.muse,(WIN_WIDTH-4*BTN_WIDTH,0))
            #使用參數化設定來定義hp，利用for
            for i in range(0,self.hp):
                win.blit(self.hp_pic,(420+(i%5)*HP_WIDTH,(i//5)*HP_HEIGHT))
            for i in range(0,self.grayhp):
                win.blit(self.hp_gray_pic,(580-(i%5)*HP_WIDTH,((9-i)//5)*HP_HEIGHT))
                    
              
               
            
            

            # draw time
            # 利用(現在時間時間-進入遊戲時間)來計算遊戲時間
            
            counting_time =int(time.time()-self.start_time)
            counting_minutes =int((counting_time/60)%60 )     #分的轉換，並使用int除去小數
            counting_seconds =int( (counting_time%60) )       #秒的轉換，並使用int除去小數
            #黑框
            pygame.draw.rect(win, BLACK, [0,560,60, 40])
            #輸出時間(轉成string後輸出並使秒數高位補0)
            text_surface = self.font.render(str(counting_minutes)+':'+str(counting_seconds).zfill(2) , True,WHITE,BLACK )
            
            win.blit(text_surface, (TIME_SIZE/2,WIN_HEIGHT-TIME_SIZE))

            pygame.display.update()#更新繪圖視窗

if __name__ == "__main__":
    covid_game = Game()
    covid_game.game_run()


pygame.quit()


# In[ ]:




