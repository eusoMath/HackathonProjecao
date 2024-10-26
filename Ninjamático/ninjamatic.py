import pygame
from pygame.locals import *
from sys import exit
import random

pygame.init()

largura = 640
altura = 480
x_ninja = 100
y_ninja = 300
jumping = False
jump_height = 120
current_jump = 0
gravity = 2
target_x = 580
pontuacao = 0

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Ninjamatic')
relogio = pygame.time.Clock()

casa = pygame.image.load('assets/casa.png')
casa_redimensionada = pygame.transform.scale(casa, (280, 280))
ninja_pulando = pygame.image.load('assets/pulando.png')
ninja_caindo = pygame.image.load('assets/caindo.png')

pergunta = "Quanto é 2 + 2?"
respostas = [4, 3, 5]
resposta_correta = 4
random.shuffle(respostas)

def desenhar_texto(texto, tamanho, cor, pos):
    fonte = pygame.font.Font(None, tamanho)
    superficie = fonte.render(texto, True, cor)
    tela.blit(superficie, pos)

casa1_x = -80
casa2_x = 420
mensagem = ""

while True:
    relogio.tick(30)
    
    tela.fill((50, 50, 150))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == MOUSEBUTTONDOWN and not jumping:
            mouse_x, mouse_y = event.pos
            if 50 < mouse_x < 200 and 100 < mouse_y < 150:
                if respostas[0] == resposta_correta:
                    jumping = True
                    current_jump = 0
                    pontuacao += 1
                    mensagem = "Você venceu!!"
                else:
                    mensagem = "Você perdeu!"
            elif 50 < mouse_x < 200 and 160 < mouse_y < 210:
                if respostas[1] == resposta_correta:
                    jumping = True
                    current_jump = 0
                    pontuacao += 1
                    mensagem = "Você venceu!!"
                else:
                    mensagem = "Você perdeu!"
            elif 50 < mouse_x < 200 and 220 < mouse_y < 270:
                if respostas[2] == resposta_correta:
                    jumping = True
                    current_jump = 0
                    pontuacao += 1
                    mensagem = "Você venceu!!"
                else:
                    mensagem = "Você perdeu!"

    if jumping:
        if x_ninja < target_x:
            x_ninja += 12
            
        current_jump += gravity
        y_ninja = 300 - current_jump

        if current_jump >= jump_height:
            current_jump = jump_height

        if x_ninja >= target_x:
            x_ninja = target_x
            jumping = False
            y_ninja = 300
            mensagem = ""

    tela.blit(casa_redimensionada, (casa1_x, 200))
    tela.blit(casa_redimensionada, (casa2_x, 200))

    if jumping:
        tela.blit(ninja_pulando, (x_ninja, y_ninja))
    else:
        tela.blit(ninja_caindo, (x_ninja, y_ninja))

    desenhar_texto(pergunta, 36, (255, 255, 255), (50, 30))
    for i, resposta in enumerate(respostas):
        letra = chr(65 + i)
        desenhar_texto(f"{letra}: {resposta}", 36, (255, 255, 255), (50, 100 + (i * 60)))

    desenhar_texto(f"Pontos: {pontuacao}", 36, (255, 255, 255), (largura - 150, 30))

    if mensagem:
        cor = (0, 255, 0) if "venceu" in mensagem else (255, 0, 0)
        largura_mensagem = len(mensagem) * 18
        desenhar_texto(mensagem, 36, cor, ((largura - largura_mensagem) // 2, altura // 2))

    pygame.display.update()
