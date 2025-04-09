import pygame
from pygame.sprite import Sprite

class Espaconave(Sprite):
    def __init__(self, ai_configuracoes, tela):
        '''
        Inicializa a espaçonave e define a sua posição inicial
        '''
        super(Espaconave, self).__init__()

        self.tela= tela
        self.ai_configuracoes= ai_configuracoes
        #Carrega a imagem da espaçonave e obtém o seu rect
        self.image= pygame.image.load('images/ship_3.bmp')
        self.rect= self.image.get_rect()
        self.tela_rect= tela.get_rect()

        #Inicia a espaçonave na parte inferior central da tela
        self.rect.centerx= self.tela_rect.centerx
        self.rect.bottom= self.tela_rect.bottom

        #Armazena um valor decimal para o centro da espaçonave
        self.center= float(self.rect.centerx)

        #Flag de movimento
        self.mover_direita= False
        self.mover_esquerda= False

    def blitme(self):
        '''
        Desenha a espaçonave na sua posição atual
        '''
        self.tela.blit(self.image, self.rect)

    def atualizar(self):
        '''
        Atualiza a posição da espaçonave com base nas flags de movimentos
        '''
        #Atualiza o centro da espaconave e não o retângulo
        if self.mover_direita and (self.rect.right < self.tela_rect.right):
            self.center+= self.ai_configuracoes.espaconave1_velocidade_fator
        
        if self.mover_esquerda and (self.rect.left > 0):
            self.center-= self.ai_configuracoes.espaconave1_velocidade_fator

        #Atualiza o objeto rect de acordo com self.center
        self.rect.centerx= self.center

    def centralizar_espaconave(self):
        '''
        Centraliza a espaçonave na tela
        '''
        self.center= self.tela_rect.centerx
        
