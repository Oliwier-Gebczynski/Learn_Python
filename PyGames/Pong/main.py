import pygame
import pyglet
pygame.init()
running = True

# constants and variables
white = (255, 255, 255)
black = (0, 0, 0)
blue = (22, 44, 77)
bg = pygame.image.load("bg.png")

screen_width = 800
screen_height = 800
tick_rate = 30

paddle_speed = 10
paddle_width = 10
paddle_height = 100

line_width = 3

p1_x_pos = 10
p1_y_pos = screen_height / 2 - paddle_height / 2

p2_x_pos = screen_width - paddle_width - 10
p2_y_pos = screen_height / 2 - paddle_height / 2

p1_score = 0
p2_score = 0

p1_up = False
p1_down = False
p2_up = False
p2_down = False

ball_x_pos = screen_width / 2
ball_y_pos = screen_height / 2
ball_width = 15
ball_x_vel = -10
ball_y_vel = 0

game_font = pygame.font.SysFont('Ubuntu', 40)
game_text = pygame.font.SysFont('Ubuntu', 20)

screen = pygame.display.set_mode((screen_width, screen_height))

# drawing objects
def draw_object():
    pygame.draw.rect(screen, white, (int(p1_x_pos), int(p1_y_pos), paddle_width, paddle_height))
    pygame.draw.rect(screen, white, (int(p2_x_pos), int(p2_y_pos), paddle_width, paddle_height))
    pygame.draw.rect(screen, white, ((ball_x_pos),(ball_y_pos), ball_width, ball_width))
    pygame.draw.line(screen, blue, (screen_width/2, 20), (screen_width/2, screen_height-150), line_width)

    score = game_font.render(f"{str(p1_score)} - {str(p2_score)}", False, white)
    exit_text = game_text.render(f"ESC [EXIT]", False, white)

    screen.blit(score, (screen_width / 2.2, screen_height - 100))
    screen.blit(exit_text, (20, 20))


def apply_player_movement():
    global p1_y_pos
    global p2_y_pos

    if p1_up:
        p1_y_pos = max(p1_y_pos - paddle_speed, 0)
    elif p1_down:
        p1_y_pos = min((p1_y_pos + paddle_speed), screen_height - paddle_height)

    if p2_up:
        p2_y_pos = max(p2_y_pos - paddle_speed, 0)
    elif p2_down:
        p2_y_pos = min((p2_y_pos + paddle_speed), screen_height  - paddle_height)

def apply_ball_movement():
    global ball_x_pos
    global ball_y_pos
    global ball_x_vel
    global ball_y_vel
    global p1_score
    global p2_score
    global p1_y_pos
    global p2_y_pos

    if (ball_x_pos + ball_x_vel < p1_x_pos + paddle_width) and (p1_y_pos < ball_y_pos + ball_y_vel + ball_width < p1_y_pos + paddle_height):
        ball_x_vel = -ball_x_vel
        ball_y_vel = (p1_y_pos + paddle_height / 2 - ball_y_pos) / 10
        ball_y_vel = -ball_y_vel
        ball_x_vel *= 1.05

    elif ball_x_pos + ball_x_vel < 0:
        p2_score += 1
        ball_x_pos = screen_width / 2
        ball_y_pos = screen_height / 2
        ball_x_vel = 10
        ball_y_vel = 0

        p1_y_pos = screen_height / 2 - paddle_height / 2
        p2_y_pos = screen_height / 2 - paddle_height / 2

    if (ball_x_pos + ball_x_vel > p2_x_pos - paddle_width) and (p2_y_pos < ball_y_pos + ball_y_vel + ball_width < p2_y_pos + paddle_height):
        ball_x_vel = -ball_x_vel
        ball_y_vel = (p2_y_pos + paddle_height / 2 - ball_y_pos) / 10
        ball_y_vel = -ball_y_vel
        ball_x_vel *= 1.05

    elif ball_x_pos + ball_x_vel > screen_height:
        p1_score += 1
        ball_x_pos = screen_width / 2
        ball_y_pos = screen_height / 2
        ball_x_vel = -10
        ball_y_vel = 0

        p1_y_pos = screen_height / 2 - paddle_height / 2
        p2_y_pos = screen_height / 2 - paddle_height / 2

    if ball_y_pos + ball_y_vel > screen_height or ball_y_pos + ball_y_vel < 0:
        ball_y_vel = -ball_y_vel
        ball_x_vel *= 1.05

    ball_x_pos += ball_x_vel
    ball_y_pos += ball_y_vel

#restart
def restart_game():
    global p1_score
    global p2_score
    global p1_y_pos
    global p2_y_pos

    p1_score = 0
    p2_score = 0
    p1_y_pos = screen_height / 2 - paddle_height / 2
    p2_y_pos = screen_height / 2 - paddle_height / 2


pygame.display.set_caption("PONG")

pygame.display.flip()

while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_a:
                    p1_up = True
                if event.key == pygame.K_z:
                    p1_down = True
                if event.key == pygame.K_UP:
                    p2_up = True
                if event.key == pygame.K_DOWN:
                    p2_down = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    p1_up = False
                if event.key == pygame.K_z:
                    p1_down = False
                if event.key == pygame.K_UP:
                    p2_up = False
                if event.key == pygame.K_DOWN:
                    p2_down = False

    if p1_score == 5 or p2_score == 5:
        restart_game()

    screen.blit(bg, (0, 0))
    apply_player_movement()
    apply_ball_movement()
    draw_object()

    pygame.display.flip()
    pygame.time.wait(tick_rate)

# NeuralNine tutorial