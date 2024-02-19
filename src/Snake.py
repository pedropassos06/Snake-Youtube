import pygame
from enum import Enum

class Deslocamento(Enum):
    TAMANHO = 50
    CIMA = [0, -TAMANHO]
    BAIXO = [0, TAMANHO]
    ESQUERDA = [-TAMANHO, 0]
    DIREITA = [TAMANHO, 0]

class Snake:

    def __init__(self, tamanho, velocidade, largura, altura):
        self.tamanho = tamanho
        self.velocidade = velocidade
        self.largura = largura
        self.altura = altura
        self.comprimento = 1
        self.posicao = [largura // 2, altura // 2]
        self.corpo = [self.posicao]
        self.cabeca = [self.posicao[0], self.posicao[1]]
        self.deslocamento = [0, 0]

    def aumentar(self):
        self.comprimento += 1
    
    def desenhar(self, screen, cor):
        for bloco in self.corpo:
            pygame.draw.rect(screen, cor, [bloco[0], bloco[1], self.tamanho, self.tamanho])
        
        if len(self.corpo) > self.comprimento:
            del self.corpo[0]

    def update_deslocamento(self, event):
        if event.key == pygame.K_UP:
            self.deslocamento = Deslocamento.CIMA.value
        elif event.key == pygame.K_DOWN:
            self.deslocamento = Deslocamento.BAIXO.value
        elif event.key == pygame.K_LEFT:
            self.deslocamento = Deslocamento.ESQUERDA.value
        elif event.key == pygame.K_RIGHT:
            self.deslocamento = Deslocamento.DIREITA.value
        return self.deslocamento

    def mover(self):
        self.posicao[0] += self.deslocamento[0]
        self.posicao[1] += self.deslocamento[1]
        self.cabeca = [self.posicao[0], self.posicao[1]]
        self.corpo.append(self.cabeca)

    def checar_colisao(self, running):
        for bloco in self.corpo[:-1]:
            if self.cabeca == bloco:
                running = False
    
        if self.cabeca[0] < 0 or self.cabeca[0] > self.largura or self.cabeca[1] > self.altura or self.cabeca[1] < 0:
            running = False
        
        return running