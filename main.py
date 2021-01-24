import pygame
import math
import random
from templates import Templates

pygame.init()
size = width, height = 1200, 800
window = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption("Conway's Game of Life")
playing = True
started = False
cell_horizontal = 100
cell_vertical = 100


def gen_grid(width, height):
    arr = []
    for i in range(height):
        arr.append([0 for i in range(width)])
    return arr


map_array = gen_grid(cell_horizontal, cell_vertical)
templates = Templates()


def draw_grid():
    for i in range(len(map_array)):
        pygame.draw.line(window, (100,100,100), (0, (height / len(map_array) * i)), (width, (height / len(map_array) * i)))
        for j in range(len(map_array[i])):
            pygame.draw.line(window, (100,100,100), ((width / len(map_array[i]) * j), 0), ((width / len(map_array[i])) * j, height))


def draw_cells():
    for i in range(len(map_array)):
        for j in range(len(map_array[i])):
            cords = ((width / len(map_array[i])) * j, (height / len(map_array)) * i)
            size = (width / len(map_array[i]), height / len(map_array))
            rect = pygame.Rect(cords, size)
            if map_array[i][j] == 1:
                pygame.draw.rect(window, (155, 155, 0), rect)
            elif map_array[i][j] == 2:
                pygame.draw.rect(window, (0, 255, 0), rect)


def get_neighbours(x, y):
    # TODO optimize this
    neighbours = []
    for i in range(-1, 2):
        next_y = y + i
        if not next_y >= 0:
            next_y = len(map_array) - 1
        elif next_y > len(map_array) - 1:
            next_y = 0
        for j in range(-1, 2):
            next_x = x + j
            if not next_x >= 0:
                next_x = len(map_array[i]) - 1
            elif next_x > len(map_array) - 1:
                next_x = 0

            if i == 0 and j == 0:
                continue

            if map_array[next_y][next_x] == 1:
                neighbours.append([next_y, next_x])

    # if len(neighbours) > 0:
    #     # print(f"{neighbours} for cell x:{x} y:{y}")
    #     if map_array[y][x] != 1:
    #         map_array[y][x] = 2
    #         # print(next_y, next_x)
    return len(neighbours)


def pos_to_cell(x, y):
    cell_width = width / len(map_array[0])
    cell_height = height / len(map_array)
    index = (math.floor(x / cell_width), math.floor(y / cell_height))
    return index


def create_random():
    global map_array
    map_array = gen_grid(cell_horizontal, cell_vertical)
    for i in range(len(map_array)):
        for j in range(len(map_array[i])):
            map_array[i][j] = random.choice([0, 1])


def simulate_cells():
    to_kill = []
    to_live = []
    for i in range(len(map_array)):

        for j in range(len(map_array[i])):

            neighbours = get_neighbours(j, i)
            # print(neighbours)
            # live = sum([x.count(1) for x in neighbours]) - 1 # Accounting for self
            # if neighbours > 0 and map_array[j][i] == 1:
            #     # print(live)
            #     print(neighbours)
            # print(live)

            if map_array[i][j] == 0:
                if neighbours == 3:
                    to_live.append((i,j))
                    # print(f"Save {i} {j}")

            if map_array[i][j] == 1:
                if neighbours == 2 or neighbours == 3:
                    # print("test")
                    continue
                else:
                    # print(f"Kill {i} {j}")
                    to_kill.append((i,j))
    for i in to_kill:
        map_array[i[0]][i[1]] = 0
    for i in to_live:
        map_array[i[0]][i[1]] = 1

    # map_array = arr


while playing:
    window.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                started = True if not started else False
            if event.key == pygame.K_s:
                started = False
                map_array = gen_grid(cell_horizontal, cell_vertical)
            if event.key == pygame.K_r:
                started = False
                create_random()
            if event.key == pygame.K_1:
                started = False
                map_array = templates.create_methuselahs(random.choice([1,2,3, 4]))
            if event.key == pygame.K_2:
                started = False
                map_array = templates.create_gosper_gun()

    if pygame.mouse.get_pressed()[0]:
        pos = pos_to_cell(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        map_array[pos[1]][pos[0]] = 1
    if started:
        simulate_cells()
    draw_grid()
    draw_cells()
    clock.tick(10)
    pygame.display.update()