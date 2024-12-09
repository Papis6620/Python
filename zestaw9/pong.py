import random
import sys
import pygame

# COLORS
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

pygame.init()
size = width, height = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Pong')
font = pygame.font.SysFont("Arial", 42)

# CLOCK
FPS = 60
clock = pygame.time.Clock()

# GAME VARIABLES
ball_x, ball_y = width / 2 - 4, height / 2 - 4
pallet_width, pallet_height = 100, 10
pallet_start_x = width / 2 - pallet_width / 2
player1_score = 0
player2_score = 0
winning_score = 11
ai = 0  # 0 - two players, 1 - AI
choice = 0
move_ball_x = random.randint(-3, 3)
move_ball_y = 5

# SPRITES
sprite_group = pygame.sprite.Group()

sprite_pallet1 = None
sprite_pallet2 = None
sprite_ball = None
sprite_walls = []


class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()


def initialize_sprites():
    global sprite_pallet1, sprite_pallet2, sprite_ball, sprite_walls

    sprite_pallet1 = Block(black, pallet_width, pallet_height)
    sprite_pallet1.rect.topleft = (pallet_start_x, 0)
    sprite_group.add(sprite_pallet1)

    sprite_pallet2 = Block(black, pallet_width, pallet_height)
    sprite_pallet2.rect.topleft = (pallet_start_x, height - pallet_height)
    sprite_group.add(sprite_pallet2)

    sprite_ball = Block(red, 8, 8)
    sprite_ball.rect.topleft = (ball_x, ball_y)
    sprite_group.add(sprite_ball)

    left_wall = Block(white, 1, height)
    left_wall.rect.topleft = (0, 0)
    sprite_group.add(left_wall)

    right_wall = Block(white, 1, height)
    right_wall.rect.topright = (width, 0)
    sprite_group.add(right_wall)

    top_wall = Block(white, width, 1)
    top_wall.rect.topleft = (0, 0)
    sprite_group.add(top_wall)

    bottom_wall = Block(white, width, 1)
    bottom_wall.rect.topleft = (0, height - 1)
    sprite_group.add(bottom_wall)

    sprite_walls = [left_wall, right_wall, top_wall, bottom_wall]


def reset():
    global move_ball_x
    sprite_ball.rect.topleft = (ball_x, ball_y)
    sprite_pallet1.rect.x = pallet_start_x
    sprite_pallet2.rect.x = pallet_start_x
    move_ball_x = random.randint(-3, 3)


def display_winner(winner):
    global player1_score, player2_score, choice
    screen.fill(white)
    winner_text = font.render(f"{winner} wins!", True, black)
    screen.blit(winner_text, (width / 2 - winner_text.get_width() / 2, height / 2 - winner_text.get_height()))
    pygame.display.flip()
    pygame.time.delay(5000)
    player1_score, player2_score, choice = 0, 0, 0
    display_menu()


def display_menu():
    screen.fill(white)
    option1 = font.render("1. Play with computer", True, black)
    screen.blit(option1, (width / 2 - option1.get_width() / 2, height / 2 - 100))
    option2 = font.render("2. Play with 2nd player", True, black)
    screen.blit(option2, (width / 2 - option2.get_width() / 2, height / 2))
    option3 = font.render("Press q to quit", True, black)
    screen.blit(option3, (width / 2 - option3.get_width() / 2, height / 2 + 100))


def handle_events():
    global choice, ai
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit(0)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_1] and choice == 0:
        choice = 1
        ai = 1
    if keys[pygame.K_2] and choice == 0:
        choice = 1
        ai = 0
    if keys[pygame.K_q]:
        pygame.quit()
        sys.exit(0)


def update_paddles():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and sprite_pallet1.rect.x > 0:
        sprite_pallet1.rect.x -= 4
    if keys[pygame.K_RIGHT] and sprite_pallet1.rect.x + pallet_width < width:
        sprite_pallet1.rect.x += 4

    if ai:
        ball_center = sprite_ball.rect.centerx
        pallet_center = sprite_pallet2.rect.centerx
        ai_reaction = random.randint(0, 30)
        if abs(ball_center - pallet_center) > ai_reaction:
            if ball_center < pallet_center and sprite_pallet2.rect.x > 0:
                sprite_pallet2.rect.x -= 3
            if ball_center > pallet_center and sprite_pallet2.rect.right <= width:
                sprite_pallet2.rect.x += 3
    else:
        if keys[pygame.K_a] and sprite_pallet2.rect.x > 0:
            sprite_pallet2.rect.x -= 4
        if keys[pygame.K_d] and sprite_pallet2.rect.x + pallet_width < width:
            sprite_pallet2.rect.x += 4


def update_ball():
    global move_ball_x, move_ball_y, player1_score, player2_score
    sprite_ball.rect.x += move_ball_x
    sprite_ball.rect.y += move_ball_y

    if pygame.sprite.collide_rect(sprite_pallet1, sprite_ball):
        relative_intersect = (sprite_ball.rect.centerx - sprite_pallet1.rect.centerx) / (pallet_width / 2)
        move_ball_x = relative_intersect * 5
        move_ball_y = -move_ball_y
    if pygame.sprite.collide_rect(sprite_pallet2, sprite_ball):
        relative_intersect = (sprite_ball.rect.centerx - sprite_pallet2.rect.centerx) / (pallet_width / 2)
        move_ball_x = relative_intersect * 5
        move_ball_y = -move_ball_y
    if pygame.sprite.collide_rect(sprite_walls[0], sprite_ball) or pygame.sprite.collide_rect(sprite_walls[1], sprite_ball):
        move_ball_x = -move_ball_x
    if pygame.sprite.collide_rect(sprite_walls[2], sprite_ball):
        player2_score += 1
        reset()
    if pygame.sprite.collide_rect(sprite_walls[3], sprite_ball):
        player1_score += 1
        reset()


def draw():
    if not choice:
        display_menu()
    else:
        screen.fill(white)
        sprite_group.draw(screen)
        player1_score_text = font.render(str(player1_score), True, black)
        player2_score_text = font.render(str(player2_score), True, black)
        screen.blit(player1_score_text, (width / 2 - player1_score_text.get_width() / 2, 50))
        screen.blit(player2_score_text, (width / 2 - player2_score_text.get_width() / 2, height - 100))


def main_loop():
    while True:
        handle_events()
        if choice:
            update_paddles()
            update_ball()
            if player1_score == winning_score or player2_score == winning_score:
                winner = "Player 1" if player1_score == winning_score else "Player 2"
                display_winner(winner)
        draw()
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    initialize_sprites()
    main_loop()
