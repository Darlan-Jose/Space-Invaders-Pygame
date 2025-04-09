import os

script_path = os.path.dirname(os.path.abspath(__file__)) 
os.chdir(script_path)

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''
    Uma classe que representam um único alienígina de uma frota
    '''

    def __init__(self, ai_configuracoes, tela):
        '''
        Inicializa o alienígina e define a sua posição inicial
        '''
        super(Alien, self).__init__()
        self.tela= tela
        self.ai_configuracoes= ai_configuracoes

        #Carrega a imagem do alienígina e define o seu atributo rect
        self.image= pygame.image.load('images/alien1.bmp')
        self.rect= self.image.get_rect()

        #Inicia cada alienígina próximo a parte superior a esquerda da tela
        self.rect.x= self.rect.width
        self.rect.y= self.rect.height

        #Armazena a posição exata do alienígina
        self.x= float(self.rect.x)
    
    def blitme(self):
        '''
        Desenha o alienígina na sua posição atual
        '''
        self.tela.blit(self.image, self.rect)

    def update(self):
        '''
        Move o alienígina para a direta ou esquerda
        '''
        self.x+= (self.ai_configuracoes.alien_speed_factor * self.ai_configuracoes.frota_direcao)
        self.rect.x= self.x

    def checar_bordas(self):
        '''
        Devolve True se o alienigena estiver na borda da tela 
        '''
        tela_rect= self.tela.get_rect()

        if self.rect.right >= tela_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        

