import os

script_path = os.path.dirname(os.path.abspath(__file__)) 
os.chdir(script_path)

class JogoEstatisticas():
    '''
    Armazena dados estatísticos da invasão alienígena
    '''
    def __init__(self, ai_configuracoes):
        '''
        Inicializa os dados estatísticos
        '''
        self.ai_configuracoes= ai_configuracoes
        self.reset_estatisticas()

        #Inicia a invasão alienígena em um estado ativo
        self.jogo_ativo= False

        #Le a pontuação máxima de um arquivo externo e passa esse valor para a pontuação máxima do jogo
        local= 'pontuacaomaxima_reg.txt'
        with open(local, 'r') as arquivo_objeto:
               conteudo= arquivo_objeto.read()
               conteudo= int(conteudo)

        #A pontuação máxima não pode ser reiniciada
        self.pontuacao_maxima= conteudo


    def reset_estatisticas(self):
        '''
        Inicializa os dados estatísticos que podem mudar durante o jogo
        '''
        self.espaconaves_sobrando= self.ai_configuracoes.espaconave_limite
        self.pontuacao= 0
        self.nivel= 1