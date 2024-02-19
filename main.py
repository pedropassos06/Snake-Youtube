"""
1. Setup (pronto)
2. Partir para os movimentos: movimentar a snake (pronto)
3. Tentar aumentar comprimento da snake (pronto)
4. Reiniciar jogo 
"""
# Example file showing a basic pygame "game loop"
import pygame
import random

# pygame setup
pygame.init()
largura, altura = 800, 600
screen = pygame.display.set_mode((largura, altura))
clock = pygame.time.Clock()
running = True

# cores
PRETO = (0, 0, 0)
VERDE = (0, 255, 0) #RGB
VERMELHO = (255, 0, 0)

# tamanho comida e cobra
TAMANHO = 50

# cobra
velocidade = 10
comprimento_cobra = 1
corpo_cobra = []
cabeca_cobra = []

# init comida
pos_comida = [random.randint(0, largura // TAMANHO) * TAMANHO, 
              random.randint(0, altura // TAMANHO) * TAMANHO]
pos_cobra = [largura//2, altura//2]

# deslocamento cobra
deslocamento_x = 0
deslocamento_y = 0

# desenhar cobra
def desenhar_cobra(corpo):
    for bloco in corpo:
        pygame.draw.rect(screen, VERDE, [bloco[0], bloco[1], TAMANHO, TAMANHO])

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                deslocamento_x = 0
                deslocamento_y = -TAMANHO
            elif event.key == pygame.K_DOWN:
                deslocamento_x = 0
                deslocamento_y = TAMANHO
            elif event.key == pygame.K_LEFT:
                deslocamento_x = -TAMANHO
                deslocamento_y = 0
            elif event.key == pygame.K_RIGHT:
                deslocamento_x = TAMANHO
                deslocamento_y = 0

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    desenhar_cobra(corpo_cobra)
    pygame.draw.rect(screen, VERMELHO, [pos_comida[0], pos_comida[1], TAMANHO, TAMANHO])

    pos_cobra[0] += deslocamento_x
    pos_cobra[1] += deslocamento_y
    cabeca_cobra = [pos_cobra[0], pos_cobra[1]]
    corpo_cobra.append(cabeca_cobra)

    if len(corpo_cobra) > comprimento_cobra:
        del corpo_cobra[0]

    for bloco in corpo_cobra[:-1]:
        if cabeca_cobra == bloco:
            running = False
    
    if cabeca_cobra[0] < 0 or cabeca_cobra[0] > largura or cabeca_cobra[1] > altura or cabeca_cobra[1] < 0:
        running = False

    if cabeca_cobra == pos_comida:
        comprimento_cobra += 1
        pos_comida = [random.randint(0, largura // TAMANHO) * TAMANHO, 
              random.randint(0, altura // TAMANHO) * TAMANHO]

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(velocidade)  # limits FPS to 60

pygame.quit()