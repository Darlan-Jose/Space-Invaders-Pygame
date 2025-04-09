import os

script_path = os.path.dirname(os.path.abspath(__file__)) 
os.chdir(script_path)

import sys
import pygame
from projetil import Projetil
from alien import Alien
from time import sleep


def checar_eventos_keydown(evento, ai_configuracoes, tela, espaconave1, projeteis):
        '''
        Responde ao pressionamento de teclas
        '''
        if evento.key== pygame.K_d:
            espaconave1.mover_direita= True
        elif evento.key== pygame.K_a:
            espaconave1.mover_esquerda= True
        elif evento.key== pygame.K_SPACE:
             atirar_projetil(ai_configuracoes, tela, espaconave1, projeteis)
        elif evento.key== pygame.K_ESCAPE:
             sys.exit()
        

def checar_eventos_keyup(evento, espaconave1):
      '''
      Respode quando as teclas são soltas
      '''
      if evento.key== pygame.K_d:
        espaconave1.mover_direita= False
      elif evento.key== pygame.K_a:
        espaconave1.mover_esquerda= False
      
def checar_eventos(ai_configuracoes, tela, estatisticas, placar, botao_jogar, espaconave1, alienigenas, projeteis):
     '''
     Respode a eventos de pressionamento de tecla e de mouse
     '''
     for evento in pygame.event.get():
        if evento.type== pygame.QUIT:
            sys.exit()
        elif evento.type== pygame.KEYDOWN:
             checar_eventos_keydown(evento, ai_configuracoes, tela, espaconave1, projeteis)
        elif evento.type== pygame.KEYUP:
             checar_eventos_keyup(evento, espaconave1)
        elif evento.type== pygame.MOUSEBUTTONDOWN:
             mouse_x, mouse_y= pygame.mouse.get_pos() 
             checar_botao_jogar(ai_configuracoes, tela, estatisticas, placar, botao_jogar, espaconave1, alienigenas, projeteis, mouse_x, mouse_y)

def checar_botao_jogar(ai_configuracoes, tela, estatisticas, placar, botao_jogar, espaconave1, alienigenas, projeteis, mouse_x, mouse_y):
     '''
     Inicia um novo jogo quando o jogador clica em Jogar
     '''
     botao_clicado= botao_jogar.rect.collidepoint(mouse_x, mouse_y)                         
     if botao_clicado and not estatisticas.jogo_ativo:
          #Reinicia as configurações do jogo
          ai_configuracoes.iniciar_configuracoes_dinamicas()
          
          #Ocultar o cursos do mouse
          pygame.mouse.set_visible(False)
 
          #Reinicia os dados estatísticos do jogo
          estatisticas.reset_estatisticas()
          estatisticas.jogo_ativo= True
 
          #Reinicia as imagens do painel de pontuação
          placar.prep_images()
          
          #Esvazia a lista de alieníginas e projéteis
          alienigenas.empty()
          projeteis.empty()
 
          #Cria uma nova frota e centraliza a espaçonave
          criar_frota(ai_configuracoes, tela, espaconave1, alienigenas)
          espaconave1.centralizar_espaconave()
          

def atualizar_tela(ai_configuraçoes, tela, estatisticas, placar, espaconave1, alienigenas, projeteis, botao_jogar,creditos, imagem_fundo):
        '''
        Atualiza as imagens na tela e alterna para nova tela
        '''
        #Redesenha a tela a cada passagem pelo laço
        tela.fill(ai_configuraçoes.bg_cor)

        tela.blit(imagem_fundo, (0, 0))
        
        #Redesenha todos os projeteis atrás da espaçonave e dos alieníginas
        for projetil in projeteis.sprites():
             projetil.desenhar_projetil()
        espaconave1.blitme()
        alienigenas.draw(tela)

        #Desenha a informação sobre a pontuação e creditos
        placar.mostrar_pontuacao()
        

        #Desenha o botão jogar e os créditos se o jogo estiver inativo
        if not estatisticas.jogo_ativo:
             botao_jogar.desenhar_botao()
             creditos.mostrar_creditos()
        
        #Deixa a tela mais recente visível
        pygame.display.flip()

def atualizar_projeteis(ai_configuracoes, tela, estatisticas, placar, espaconave1 ,alienigenas, projeteis):
     '''
     Atualiza a posição de projeteis e se livra de projeteis antigos
     '''
     #Atualiza a posição dos projéteis
     projeteis.update()
     checar_projetil_alien_colisoes(ai_configuracoes, tela, estatisticas, placar, espaconave1 ,alienigenas, projeteis)
     deletar_projeteis_antigos(projeteis)
     comecar_novo_nivel(ai_configuracoes, tela, espaconave1, alienigenas, projeteis, estatisticas, placar)
 
def comecar_novo_nivel(ai_configuracoes, tela, espaconave1, alienigenas, projeteis, estatisticas, placar):
     if len(alienigenas) == 0: #Destrói os projéteis existentes,aumenta a velocidade do jogo e cria uma nova frota. Se a frota for destruída inicia um novo nivel
          projeteis.empty()   
          ai_configuracoes.aumentar_velocidade()
          
          #Aumenta o nível
          estatisticas.nivel+= 1
          placar.prep_nivel()
 
          criar_frota(ai_configuracoes, tela, espaconave1, alienigenas)

def deletar_projeteis_antigos(projeteis):
     for projetil in projeteis.copy():
          if projetil.rect.bottom <= 0:
               projeteis.remove(projetil)

def checar_projetil_alien_colisoes(ai_configuracoes, tela, estatisticas, placar, espaconave1 ,alienigenas, projeteis):
     '''
     Responde a colisões entre projéteis e alieníginas
     '''
     #Remove qualquer projétil e alienígina que tenha colidido
     colisoes= pygame.sprite.groupcollide(projeteis, alienigenas, True, True)

     if colisoes: 
          for aliens in colisoes.values():
               estatisticas.pontuacao+= ai_configuracoes.alien_pontos * len(aliens)
               placar.prep_pontuacao()
               checar_pontuacao_maxima(estatisticas, placar)
 

def comecar_novo_nivel(ai_configuracoes, tela, espaconave1, alienigenas, projeteis, estatisticas, placar):
     if len(alienigenas) == 0: #Destrói os projéteis existentes,aumenta a velocidade do jogo e cria uma nova frota. Se a frota for destruída inicia um novo nivel
          projeteis.empty()   
          ai_configuracoes.aumentar_velocidade()
          
          #Aumenta o nível
          estatisticas.nivel+= 1
          placar.prep_nivel()

          criar_frota(ai_configuracoes, tela, espaconave1, alienigenas)



def atirar_projetil(ai_configuracoes, tela, espaconave1, projeteis):
                  '''
                  Dispara um projetil se o limite ainda não foi alcançado
                  '''
                  #Cria um novo projétil e o adiocina a um novo grupo de projéteis
                  if len(projeteis) < ai_configuracoes.projeteis_permitidos:
                    novo_projetil= Projetil(ai_configuracoes, tela, espaconave1)
                    projeteis.add(novo_projetil)
                    

def obter_numero_aliens_x(ai_configuracoes, alien_largura):
     '''
     Determine o número de alieníginas que cabem em uma linha
     '''
     espaco_disponivel_x= ai_configuracoes.tela_largura - 2 * alien_largura
     numero_alienigenas_x= int(espaco_disponivel_x/(2 * alien_largura))

     return(numero_alienigenas_x)

def obter_num_linhas(ai_configuracoes, espaconave_altura, alien_altura):
     '''
     Determina o número de linhas de alieníginas que cabem na tela 
     '''
     espaco_disponivel_y= (ai_configuracoes.tela_altura - (3 * alien_altura) - espaconave_altura)
     num_linhas= int(espaco_disponivel_y / (2 * alien_altura))

     return(num_linhas)

def criar_alien(ai_configuracoes, tela, alienigenas, numero_alienigenas_x, num_linha):
     #Cria um alienígina e o posiciona na linha
     alien= Alien(ai_configuracoes, tela)
     alien_largura= alien.rect.width
     alien.x= alien_largura + 2 * alien_largura * numero_alienigenas_x
     alien.rect.x= alien.x
     alien.rect.y= alien.rect.height + 2 * alien.rect.height * num_linha
     alienigenas.add(alien)

def criar_frota(ai_configuracoes, tela, espaconave, alienigenas):
     '''
     Cria uma frota completa de alieníginas
     '''
     #Cria um alienígina e calcula o número de alieníginas que cabem em uma linha
     alien= Alien(ai_configuracoes, tela)
     numero_aliens= obter_numero_aliens_x(ai_configuracoes, alien.rect.width)
     num_linhas= obter_num_linhas(ai_configuracoes, espaconave.rect.height, alien.rect.height)

     #Cria a primeira linha de alieníginas
     for num_linha in range(num_linhas):
          for num_alien in range(numero_aliens):
               criar_alien(ai_configuracoes, tela, alienigenas, num_alien, num_linha)

def atualizar_aliens(ai_configuracoes, tela, estatisticas, placar, espaconave1, alienigenas, projeteis):
     '''
     Verifica se a frota está em uma das bordas e então atualiza as posições de todos os 
     alieníginas na tela.
     '''
     checar_frota_bordas(ai_configuracoes, alienigenas)
     alienigenas.update()

     #Verifica se houve colisões entre os alienígias e a espaçonave do jogador
     if pygame.sprite.spritecollideany(espaconave1, alienigenas):
          espaconave_atingida(ai_configuracoes, tela, estatisticas, placar, espaconave1, alienigenas, projeteis)

     #Verifica se algum alienígina atingiu a parte inferior da tela
     checar_aliens_inferior(ai_configuracoes, tela, estatisticas, placar, espaconave1, alienigenas, projeteis)


def checar_frota_bordas(ai_configuracoes, alienigenas):
     '''
     Responde apropriadamente se um alienígia alcançou alguma borda
     '''
     for alien in alienigenas.sprites():
          if alien.checar_bordas():
               alterar_frota_direcao(ai_configuracoes, alienigenas)
               break
                   
def alterar_frota_direcao(ai_configuracoes, alienigenas):
     '''
     Faz toda a froat descer e mudar de direção 
     '''
     for alien in alienigenas.sprites():
          alien.rect.y += ai_configuracoes.descer_frota_speed
     
     ai_configuracoes.frota_direcao *= -1

def espaconave_atingida(ai_configuracoes, tela, estatisticas, placar, espaconave1, alienigenas, projeteis):
     '''
     Responde ao fato de a espaçonave ter sido atiginda por uma alienígina
     '''
     #Decrementa espaconaves_sobrando
     if estatisticas.espaconaves_sobrando > 0: #Decrementa espaçonaves
          estatisticas.espaconaves_sobrando-= 1
          
          #Atualza o painel de pontuação
          placar.prep_espaconaves()
          
          #Esvazia a lista de alieníginas e de projéteis
          alienigenas.empty()
          projeteis.empty()

          #Cria uma nova frota e centraliza a espaçonave
          criar_frota(ai_configuracoes, tela, espaconave1, alienigenas)
          espaconave1.centralizar_espaconave()

          #Faz uma pausa
          sleep(0.5)
     else:
          estatisticas.jogo_ativo= False
          pygame.mouse.set_visible(True)

def checar_aliens_inferior(ai_configuracoes, tela, estatisticas, placar, espaconave1, alienigenas, projeteis):
     '''
     Verifica se algum alienígina alcançou a parte inferior da tela
     '''
     tela_rect= tela.get_rect()
     
     for alien in alienigenas.sprites():
          if alien.rect.bottom >= tela_rect.bottom: #Trata da mesma forma quando a espaçonave é atingida
               espaconave_atingida(ai_configuracoes, tela, estatisticas, placar, espaconave1, alienigenas, projeteis)
               break

def checar_pontuacao_maxima(estatisticas, placar):
     '''
     Verifica se há uma nova pontuação máxima
     '''
     if estatisticas.pontuacao > estatisticas.pontuacao_maxima:
          estatisticas.pontuacao_maxima= estatisticas.pontuacao
          placar.prep_pontuacao_maxima()
 
          #Armazena a pontuação máxima em um arquivo externo
          local= 'pontuacaomaxima_reg.txt'
          with open(local, 'w') as arquivo_objeto:
               arquivo_objeto.write(str(estatisticas.pontuacao_maxima))

