import pygame.font
from pygame.sprite import Group
from espaconave import Espaconave

class Placar():
    '''
    Uma classe para mostrar informações sobre a pontuação
    '''
    def __init__(self, ai_configuracoes, tela, estatisticas):
        '''
        Inicializa os atributos da pontuação
        '''
        self.tela= tela
        self.tela_rect= tela.get_rect()
        self.ai_configuracoes= ai_configuracoes
        self.estatisticas= estatisticas
 
        #Configurações de fonte para as informações da pontuação
        self.texto_cor= (255, 255, 255)
        self.fonte= pygame.font.SysFont(None, 48)
 
        self.prep_images()
 
    def prep_images(self):
        #Prepara a imagem da pontuação inicial
        self.prep_pontuacao()
        self.prep_pontuacao_maxima()
        self.prep_nivel()
        self.prep_espaconaves()

    def prep_pontuacao(self):
        '''
        Tranforma a pontuação em uma imagem renderizada
        '''
        pontuacao_arredondada= int(round(self.estatisticas.pontuacao, -1))
        pontuacao_str= "{:,}".format(pontuacao_arredondada)
        self.pontuacao_image= self.fonte.render(pontuacao_str, True, self.texto_cor, self.ai_configuracoes.bg_cor)

        #Exibe a pontuação na parte superior direita da tela
        self.pontuacao_rect= self.pontuacao_image.get_rect()
        self.pontuacao_rect.right= self.tela_rect.right - 20
        self.pontuacao_rect.top= 20

    def mostrar_pontuacao(self):
        '''
        Desenha a pontuação na tela
        '''
        self.tela.blit(self.pontuacao_image, self.pontuacao_rect)
        self.tela.blit(self.pontuacao_maxima_image, self.pontuacao_maxima_rect)
        self.tela.blit(self.nivel_image, self.nivel_rect)

        #Desenha as espaçonaves
        self.espaconaves.draw(self.tela)

    def prep_pontuacao_maxima(self):
        '''
        Transforma a pontuação máxima em uma imagem renderizada
        '''
        pontuacao_maxima= int(round(self.estatisticas.pontuacao_maxima, -1))
        pontuacao_maxima_str= "{:,}".format(pontuacao_maxima)
        self.pontuacao_maxima_image= self.fonte.render(pontuacao_maxima_str, True, self.texto_cor, self.ai_configuracoes.bg_cor)

        #Centraliza a pontuação máxima na parte superior da tela
        self.pontuacao_maxima_rect= self.pontuacao_maxima_image.get_rect()
        self.pontuacao_maxima_rect.centerx= self.tela_rect.centerx
        self.pontuacao_maxima_rect.top= self.pontuacao_rect.top

    def prep_nivel(self):
        '''
        Transforma o nível em uma imagem renderizada
        '''
        self.nivel_image= self.fonte.render(str(self.estatisticas.nivel), True, self.texto_cor, self.ai_configuracoes.bg_cor)

        #Posiciona o nível abaixo da pontuação
        self.nivel_rect= self.nivel_image.get_rect()
        self.nivel_rect.right= self.pontuacao_rect.right
        self.nivel_rect.top= self.pontuacao_rect.bottom + 10

    def prep_espaconaves(self):
        '''
        Mostrar quantas espaçonaves restam
        '''
        self.espaconaves= Group()

        for num_espaconave in range(self.estatisticas.espaconaves_sobrando):
            espaconave= Espaconave(self.ai_configuracoes, self.tela)
            espaconave.rect.x= 10 + num_espaconave * espaconave.rect.width
            espaconave.rect.y= 10
            self.espaconaves.add(espaconave)



class Creditos():
    '''
    Escrever depois
    '''
    def __init__(self, ai_configuracoes, tela, estatisticas):
        '''
        Inicializa os atributos da pontuação
        '''
        self.tela= tela
        self.tela_rect= tela.get_rect()
        self.ai_configuracoes= ai_configuracoes
        self.estatisticas= estatisticas
 
        #Configurações de fonte para as informações da pontuação
        self.texto_cor= (255, 255, 255)
        self.fonte= pygame.font.SysFont(None, 25)
 
        self.prep_images()

    def prep_images(self):
        #Prepara a imagem da pontuação inicial
        self.prep_creditos()

    def mostrar_creditos(self):
        '''
        Desenha a pontuação na tela
        '''
        self.tela.blit(self.creditos_image, self.creditos_rect)
        self.tela.blit(self.creditos_image2, self.creditos_rect2)
        self.tela.blit(self.creditos_image3, self.creditos_rect3)

    def prep_creditos(self):
        '''
        Mostra os créditos dos autores das artes/imagens
        '''
        msg0= "Assets by:"
        msg= "Stephen Challener (Redshrike), hosted by OpenGameArt.org"
        msg2= "'Spaceships 32x32' by Irmandito licensed CC-BY 3.0: https://opengameart.org/content/spaceships-32x32"
        
        self.creditos_image= self.fonte.render(msg, True, self.texto_cor, self.ai_configuracoes.bg_cor)

        self.creditos_rect= self.creditos_image.get_rect()
        self.creditos_rect.right= self.tela_rect.right - 20
        self.creditos_rect.top= 600

        self.creditos_image2= self.fonte.render(msg2, True, self.texto_cor, self.ai_configuracoes.bg_cor)

        self.creditos_rect2= self.creditos_image2.get_rect()
        self.creditos_rect2.right= self.tela_rect.right - 20
        self.creditos_rect2.top= 630

        self.creditos_image3= self.fonte.render(msg0, True, self.texto_cor, self.ai_configuracoes.bg_cor)

        self.creditos_rect3= self.creditos_image3.get_rect()
        self.creditos_rect3.right= self.tela_rect.right - 20
        self.creditos_rect3.top= 580




