import pygame
import random
import json

from db import get_user, create_user, save_game_state, get_connection

pygame.init()

WIDTH, HEIGHT = 600, 600
BLOCK = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake with Levels")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)

LEVEL_SPEED = {
    1: 8,
    2: 12,
    3: 16
}

def calculate_level(score):
    if score >= 100:
        return 3
    elif score >= 50:
        return 2
    return 1

def update_user_level(user_id, level):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE users SET level = %s WHERE user_id = %s",
        (level, user_id)
    )
    conn.commit()
    conn.close()

def username_screen():
    username = ""

    while True:
        screen.fill(BLACK)

        title = font.render("Enter username", True, WHITE)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, HEIGHT//2 - 80))

        box = pygame.Rect(WIDTH//2 - 150, HEIGHT//2 - 20, 300, 40)
        pygame.draw.rect(screen, WHITE, box, 2)

        text = font.render(username, True, WHITE)
        screen.blit(text, (box.x + 10, box.y + 7))

        hint = font.render("Press ENTER to start", True, WHITE)
        screen.blit(hint, (WIDTH//2 - hint.get_width()//2, HEIGHT//2 + 40))

        pygame.display.flip()
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and username:
                    return username
                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                elif event.unicode.isalnum() and len(username) < 15:
                    username += event.unicode

username = username_screen()

user = get_user(username)
if user:
    user_id = user["user_id"]
    level = user["level"]
else:
    user_id = create_user(username)
    level = 1

speed = LEVEL_SPEED[level]

snake = [(10, 10)]
direction = (1, 0)
food = (random.randint(0, 29), random.randint(0, 29))
score = 0
paused = False
running = True

def save_game():
    state = json.dumps({
        "snake": snake,
        "direction": direction,
        "food": food
    })

    save_game_state(
        user_id=user_id,
        score=score,
        level=level,
        state_json=state
    )

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_game()
            update_user_level(user_id, level)
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 1):
                direction = (0, -1)
            elif event.key == pygame.K_DOWN and direction != (0, -1):
                direction = (0, 1)
            elif event.key == pygame.K_LEFT and direction != (1, 0):
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                direction = (1, 0)

            elif event.key == pygame.K_p:
                paused = not paused
                if paused:
                    save_game()

    if paused:
        screen.fill(BLACK)
        pause_text = font.render("PAUSED (Press P)", True, WHITE)
        screen.blit(
            pause_text,
            (WIDTH//2 - pause_text.get_width()//2, HEIGHT//2)
        )
        pygame.display.flip()
        clock.tick(5)
        continue

    head_x, head_y = snake[0]
    new_head = (head_x + direction[0], head_y + direction[1])

    if not (0 <= new_head[0] < WIDTH//BLOCK and 0 <= new_head[1] < HEIGHT//BLOCK):
        save_game()
        update_user_level(user_id, level)
        break

    if new_head in snake:
        save_game()
        update_user_level(user_id, level)
        break

    snake.insert(0, new_head)

    if new_head == food:
        score += 10

        new_level = calculate_level(score)
        if new_level != level:
            level = new_level
            speed = LEVEL_SPEED[level]

        food = (random.randint(0, 29), random.randint(0, 29))
    else:
        snake.pop()

    screen.fill(BLACK)

    for part in snake:
        pygame.draw.rect(
            screen, GREEN,
            (part[0] * BLOCK, part[1] * BLOCK, BLOCK, BLOCK)
        )

    pygame.draw.rect(
        screen, RED,
        (food[0] * BLOCK, food[1] * BLOCK, BLOCK, BLOCK)
    )

    info = font.render(
        f"User: {username}  Score: {score}  Level: {level}",
        True, WHITE
    )
    screen.blit(info, (10, 10))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
