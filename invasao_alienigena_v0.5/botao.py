import pygame.font

class Botao():
    def __init__(self, ai_configuracoes, tela, msg):
        '''
        Inicializa os atributos do botão
        '''
        self.tela= tela
        self.tela_rect= tela.get_rect()

        #Define as dimensões e propridades do botão
        self.largura, self.altura= 200, 50
        self.botao_cor= (0, 144, 0)
        self.texto_cor= (255, 255, 255)
        self.font= pygame.font.SysFont(None, 48)

        #Constroi o objeto rect do botão e o centraliza
        self.rect= pygame.Rect(0, 0, self.largura, self.altura)
        self.rect.center= self.tela_rect.center

        #A mensagem do botão deve ser preparada apenas uma vez
        self.preparar_msg(msg)

    def preparar_msg(self, msg):
        '''
        Transforma msgm em imagem e centraliza o texto no botao
        '''
        self.msg_image= self.font.render(msg, True, self.texto_cor, self.botao_cor)
        self.msg_image_rect= self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center

    def desenhar_botao(self):
        #Desenha um botão em branco, e em seguida desenha a mensagem
        self.tela.fill(self.botao_cor, self.rect)
        self.tela.blit(self.msg_image, self.msg_image_rect)



