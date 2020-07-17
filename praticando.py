import pygame
from random import randint
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)
# Definindo constantes para o tamanho da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player(pygame.sprite.Sprite):
        def __init__(self):
            super(Player, self).__init__()

            # Crie uma superfície e passa uma tupla com seu comprimento e largura
            self.surf = pygame.Surface((75, 25))

            # Dando cor a surface
            self.surf.fill((255, 255, 255))

            # Armazena os valores de 'surf' em 'rect' para uso posterior
            self.rect = self.surf.get_rect()


        def  update(self, pressed_keys):
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 5)
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

            # Manter o jogador na tela
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > SCREEN_WIDTH: 
                self.rect.right = SCREEN_WIDTH
            if self.rect.top < 0:
                self.rect.top = 0
            if self.rect.bottom >= SCREEN_HEIGHT:
                self.rect.bottom = SCREEN_HEIGHT

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center = (
                randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = randint(5, 20)

    
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

pygame.init()

# Criando a tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

ADDENEMY =  pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

player = Player()

enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Loop principal do jogo, verifica as entradas do úsuario
running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN: # Verifica se o úsuario apertou alguma tecla
            if event.key == K_ESCAPE: # Se a tecla de ESC for pressionada pare o loop
                running = False
        elif event.type == pygame.QUIT: # Verifica se a janela foi fechada
            running = False
        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

    pressed_keys = pygame.key.get_pressed() # retorna um dicionario com todas as
    # teclas pressionadas no inicio de cada quadro

    player.update(pressed_keys)

    enemies.update()

    screen.fill((0, 0, 0)) # Apreenchendo o funco com a cor branca

    # surf_center = (
    #     (SCREEN_WIDTH - surf.get_width())/2,
    #     (SCREEN_HEIGHT - surf.get_height())/2
    # )

    clock = pygame.time.Clock()
    # Copia a surface 'surf' para a outra surface 'screen' e como segundo
    # argumento é passado a posição de 'surf' na tela
    # screen.blit(player.surf, player.rect)

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    
    # Detectando colisões
    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()
        running = False

    pygame.display.flip() # Atualiza os dados na tela
    clock.tick(30)

     





