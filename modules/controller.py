import sys

import pygame


class Controller:
    def __init__(self, model):
        self.model = model

    def run(self):
        while ...:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.VIDEORESIZE:
                    self.model.SIZE = self.model.WIDTH, self.model.HEIGHT = event.size
                elif event.type == pygame.MOUSEWHEEL:
                    if event.y > 0:
                        self.model.ZOOM_RATIO += 0.05
                    else:
                        self.model.ZOOM_RATIO -= 0.05

                    if self.model.ZOOM_RATIO < 0.1:
                        self.model.ZOOM_RATIO = 0.1
                    elif self.model.ZOOM_RATIO > 2:
                        self.model.ZOOM_RATIO = 2
                    self.model.CURR_CELL_SIZE = int(self.model.DEF_CELL_SIZE * self.model.ZOOM_RATIO)
                elif event.type == pygame.MOUSEBUTTONUP and (event.button == 1 or event.button == 3):
                    if event.button == 1:
                        self.model.is_clicked = False
                    if not self.model.is_moved:
                        pos = pygame.mouse.get_pos()
                        coord = self.model.get_cell_coord(pos, self.model.grid_x, self.model.grid_dy)
                        if event.button == 1 and coord in self.model.cells:
                            self.model.cells.remove(coord)
                        elif event.button == 1:
                            self.model.cells.add(coord)
                    else:
                        self.model.is_moved = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.model.is_clicked = True
                    self.model.init_mouse_pos = pygame.mouse.get_pos()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.model.is_running = not self.model.is_running
                    if event.key == pygame.K_c:
                        self.model.cells = set()
                    if event.key == pygame.K_UP and self.model.CURR_SPEED < 110:
                        self.model.CURR_SPEED += 2
                    if event.key == pygame.K_DOWN and self.model.CURR_SPEED > 70:
                        self.model.CURR_SPEED -= 2

            if self.model.is_clicked:
                pos = pygame.mouse.get_pos()
                dx, dy = self.model.init_mouse_pos[0] - pos[0], self.model.init_mouse_pos[1] - pos[1]
                if abs(dx) > 5 or abs(dy) > 5:
                    self.model.is_moved = True
                if self.model.is_moved:
                    shift = self.model.get_cell_coord((dx, dy), self.model.grid_x, self.model.grid_dy)
                    self.model.grid_x += dx
                    self.model.grid_dy += dy
                    self.model.cells = self.model.shift_cells(shift[0], shift[1])
                    self.model.init_mouse_pos = pos

            if self.model.is_running and self.model.speed_counter >= (1100 - (9 + self.model.CURR_SPEED / 110) * 110):
                self.model.speed_counter = 0
                self.model.update_cells()

            self.model.speed_counter += 1
            self.model.update()
