import sys
from time import sleep
import pygame
from pyparsing import Literal

# COLORS
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

class Block(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

# INITIALIZE THE GAME
pygame.init()   # to zawsze na starcie
size = width, height = (800, 600)
screen = pygame.display.set_mode(size)   # display Surface
pygame.display.set_caption('Pong')
font = pygame.font.SysFont("Arial", 42)

# CLOCK
FPS = 60  # frames per second setting
clock = pygame.time.Clock()


ball_x, ball_y = width/2 - 4, height/2 - 4
pallet_width, pallet_height = 100, 10
pallet_start_x = width / 2 - pallet_width/2
box_color = black   # początkowy kolor kwadratu
player1_score = 0
player2_score = 0

sprite_group = pygame.sprite.Group()

sprite_pallet1 = Block(black, pallet_width, pallet_height)
sprite_pallet1.rect.topleft = (pallet_start_x, 0)
sprite_group.add(sprite_pallet1)

sprite_pallet2 = Block(black, pallet_width, pallet_height)
sprite_pallet2.rect.topleft = (pallet_start_x, height - pallet_height)
sprite_group.add(sprite_pallet2)

sprite_ball = Block(red, 8, 8)
sprite_ball.rect.topleft = (ball_x, ball_y)
sprite_group.add(sprite_ball)

sprite_left_wall = Block(white, 1, height)
sprite_left_wall.rect.topleft = (0, 0)
sprite_group.add(sprite_left_wall)

sprite_right_wall = Block(white, 1, height)
sprite_right_wall.rect.topright = (width, 0)
sprite_group.add(sprite_right_wall)

sprite_bottom_wall = Block(green, width, 1)
sprite_bottom_wall.rect.topleft = (0, height - 1)
sprite_group.add(sprite_bottom_wall)

sprite_top_wall = Block(blue, width, 1)
sprite_top_wall.rect.topleft = (0, 0)
sprite_group.add(sprite_top_wall)

move_ball_x = 2
move_ball_y = 2


def reset():
    sprite_ball.rect.x = ball_x
    sprite_ball.rect.y = ball_y
    sprite_pallet1.rect.x = pallet_start_x
    sprite_pallet2.rect.x = pallet_start_x

# MAIN GAME LOOP
while True:
    # HANDLE EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # QUIT Event
            pygame.quit()
            sys.exit(0)
        # Wykrywanie wciśnięcia i puszczenia klawisza.
        # SPOSÓB I - badanie zdarzeń.
        elif event.type == pygame.KEYDOWN:
            # print("event down dict {}".format(event.__dict__))
            # atrybuty key, mod, unicode, scancode
            if event.key == pygame.K_ESCAPE:
                print("Właśnie wciśnięto ESC")
            elif event.key == pygame.K_a:
                print("Właśnie wciśnięto A")
            elif event.key == pygame.K_d:
                print("Właśnie wciśnięto D")
            elif event.key == pygame.K_LEFT:
                print("Właśnie wciśnięto l_a")
            elif event.key == pygame.K_RIGHT:
                print("Właśnie wciśnięto r_a")

    # CHECKING INPUTS
    # SPOSÓB II - badanie stanu urządzenia (pygame.key).
    keys = pygame.key.get_pressed()   # tablica/tuple 0/1
    # Tablica dostarcza informacji, że klawisz jest trzymany wciśnięty.
    # Do indeksowania tablicy używa się ID klawiszy.
    # UWAGA Tej metody nie należy używać do pobierania tekstu od usera
    # (można zgubić klawisze).
    #print(keys)
    # Nie używamy elif, bo klawisze mogą być jednocześnie wciśnięte.
    if keys[pygame.K_LEFT] and sprite_pallet1.rect.x > 0:   # klawisze kursorów
        sprite_pallet1.rect.x -= 3
    if keys[pygame.K_RIGHT] and sprite_pallet1.rect.x + pallet_width < width:
        sprite_pallet1.rect.x += 3
    if keys[pygame.K_a] and sprite_pallet2.rect.x > 0:   # klawisze kursorów
        sprite_pallet2.rect.x -= 3
    if keys[pygame.K_d] and sprite_pallet2.rect.x + pallet_width < width:
        sprite_pallet2.rect.x += 3
    if keys[pygame.K_q]:
        pygame.quit()
        sys.exit(0)
    if pygame.sprite.collide_rect(sprite_pallet1, sprite_ball):
        move_ball_y *= -1
    if pygame.sprite.collide_rect(sprite_pallet2, sprite_ball):
        move_ball_y *= -1
    if pygame.sprite.collide_rect(sprite_left_wall, sprite_ball):
        move_ball_x *= -1
    if pygame.sprite.collide_rect(sprite_right_wall, sprite_ball):
        move_ball_x *= -1
    if pygame.sprite.collide_rect(sprite_top_wall, sprite_ball):
        player2_score += 1
        print("\n \n \n \n \n")
        print(f"Player 1: {player1_score}")
        print(f"Player 2: {player2_score}")

        reset()

    if pygame.sprite.collide_rect(sprite_bottom_wall, sprite_ball):
        player1_score += 1
        print("\n \n \n \n \n")
        print(f"Player 1: {player1_score}")
        print(f"Player 2: {player2_score}")

        reset()

    # DRAWING
    screen.fill(white)   # na nowo czarny ekran
    pygame.draw.rect(screen, box_color, sprite_pallet1)
    pygame.draw.rect(screen, box_color, sprite_pallet2)
    pygame.draw.rect(screen, box_color, sprite_ball)
    pygame.draw.rect(screen, green, sprite_bottom_wall)
    pygame.draw.rect(screen, blue, sprite_top_wall)
    pygame.draw.rect(screen, red, sprite_bottom_wall)
    pygame.draw.rect(screen, black, sprite_top_wall)

    player1_score_text = font.render(str(player1_score), True, black)
    player2_score_text = font.render(str(player2_score), True, black)

    screen.blit(player1_score_text, (width / 2 - player1_score_text.get_width() / 2, 50))
    screen.blit(player2_score_text, (width / 2 - player2_score_text.get_width() / 2, 550 - player2_score_text.get_height()))

    sprite_ball.rect.x -= move_ball_x
    sprite_ball.rect.y -= move_ball_y


    pygame.display.flip()
    clock.tick(FPS)

