import random
import pygame

class Comida:

    def __init__(self, tamanho, largura, altura):
        self.tamanho = tamanho
        self.largura = largura
        self.altura = altura
        self.posicao = [random.randint(0, (largura - 1) // tamanho) * tamanho, 
              random.randint(0, (altura - 1) // tamanho) * tamanho]
    
    def desenhar(self, screen, cor):
        pygame.draw.rect(screen, cor, [self.posicao[0], self.posicao[1], self.tamanho, self.tamanho])

    def spawn(self):
        self.posicao = [random.randint(0, (self.largura - 1) // self.tamanho) * self.tamanho, 
              random.randint(0, (self.altura - 1) // self.tamanho) * self.tamanho]