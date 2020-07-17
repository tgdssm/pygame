import pygame
pygame.init()

screen = pygame.display.set_mode([300, 300]) # Configura o tamanho da tela

running = True
while running: # Executa até que o eu queira sair
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    screen.fill((255, 255, 255)) # Configura a cor da tela 

    # Desenha um circulo na tela
    # O primeiro argumento é a tela onde será feito o desenho
    # O segundo é a cor do circulo
    # O terceiro a posição e o quarto o tamanho do circulo
    pygame.draw.circle(screen, (102, 0, 0), (150, 150), 75)

    # Atualiza o conteúdo da exibição na tela. Sem isso nada aparece na janela
    pygame.display.flip() 

pygame.quit()