class Model:
    def __init__(self, react):
        self.cells = react
        self.SIZE = self.WIDTH, self.HEIGHT = 1280, 720
        self.DEF_CELL_SIZE = 30
        self.CURR_CELL_SIZE = self.DEF_CELL_SIZE
        self.CURR_SPEED = 100
        self.ZOOM_RATIO = 1
        self.GRID_WIDTH = 1
        self.FPS = 60
        self.is_running = False
        self.speed_counter = 0
        self.is_clicked = False
        self.init_mouse_pos = None
        self.is_moved = False
        self.grid_x, self.grid_dy = 0, 0
        self.view = None

    def shift_cells(self, dx, dy):
        return set([(i - dx, j - dy) for i, j in self.cells])

    def get_cell_corner(self, pos, dx, dy):
        return (
            pos[0] * self.CURR_CELL_SIZE - dx % self.CURR_CELL_SIZE,
            pos[1] * self.CURR_CELL_SIZE - dy % self.CURR_CELL_SIZE,
        )

    def get_cell_coord(self, pos, dx, dy):
        return (
            ((pos[0] + dx % self.CURR_CELL_SIZE) // self.CURR_CELL_SIZE),
            ((pos[1] + dy % self.CURR_CELL_SIZE) // self.CURR_CELL_SIZE),
        )

    def update_cells(self):
        all_neighbors = {}
        for i in self.cells:
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
        for i in self.cells.copy():
            if all_neighbors[i] > 3 or all_neighbors[i] < 2:
                self.cells.remove(i)
        for k in all_neighbors:
            if all_neighbors[k] == 3:
                self.cells.add(k)

    def update(self):
        self.view.update_screen()
