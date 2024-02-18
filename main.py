import pygame
import random

grid = []
cols = 10
rows = 10
res = 10
width = 1280
height = 1280
FPS = 24
font_size = 24


def make2DArray(c, r):
    arr = []
    for _ in range(r):
        row = []
        for _ in range(c):
            row.append(0)
        arr.append(row)
    return arr


def move_forward(x, y, dir):
    match dir:
        case 0:
            y -= 1
        case 1:
            x += 1
        case 2:
            y += 1
        case 3:
            x -= 1
    return x, y


if __name__ == '__main__':
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    running = True
    drawing = False

    # Set the window title
    pygame.display.set_caption("Game of Life")

    cols = int(width / res)
    rows = int(height / res)

    grid = make2DArray(cols, rows)

    ant_x = random.randint(0, cols)
    ant_y = random.randint(0, rows)
    ant_dir = random.randint(0, 3)

    steps = 0
    font = pygame.font.Font(None, 24)


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")

        # Out of bound handling
        if ant_x <= 0:
            ant_x = cols
        if ant_x >= cols:
            ant_x = 0
        if ant_y <= 0:
            ant_y = rows
        if ant_y >= rows:
            ant_y = 0

        for i in range(cols):
            for j in range(rows):
                x = i * res
                y = j * res
                if grid[i][j] == 1:
                    pygame.draw.rect(screen, "white", (x, y, res, res))
                if i == ant_x and j == ant_y:
                    pygame.draw.polygon(screen, "red",
                                        [(x + res, y + res), (x, y + res), (x + res / 2, y)])

        # At a black square, turn 90° clockwise, flip the color of the square, move forward one unit
        if grid[ant_x][ant_y] == 0:
            ant_dir += 1
            if ant_dir == 4:
                ant_dir = 0
            grid[ant_x][ant_y] = 1
            ant_x, ant_y = move_forward(ant_x, ant_y, ant_dir)
        # At a white square, turn 90° counter-clockwise, flip the color of the square, move forward one unit
        else:
            ant_dir -= 1
            if ant_dir < 0:
                ant_dir += 4
            grid[ant_x][ant_y] = 0
            ant_x, ant_y = move_forward(ant_x, ant_y, ant_dir)

        steps += 1
        text = font.render(f"Steps: {steps}", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.topright = (width - 10, 10)
        screen.blit(text, text_rect)
        pygame.display.flip()

        clock.tick(FPS)  # limits FPS

    pygame.quit()
