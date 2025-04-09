import os

script_path = os.path.dirname(os.path.abspath(__file__)) 
os.chdir(script_path)

import pygame
from configuracoes import Configuraçoes
from espaconave import Espaconave
import funcoes_jogo as fj
from pygame.sprite import Group
from jogo_stats import JogoEstatisticas
from botao import Botao
from placar import Placar
from placar import Creditos

def rodar_jogo():
    #Inicializa o pygame, configurações o objeto tela
    pygame.init()
    ai_configuracoes= Configuraçoes()
    tela= pygame.display.set_mode((ai_configuracoes.tela_largura, ai_configuracoes.tela_altura))

    pygame.display.set_caption("Jogo Alien Invasion")

    win_icon= pygame.image.load('images/Ship_3.bmp')
    pygame.display.set_icon(win_icon)

    #Imagem de fundo
    imagem_fundo= pygame.image.load('images/background.bmp')

    #Cria o botão jogar
    botao_jogar= Botao(ai_configuracoes, tela, "Jogar")

    #Cria uma instância para armazenar dados estastístiscos do jogo e cria o painel de pontuacão
    estatisticas= JogoEstatisticas(ai_configuracoes)
    placar= Placar(ai_configuracoes, tela, estatisticas)
    creditos= Creditos(ai_configuracoes, tela, estatisticas)

    #Cria uma espaçonave
    espaconave1= Espaconave(ai_configuracoes, tela)

    #Cria um grupo no qual serão armazenado os projeteis e um grupo de alienigenas 
    projeteis = Group()
    alienigenas = Group()

    #Cria uma frota de alieníginas
    fj.criar_frota(ai_configuracoes, tela, espaconave1, alienigenas)


    #Inicializa o laço principal do jogo
    while True:
        fj.checar_eventos(ai_configuracoes, tela, estatisticas, placar, botao_jogar, espaconave1, alienigenas, projeteis)
        
        if estatisticas.jogo_ativo:
            espaconave1.atualizar()
            fj.atualizar_projeteis(ai_configuracoes, tela, estatisticas, placar, espaconave1 ,alienigenas, projeteis)
            fj.atualizar_aliens(ai_configuracoes, tela, estatisticas, placar, espaconave1, alienigenas, projeteis)
        
        fj.atualizar_tela(ai_configuracoes, tela, estatisticas, placar, espaconave1, alienigenas, projeteis, botao_jogar, creditos, imagem_fundo)

rodar_jogo()
