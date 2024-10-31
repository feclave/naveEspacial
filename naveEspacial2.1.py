import pygame
import random
import os

# Inicialização do Pygame
pygame.init()

# Caminho base para imagens
base_path = os.path.dirname(__file__)

# Dimensões da tela
largura_tela = 1920
altura_tela = 1080
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Asteroids")

# Cores
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)

# Carregar e redimensionar a imagem de fundo
background = pygame.image.load(os.path.join(base_path, "background.png")).convert()
background = pygame.transform.scale(background, (largura_tela, altura_tela))  # Redimensiona o fundo
background_x = 0
background_y = 0
background2_y = -altura_tela  # Coloca a segunda imagem logo acima da primeira

# Carregar imagem do coração
coracao_img = pygame.image.load(os.path.join(base_path, "coracao.png")).convert_alpha()
coracao_img = pygame.transform.scale(coracao_img, (30, 30))

# Variável global para a pontuação
pontuacao = 0

class NaveEspacial(pygame.sprite.Sprite):
    def __init__(self, name, image_path, initial_position):
        super().__init__()
        self.direction = 0
        self.name = name
        self.image = pygame.image.load(image_path).convert_alpha()
        self.original_image = self.image
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(center=initial_position)
        self.hitbox = pygame.Rect(self.rect.x + 4, self.rect.y + 4, 70, 70)
        self.speed = 5
        self.shield = 100
        self.energy = 100
        self.alive = True
        self.distance_travelled = 0
        self.coracoes = 5

    def update(self):
        if self.alive:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.rect.x -= self.speed
            if keys[pygame.K_RIGHT]:
                self.rect.x += self.speed
            self.distance_travelled += self.speed
            self.rect.clamp_ip(pygame.Rect(0, 0, largura_tela, altura_tela))
            self.hitbox.topleft = (self.rect.x + 5, self.rect.y + 5)
            rotated_image = pygame.transform.rotate(self.original_image, -self.direction)
            rotated_rect = rotated_image.get_rect(center=self.rect.center)
            self.image, self.rect = rotated_image, rotated_rect

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def atirar(self):
        tiro = Tiro(self.rect.centerx, self.rect.top)
        tiros.add(tiro)
        todos_sprites.add(tiro)

class Asteroide(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(os.path.join(base_path, "asteroide.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        self.rect.y += 3
        if self.rect.top > altura_tela:
            self.kill()

class Tiro(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(branco)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 10

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()

def desenhar_coracoes(screen, coracoes):
    for i in range(coracoes):
        screen.blit(coracao_img, (largura_tela - 40 - (i * 35), 10))  # Desenha corações usando a imagem

# Grupos de sprites
todos_sprites = pygame.sprite.Group()
asteroides = pygame.sprite.Group()
tiros = pygame.sprite.Group()

# Criar a nave
nave = NaveEspacial("Nave", os.path.join(base_path, "nave.png"), (largura_tela // 2, altura_tela - 50))
todos_sprites.add(nave)

# Função para gerar asteroides
def gerar_asteroides():
    for _ in range(5):
        x = random.randint(0, largura_tela - 30)
        y = random.randint(-100, -40)
        if not nave.hitbox.colliderect(pygame.Rect(x, y, 30, 30)):
            asteroide = Asteroide(x, y)
            asteroides.add(asteroide)
            todos_sprites.add(asteroide)

# Função para verificar colisões
def verificar_colisoes():
    global pontuacao
    colisoes = [asteroide for asteroide in asteroides if nave.hitbox.colliderect(asteroide.rect)]
    for asteroide in colisoes:
        nave.coracoes -= 1
        asteroide.kill()
        if nave.coracoes <= 0 and nave.alive:
            nave.alive = False
            # Remove todos os asteroides e tiros
            asteroides.empty()
            tiros.empty()
            break
    pygame.sprite.groupcollide(asteroides, tiros, True, True)

# Função para desenhar pontuação
def desenhar_pontuacao():
    global pontuacao
    pontuacao = nave.distance_travelled // 10
    font = pygame.font.Font(None, 36)
    texto = font.render("Pontuação: " + str(pontuacao), True, branco)
    tela.blit(texto, (10, 10))

# Loop principal
rodando = True
clock = pygame.time.Clock()

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE):
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE and nave.alive:  # Só atira se estiver viva
                nave.atirar()

    verificar_colisoes()  # Verificar colisões primeiro

    if nave.alive:
        todos_sprites.update()
        if random.randint(0, 100) < 5:
            gerar_asteroides()
    else:
        # Se a nave não está viva, exibir GAME OVER
        font = pygame.font.Font(None, 72)
        texto_game_over = font.render("GAME OVER", True, vermelho)

        # Desenhar a mensagem "GAME OVER" centralizada
        tela.fill(preto)  # Limpa a tela para fundo preto
        tela.blit(texto_game_over, (largura_tela // 2 - texto_game_over.get_width() // 2, altura_tela // 2))

    # Movimentação do background
    background_y += 2
    background2_y += 2
    if background_y >= altura_tela:
        background_y = -altura_tela
    if background2_y >= altura_tela:
        background2_y = -altura_tela
    
    # Desenho na tela
    if nave.alive:
        tela.fill(preto)
        tela.blit(background, (background_x, background_y))
        tela.blit(background, (background_x, background2_y))
        todos_sprites.draw(tela)

    # Desenhar pontuação e corações na tela
    desenhar_pontuacao()
    if nave.alive:
        desenhar_coracoes(tela, nave.coracoes)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()