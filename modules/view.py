import random

import pygame


class View:
    def __init__(self, model):
        self.GRID_COLOR = (0, 0, 0)
        self.FONT_COLOR = (255, 255, 255)
        self.FIELD_COLOR = (50, 50, 50)
        self.RECT_COLOR = (0, 255, 255)
        self.COLORS = [(255, 100, 180), (240, 0, 255), (127, 127, 127), (255, 0, 230), (0, 0, 100), (210, 150, 75),
                       (255, 200, 0), (0, 255, 255), (200, 200, 200), (235, 245, 255),'paleturquoise3']
        self.NOT_RUNNING_COLOR = (255,100,10)
        self.RUNNING_COLOR = (0, 150, 0)
        self.__START_MESSAGE = "SPACE to start/pause simulation"
        self.__CLEAR_FIELD = "C to clear field"
        self.__ARROW_UP = "ARROW UP for increasing speed"
        self.__ARROW_DOWN = "ARROW DOWN for decreasing speed"
        self.__MOUSE = "MOUSEWHEEL for zooming"
        self.__RUN = "Is running"
        self.__PAUSE = "PAUSE"
        self.__STOP = "SPACE to pause simulation"
        self.model = model
        self.screen, self.clock = self.init()
        self.tick = 40
        self.cur_tick = 0
        self.cur_color = 0

    def draw_cells(self, dx, dy):
        if self.cur_tick > 120 - self.model.CURR_SPEED:
            self.cur_color = random.randint(0, len(self.COLORS)-1)
            self.cur_tick = 0
        else:
            self.cur_tick += 1
        for pos in self.model.cells:
            res = self.model.get_cell_corner(pos, dx, dy)
            pygame.draw.rect(self.screen, self.COLORS[self.cur_color],
                             pygame.Rect(res[0], res[1], *(self.model.CURR_CELL_SIZE, self.model.CURR_CELL_SIZE)))

    def draw_messages(self):
        FONT_SIZE = min(self.model.HEIGHT // 30, self.model.WIDTH // 40)
        font = pygame.font.SysFont('arial', FONT_SIZE)
        font.set_bold(True)
        if self.model.is_running:
            run = font.render(self.__RUN, False, self.RUNNING_COLOR)
            mes = font.render(self.__STOP, False, self.FONT_COLOR)
            self.screen.blit(mes, (self.model.WIDTH / 2.5, self.model.HEIGHT - (FONT_SIZE + 5) - 5))

        else:
            start = font.render(self.__START_MESSAGE, False, self.FONT_COLOR)
            restart = font.render(self.__CLEAR_FIELD, False, self.FONT_COLOR)
            speed_up = font.render(self.__ARROW_UP, False, self.FONT_COLOR)
            speed_down = font.render(self.__ARROW_DOWN, False, self.FONT_COLOR)
            zoom = font.render(self.__MOUSE, False, self.FONT_COLOR)
            run = font.render(self.__PAUSE, False, self.NOT_RUNNING_COLOR)
            messages = [start, restart, speed_up, speed_down, zoom]
            i = len(messages)
            for m in messages:
                self.print_message(m, (self.model.WIDTH / 1.75, self.model.HEIGHT - (FONT_SIZE + 5) * i - 5))
                i -= 1
        self.screen.blit(run, (20, self.model.HEIGHT - (FONT_SIZE + 5) - 5))

    def print_message(self, mes, pos):
        self.screen.blit(mes, pos)

    def draw_grid(self, dx, dy):
        dx %= self.model.CURR_CELL_SIZE
        dy %= self.model.CURR_CELL_SIZE
        for i in range(self.model.WIDTH // self.model.CURR_CELL_SIZE + 1):
            pygame.draw.line(
                self.screen,
                self.GRID_COLOR,
                (self.model.CURR_CELL_SIZE * i - dx, 0),
                (self.model.CURR_CELL_SIZE * i - dx, self.model.HEIGHT),
                self.model.GRID_WIDTH,
            )
        for i in range(self.model.HEIGHT // self.model.CURR_CELL_SIZE + 1):
            pygame.draw.line(
                self.screen,
                self.GRID_COLOR,
                (0, self.model.CURR_CELL_SIZE * i - dy),
                (self.model.WIDTH, self.model.CURR_CELL_SIZE * i - dy),
                self.model.GRID_WIDTH,
            )

    def init(self):
        pygame.init()
        pygame.font.init()
        screen = pygame.display.set_mode(self.model.SIZE, pygame.RESIZABLE)
        pygame.display.set_caption("Game of life")
        return screen, pygame.time.Clock()

    def update_screen(self):
        self.screen.fill(self.FIELD_COLOR)
        self.draw_cells(self.model.grid_x, self.model.grid_dy)
        self.draw_grid(self.model.grid_x, self.model.grid_dy)
        self.draw_messages()
        pygame.display.flip()
        self.clock.tick(self.model.FPS)
