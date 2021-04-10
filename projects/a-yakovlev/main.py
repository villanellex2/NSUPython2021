#!/usr/bin/env python3.7

import sys
import pygame
import re
from argparse import ArgumentParser

SIZE = WIDTH, HEIGHT = 1280, 720

DEF_CELL_SIZE = 30
CURR_CELL_SIZE = DEF_CELL_SIZE

GRID_COLOR = (130, 100, 100)
FONT_COLOR = (255, 255, 255)
FIELD_COLOR = (50, 50, 50)
RECT_COLOR = (0, 220, 0)
NOT_RUNNIN_COLOR = (150, 0, 0)
RUNNING_COLOR = (0, 150, 0)

ZOOM_RATIO = 1
GRID_WIDTH = 1

CURR_SPEED = 88
FPS = 60


def fill_rects(screen, pos_array, dx, dy):
    for pos in pos_array:
        res = get_rect_corner(pos, dx, dy)
        pygame.draw.rect(screen, RECT_COLOR, pygame.Rect(res[0], res[1], *(CURR_CELL_SIZE, CURR_CELL_SIZE)))


def init():
    pygame.init()
    pygame.font.init() 
    screen = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
    pygame.display.set_caption("Game of life")
    return screen, pygame.time.Clock()


def draw_grid(screen, dx, dy):
    dx %= CURR_CELL_SIZE
    dy %= CURR_CELL_SIZE
    for i in range(WIDTH // CURR_CELL_SIZE + 1):
        pygame.draw.line(
            screen,
            GRID_COLOR,
            (CURR_CELL_SIZE * i - dx, 0),
            (CURR_CELL_SIZE * i - dx, HEIGHT),
            GRID_WIDTH,
        )
    for i in range(HEIGHT // CURR_CELL_SIZE + 1):
        pygame.draw.line(
            screen,
            GRID_COLOR,
            (0, CURR_CELL_SIZE * i - dy),
            (WIDTH, CURR_CELL_SIZE * i - dy),
            GRID_WIDTH,
        )


def get_rect_corner(pos, dx, dy):
    return (
        pos[0] * CURR_CELL_SIZE - dx % CURR_CELL_SIZE,
        pos[1] * CURR_CELL_SIZE - dy % CURR_CELL_SIZE,
    )



def get_rect_coord(pos, dx, dy):
    return (
        ((pos[0] + dx % CURR_CELL_SIZE) // CURR_CELL_SIZE),
        ((pos[1] + dy % CURR_CELL_SIZE) // CURR_CELL_SIZE),
    )



def update_life(rects):
    all_neighbors = {}
    for i in rects:
        all_neighbors.setdefault(i, 0)
        curr_neighbors = (
            (i[0] - 1, i[1]),
            (i[0] + 1, i[1]),
            (i[0], i[1] - 1),
            (i[0], i[1] + 1),
            (i[0] - 1, i[1] - 1),
            (i[0] - 1, i[1] + 1),
            (i[0] + 1, i[1] + 1),
            (i[0] + 1, i[1] - 1),
        )
        for j in curr_neighbors:
            all_neighbors.setdefault(j, 0)
            all_neighbors[j] += 1
    for i in rects.copy():
        if all_neighbors[i] > 3 or all_neighbors[i] < 2:
            rects.remove(i)
    for k in all_neighbors:
        if all_neighbors[k] == 3:
            rects.add(k)
    return rects


def draw_help(screen, running):
    FONT_SIZE = min(HEIGHT//20, WIDTH//40)
    font = pygame.font.SysFont('arial', FONT_SIZE)
    help1 = font.render("SPACE to start simulation", False, FONT_COLOR)
    help2 = font.render("R to restart", False, FONT_COLOR)
    help3 = font.render("ARROW UP for increasing speed", False, FONT_COLOR)
    help4 = font.render("ARROW DOWN for decreasing speed", False, FONT_COLOR)
    help5 = font.render("MOUSEWHEEL for zooming", False, FONT_COLOR)
    help6 = font.render("SPACE to pause simulation", False, FONT_COLOR)
    
    if running:
        running_text1 = font.render("RUN", False, RUNNING_COLOR)
        screen.blit(help6, (20, HEIGHT - (FONT_SIZE + 5) * 1 - 5))
    else:
        running_text1 = font.render("RUN", False, NOT_RUNNIN_COLOR)
        screen.blit(help1, (20, HEIGHT - (FONT_SIZE + 5) * 5 - 5))
        screen.blit(help2, (20, HEIGHT - (FONT_SIZE + 5) * 4 - 5))
        screen.blit(help3, (20, HEIGHT - (FONT_SIZE + 5) * 3 - 5))
        screen.blit(help4, (20, HEIGHT - (FONT_SIZE + 5) * 2 - 5))
        screen.blit(help5, (20, HEIGHT - (FONT_SIZE + 5) * 1 - 5))
    screen.blit(running_text1, (WIDTH//2, 5))


def shift_rects(rects, dx, dy):
    return set([(i - dx, j - dy) for i, j in rects])


def main():
    parser = ArgumentParser()
    parser.add_argument('cfg_path', nargs='?', help="Path to file with config.", default=None)
    options = parser.parse_args()
    global CURR_SPEED
    screen, clock = init()
    rects = set()
    running = False
    speed_counter = 0
    holding_mouse = False
    initial_mouse_pos = None
    shifted = False
    grid_x, grid_dy = 0, 0
    if options.cfg_path != None:
        try:
            with open(options.cfg_path) as f:
                first_line = f.readline()
                if first_line.strip() != "#Life 1.06":
                    print("Error while opening config file. Wrong file type. Got: '" 
                        + first_line.strip() 
                        + "' want '#Life 1.06'.",file=sys.stderr)
                    sys.exit()
                for line in f:
                    line = line.strip()
                    if not re.match(r"^-?[0-9]*[ ]-?[0-9]*$", line):
                        print("Error while reading config file. Wrong file format. Got: '" + line + "'" ,file=sys.stderr)
                        sys.exit()
                    res = list(map(int, line.split()))
                    rects.add((res[0] + 3, res[1] + 3))

        except FileNotFoundError as e:
            print("Error while opening config file.", file=sys.stderr)
            print(e, file=sys.stderr)
            sys.exit()
    while ...:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # window resizing 
            elif event.type == pygame.VIDEORESIZE:
                global SIZE, WIDTH, HEIGHT
                SIZE = WIDTH, HEIGHT = event.size
            # zoom
            elif event.type == pygame.MOUSEWHEEL:
                global ZOOM_RATIO, CURR_CELL_SIZE

                if event.y > 0:
                    ZOOM_RATIO += 0.05
                else:
                    ZOOM_RATIO -= 0.05

                if ZOOM_RATIO < 0.5:
                    ZOOM_RATIO = 0.5
                elif ZOOM_RATIO > 1.5:
                    ZOOM_RATIO = 1.5
                CURR_CELL_SIZE = int(DEF_CELL_SIZE * ZOOM_RATIO)
            elif event.type == pygame.MOUSEBUTTONUP and (event.button == 1 or event.button == 3):
                if event.button == 1:
                    holding_mouse = False
                if not shifted:
                    pos = pygame.mouse.get_pos()
                    coord = get_rect_coord(pos, grid_x, grid_dy)
                    if event.button == 1 and coord in rects:
                        rects.remove(coord)
                    elif event.button == 1:
                        rects.add(coord)
                else:
                    shifted = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                holding_mouse = True
                initial_mouse_pos = pygame.mouse.get_pos()
            
            # user controls
            elif event.type == pygame.KEYDOWN:
                global CURR_SPEED
                if event.key == pygame.K_RETURN:
                    update_life(rects)
                if event.key == pygame.K_SPACE:
                    running = not running
                if event.key == pygame.K_r:
                    rects = set()
                if event.key == pygame.K_UP:
                    CURR_SPEED += 2
                    if CURR_SPEED > 110:
                        CURR_SPEED = 110
                if event.key == pygame.K_DOWN:
                    CURR_SPEED -= 2
                    if CURR_SPEED < 70:
                        CURR_SPEED = 70
        if holding_mouse:
            pos = pygame.mouse.get_pos()
            dx, dy = initial_mouse_pos[0] - pos[0], initial_mouse_pos[1] - pos[1]
            #if not click
            if abs(dx) > 5 or abs(dy) > 5:
                shifted = True
            if shifted:
                shift = get_rect_coord((dx, dy), grid_x, grid_dy)
                grid_x += dx
                grid_dy += dy
                rects = shift_rects(rects, shift[0], shift[1])
                initial_mouse_pos = pos

        if running and speed_counter >= (1100 - (9 + CURR_SPEED / 110) * 110):
            speed_counter = 0
            update_life(rects)
        speed_counter += 1

        screen.fill(FIELD_COLOR)
        fill_rects(screen, rects, grid_x, grid_dy)
        draw_grid(screen, grid_x, grid_dy)
        draw_help(screen, running)
        pygame.display.flip()
        clock.tick(FPS)



if __name__ == "__main__":
    main()