class Configuraçoes():
    '''
    Inicializa as configuracões estáticas do jogo
    '''
    def __init__(self):
        #Configurações da tela
        self.tela_largura= 1281
        self.tela_altura=721
        self.bg_cor=(5, 7, 25)

        #Configuração da espaçonave
        self.espaconave_limite= 3

        #Configuração de projéteis
        self.projetil_largura= 3
        self.projetil_altura= 15
        self.projetil_cor= 255, 100, 0
        self.projeteis_permitidos= 5

        #Configurações dos alienígenas
        self.descer_frota_speed= 15

        #frota_direcao= 1 representa a direta; -1 representa a esquerda
        self.frota_direcao= 1

        #A taxa com que a velocidade do jogo aumenta
        self.escala_speedup= 1.1
        #A taxa com que os pontos para cada alienígena aumentam
        self.escala_pontuacao= 1.5

        self.iniciar_configuracoes_dinamicas()

    def iniciar_configuracoes_dinamicas(self):
        '''
        Inicializa as configurações que mudam ao decorrer do jogo 
        '''
        self.espaconave1_velocidade_fator= 2
        self.projetil_speed_factor= 3
        self.alien_speed_factor= 1
        #frota_direcao= 1 representa a direta; -1 representa a esquerda
        self.frota_direcao= 1

        #Pontuação
        self.alien_pontos= 10

    def aumentar_velocidade(self):
        '''
        Aumenta as configurações de velocidade 
        '''
        self.espaconave1_velocidade_fator*= self.escala_speedup
        self.alien_pontos= int(self.alien_pontos * self.escala_pontuacao)
        self.projetil_speed_factor*= self.escala_speedup
        self.alien_speed_factor*= self.escala_speedup

        

        



        