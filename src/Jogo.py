import pygame
from Snake import Snake
from Comida import Comida
from enum import Enum

class Cores(Enum):
    PRETO = (0, 0, 0)
    VERDE = (0, 255, 0)
    VERMELHO = (255, 0, 0)

def setup_pygame(largura, altura):
    pygame.init()
    screen = pygame.display.set_mode((largura, altura))
    clock = pygame.time.Clock()
    return screen, clock

def handle_events(running, snake):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            snake.update_deslocamento(event)
    return running

def limpar_tela(screen):
    screen.fill(Cores.PRETO.value)


def main_loop(screen, clock, snake, comida):
    running = True
    while running:
    
        running = handle_events(snake, running)

        limpar_tela(screen)

        snake.mover()
        snake.desenhar(screen, Cores.VERDE.value)
        comida.desenhar(screen, Cores.VERMELHO.value)
        running = snake.checar_colisao(running)

        if snake.cabeca == comida.posicao:
            snake.aumentar()
            comida.spawn()

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(snake.velocidade)  # limits FPS to 60

    pygame.quit()


if __name__ == "__main__":
    LARGURA, ALTURA = 800, 600
    TAMANHO = 50
    VELOCIDADE = 10
    screen, clock = setup_pygame(800, 600)
    snake = Snake(TAMANHO, VELOCIDADE, LARGURA, ALTURA)
    comida = Comida(TAMANHO, LARGURA, ALTURA)
    main_loop(screen, clock, snake, comida)
