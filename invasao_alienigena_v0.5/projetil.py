import pygame 
from pygame.sprite import Sprite

class Projetil(Sprite):
    '''
    Uma classe que administra projéteis disparados pela espaçonave
    '''
    def __init__(self, ai_configuracoes, tela, espaconave1):
        '''
        Cria um objeto para o projétil na posição atual da espaçonave
        '''
        super(Projetil, self).__init__()
        self.tela= tela

        #Cria um retângulo para o projetil em 0, 0 e
        #em seguida define a posição correta
        self.rect= pygame.Rect(0, 0,ai_configuracoes.projetil_largura, ai_configuracoes.projetil_altura)
        self.rect.centerx= espaconave1.rect.centerx
        self.rect.top= espaconave1.rect.top

        #Armazena a posição do projétil como um valor decimal 
        self.y= float(self.rect.y)
        
        self.cor= ai_configuracoes.projetil_cor
        self.speed_factor= ai_configuracoes.projetil_speed_factor

    def update(self):
        '''
        Move o projétil para cima na tela
        '''
        #Atualiza a posição decimal do projétil
        self.y-= self.speed_factor

        #Atualiza a posição de rect
        self.rect.y= self.y

    def desenhar_projetil(self):
        '''
        Desenha o projétil na tela
        '''
        pygame.draw.rect(self.tela, self.cor, self.rect)
