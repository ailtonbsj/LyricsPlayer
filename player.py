# -*- coding: utf-8 -*-

from lyricsfile import *
import pygame, time
import pygame.mixer
nome = 'asserts/sexonfire' 
letra = capturarLetra(nome+'.lrc')

RED = (255,0,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)
pygame.init()
screen = pygame.display.list_modes()[0]
WIDTHSCREEN = screen[0]
HEIGHTSCREEN = int(screen[1]*0.2)
CENTER_Y = HEIGHTSCREEN/2
CENTER_X = WIDTHSCREEN/2

TELA = pygame.display.set_mode((WIDTHSCREEN,HEIGHTSCREEN),0,0)
FONTE = pygame.font.Font("font.ttf",42)
pygame.display.set_caption('LyricPlayer by José Ailton')

letraTime = {}
music = pygame.mixer.music
music.load(nome+'.mp3')
music.play()

for i in letra.keys():
    imgFont = FONTE.render(letra[i], True,BLACK)
    s = timeTosecond(i)
    letraTime[s]=(imgFont,imgFont.get_rect()[2]/2)
posAtual = 0
while True:
    y=0
    for event in pygame.event.get():
        if event.type == pygame.QUIT: break
    TELA.fill(WHITE)
    
    posAtual = (music.get_pos())
    
    for i in letraTime.keys():
        y = -0.015*(posAtual-i)+CENTER_Y
        TELA.blit(letraTime[i][0],(CENTER_X-letraTime[i][1],y))
    
    pygame.display.flip()
    pygame.display.update()
    time.sleep(0.01)
exit()