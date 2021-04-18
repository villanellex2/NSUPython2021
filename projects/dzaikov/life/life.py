import pygame as pg
import os
from os import listdir
from os.path import isfile, join

class Event(object):
    def __init__(self, event):
        self.event = event
        self.consumed = False
    
    def consume(self):
        self.consumed = True
        
class Life(object):
    def __init__(self):
        self.cells = set()
        
    def step(self):
        new_cells = set()
        for cell in self.cells:
            nb_cnt = 0
            for x0 in range(-1, 2):
                for y0 in range(-1, 2):
                    cell0 = (cell[0] + x0, cell[1] + y0)
                    if x0 == 0 and y0 == 0:
                        continue
                    if cell0 in self.cells:
                        nb_cnt += 1
                        continue
                    nb_cnt0 = 0
                    for x1 in range(-1, 2):
                        for y1 in range(-1, 2):
                            if x1 == 0 and y1 == 0:
                                continue
                            if (cell0[0] + x1, cell0[1] + y1) in self.cells:
                                nb_cnt0 += 1
                    if nb_cnt0 == 3:
                        new_cells.add(cell0)
            if nb_cnt == 2 or nb_cnt == 3:
                new_cells.add(cell)
        self.cells = new_cells

class Button(object):
    def __init__(self, action, screen, x = 0, y = 0, w = 0, h = 0, 
                 caption = "", color = (255, 255, 255), color_floating = (100, 100, 100), 
                 color_pressed = (50, 50, 50), text_color = (0, 0, 0)):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.caption = caption
        self.action = action
        self.visible = True
        self.font = pg.font.SysFont('courier', 22)
        self.screen = screen
        self.color = color
        self.color_floating = color_floating
        self.color_pressed = color_pressed
        self.text_color = text_color
        self.pressed = False
        self.floating = False
    
    def draw(self, color, pressed):
        pg.draw.rect(self.screen, color, [self.x, self.y, self.w, self.h])
        caption_surface = self.font.render(self.caption, True, self.text_color)
        self.screen.blit(caption_surface, (self.x + self.w / 2 - caption_surface.get_width() / 2, 
                                           self.y + self.h / 2 - caption_surface.get_height() / 2))
    
    def check_overlap(self, mouse_pos):
        return (mouse_pos[0] <= self.x + self.w
                and mouse_pos[0] >= self.x
                and mouse_pos[1] < self.y + self.h
                and mouse_pos[1] >= self.y)
                
    def events_handle(self, events):
        if not self.visible:
            return
        mouse_pos = pg.mouse.get_pos()
        self.floating = self.check_overlap(mouse_pos)
        for e in events:
            if not e.consumed:
                if e.event.type == pg.MOUSEBUTTONDOWN:
                    if e.event.button == 1 and self.floating:
                        self.pressed = True
                        e.consume()
                if e.event.type == pg.MOUSEBUTTONUP:
                    if e.event.button == 1:
                        if self.pressed:
                            self.action()
                            self.pressed = False
                            e.consume()
                
    def update(self, dt):
        if not self.visible:
            return
        
        curr_color = self.color
        
        if self.floating:
            curr_color = self.color_floating
        
        if self.pressed:
            curr_color = self.color_pressed
            
        self.draw(curr_color, self.pressed)

class TextBox(object):
    def __init__(self, screen, x = 0, y = 0, w = 10, h = 10, max_text_len = 20, 
                 text = "", color = (200, 200, 200), color_pressed = (255, 255, 255), text_color = (0, 0, 0)):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text
        self.visible = True
        self.font = pg.font.SysFont('courier', 22)
        self.screen = screen
        self.color = color
        self.color_pressed = color_pressed
        self.text_color = text_color
        self.pressed = False
        self.floating = False
        self.max_text_len = max_text_len
        self.blink_period = 800
        self.curr_period = self.blink_period
        self.show_carret = False
    
    def draw(self, color, carret = ''):
        pg.draw.rect(self.screen, color, [self.x, self.y, self.w, self.h])
        text_surface = self.font.render(self.text + carret, True, self.text_color)
        self.screen.blit(text_surface, (self.x + 5, self.y + self.h / 2 - text_surface.get_height() / 2))
    
    def check_overlap(self, mouse_pos):
        return (mouse_pos[0] <= self.x + self.w
                and mouse_pos[0] >= self.x
                and mouse_pos[1] < self.y + self.h
                and mouse_pos[1] >= self.y)
                
    def events_handle(self, events):
        if not self.visible:
            return
        mouse_pos = pg.mouse.get_pos()
        self.floating = self.check_overlap(mouse_pos)
        for e in events:
            if not e.consumed:
                if e.event.type == pg.MOUSEBUTTONUP:
                    if e.event.button == 1:
                        if self.pressed:
                            e.consume()
                    
                if e.event.type == pg.MOUSEBUTTONDOWN:
                    if self.floating:
                        self.pressed = True
                        e.consume()
                    else:
                        self.pressed = False
                if self.pressed:
                    e.consume()
                    if e.event.type == pg.KEYDOWN:
                        if  e.event.key == pg.K_BACKSPACE and len(self.text) > 0:
                            self.text = self.text[:-1]
                        elif e.event.key == pg.K_RETURN or e.event.key == pg.K_BACKSPACE:
                            pass
                        elif len(self.text) <= self.max_text_len:
                            self.text += e.event.unicode
                
    def update(self, dt):
        if not self.visible:
            return
        self.curr_period -= dt
        if self.curr_period <= 0:
            self.curr_period = self.blink_period
            self.show_carret = not self.show_carret
        if not self.pressed:
            self.show_carret = False
        curr_color = self.color
        if self.show_carret:
            self.draw(curr_color, "_")
        else:
            self.draw(curr_color)
            
class SaveDialog(object):
    def __init__(self, screen, life, x = 0, y = 0, w = 400, h = 100, color = (110, 110, 110)):
        self.pressed = False
        self.color = color
        self.visible = False
        self.screen = screen
        self.life = life
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text_box = TextBox(screen, x + 5, y + 20, self.w - 10, 30)
        self.save_button = Button(self.save, screen, x + 10, y + self.h - 40, 100, 30, 'Save')
        self.close_button = Button(self.close, screen, x + self.w - 110, y + self.h - 40, 100, 30, 'Close')
    
    def save(self):
        if len(self.text_box.text) == 0:
            curr_fname = 'default'
        else:
            curr_fname = self.text_box.text
        try:
            with open('./maps/' + curr_fname + '.life', 'w') as f:
                f.write('#Life 1.06\n')
                for i in self.life.cells:
                    f.write(f'{int(i[0])} {int(i[1])}\n')
        except Exception as e:
            print('Error while saving the map')
            print(e)
            exit(1)
            
    def close(self):
        self.visible = False
            
    def check_overlap(self, mouse_pos):
        return (mouse_pos[0] <= self.x + self.w
                and mouse_pos[0] >= self.x
                and mouse_pos[1] < self.y + self.h
                and mouse_pos[1] >= self.y)
    
    def draw(self, color):
        #self.text_box.x = self.x + 5
        #self.text_box.y = self.y + 20
        #self.save_button.x = x + 10
        #self.save_button.y = self.y + self.h - 40
        #self.close_button.x = 
        #self.close_button.y = self.y + self.h - 40
        pg.draw.rect(self.screen, color, [self.x, self.y, self.w, self.h])
        
    def events_handle(self, events):
        if not self.visible:
            return
        mouse_pos = pg.mouse.get_pos()
        self.floating = self.check_overlap(mouse_pos)
        
        self.text_box.events_handle(events)
        self.save_button.events_handle(events)
        self.close_button.events_handle(events)
        
        for e in events:
            if not e.consumed:
                if e.event.type == pg.MOUSEBUTTONDOWN:
                    if self.floating:
                        self.pressed = True
                        e.consume()    
                if e.event.type == pg.MOUSEBUTTONUP:
                    if self.pressed:
                        self.pressed = False
                        e.consume()
                    
                              
    def update(self, dt):
        if not self.visible:
            return
        self.draw(self.color)
        self.text_box.update(dt)
        self.save_button.update(dt)
        self.close_button.update(dt)

class OpenDialog(object):
    def __init__(self, screen, life, x = 0, y = 0, w = 400, h = 100, color = (110, 110, 110), max_files = 5):
        self.maps = [[]]
        self.max_files = max_files
        self.pressed = False
        self.color = color
        self.visible = False
        self.screen = screen
        self.life = life
        self.x = x
        self.y = y
        self.w = w
        self.h = h + max_files * 35
        self.page = 0
        self.page_num = 1
        self.buttons = []
        
        self.scan_maps()
        
        self.buttons.append(Button(self.close, screen, x + self.w - 110, y + self.h - 80, 100, 30, 'Close'))
        self.buttons.append(Button(self.scan_maps, screen, x + 10, y + self.h - 80, 100, 30, 'Refresh'))
        self.buttons.append(Button(self.prev_page, screen, x + 10, y + self.h - 40, 120, 30, 'Prev page'))
        self.buttons.append(Button(self.next_page, screen, x + self.w - 130, y + self.h - 40, 120, 30, 'Next page'))
        for i in range(max_files):
            self.buttons.append(Button(self.get_loader(i), screen, x + 5, y + 5 * (i + 1) + i * 30, self.w - 10, 30))
        self.files_buttons = self.buttons[4:]
    
    def next_page(self):
        if self.page < self.page_num - 1:
            self.page += 1
            
    def prev_page(self):
        if self.page > 0:
            self.page -= 1
    def get_loader(self, i):
        local_i = int(i)
        return lambda: self.try_read(self.maps[self.page][local_i], True)
        
    def try_read(self, path, put = False):
        new_cells = set()
        try:
            if isfile('./maps/' + path) and (path.endswith('.life') or path.endswith('.lif')):
                with open('./maps/' + path, 'r') as f:
                    header = f.readline()
                    for line in f:
                        if line == '#Life 1.06\n':
                            continue
                        split = line.split()
                        try:
                            x = int(split[0])
                            y = int(split[1])
                            
                            new_cells.add((x, y))
                        except ValueError:
                            print(1)
                            return False
            else:
                return False
        except Exception as e:
            print(e)
        if put:
            self.life.cells = new_cells
        return True
    
    def chunks(self, lst, n):
        for i in range(0, len(lst), n):
            yield lst[i:i + n]
    
    def scan_maps(self):
        try:
            maps = [f for f in listdir('./maps') if self.try_read(f)]
            self.page_num = len(maps) // self.max_files + (len(maps) % self.max_files != 0)
            self.maps = [c for c in self.chunks(maps, self.max_files)]
            if len(self.maps) == 0:
                self.maps = [[]]
        except Exception as e:
            print('scan_maps: ' + str(e))
            exit(1)
            
    def close(self):
        self.visible = False
            
    def check_overlap(self, mouse_pos):
        return (mouse_pos[0] <= self.x + self.w
                and mouse_pos[0] >= self.x
                and mouse_pos[1] < self.y + self.h
                and mouse_pos[1] >= self.y)
    
    def draw(self, color):
        pg.draw.rect(self.screen, color, [self.x, self.y, self.w, self.h])
        
    def events_handle(self, events):
        if not self.visible:
            return
        mouse_pos = pg.mouse.get_pos()
        self.floating = self.check_overlap(mouse_pos)
        
        for b in self.buttons:
            b.events_handle(events)
        
        for e in events:
            if not e.consumed:
                if e.event.type == pg.MOUSEBUTTONDOWN:
                    if self.floating:
                        self.pressed = True
                        e.consume()    
                if e.event.type == pg.MOUSEBUTTONUP:
                    if self.pressed:
                        self.pressed = False
                        e.consume()
                                                 
    def update(self, dt):
        if not self.visible:
            return
        self.draw(self.color)
        for i in range(self.max_files):
            if i >= len(self.maps[self.page]):
                self.files_buttons[i].visible = False
            else:
                self.files_buttons[i].caption = os.path.basename(self.maps[self.page][i])
                self.files_buttons[i].visible = True
                
        for b in self.buttons:
            b.update(dt)
        
class Grid(object):

    def __init__(self, screen, csize, cells):
        self.cell_size = csize
        self.screen = screen
        self.scale = 1
        self.cells = cells
        self.pov = [0, 0]
        self.curr_cell = [0, 0]

        self.saved_mouse_pos = [0, 0]
        self.mouse_pos_diff = [0, 0]
        self.drag = False
        
        self.update_grid_size()
        
    def update_grid_size(self):
        self.x_cnt = int(self.screen.get_width() // (self.cell_size * self.scale)) + 1
        self.y_cnt = int(self.screen.get_height() // (self.cell_size * self.scale)) + 1
    
    def get_curr_x_y(self):
        curr_cell_size = self.cell_size * self.scale
        curr_x = curr_cell_size - self.pov[0] % curr_cell_size
        curr_y = curr_cell_size - self.pov[1] % curr_cell_size
        return curr_cell_size, curr_x, curr_y
    
    def draw_lines(self, color):
        w = self.screen.get_width()
        h = self.screen.get_height()
        curr_cell_size, curr_x, curr_y = self.get_curr_x_y()
        for i in range(self.x_cnt):
            pg.draw.line(self.screen, color, 
                (curr_x, 0), 
                (curr_x, h), 1)
            curr_x += curr_cell_size
            
        for i in range(self.y_cnt):
            pg.draw.line(self.screen, color, 
                (0, curr_y), 
                (w, curr_y), 1)
            curr_y += curr_cell_size
            
    def draw_rects(self, color):
        curr_cell_size, curr_x, curr_y = self.get_curr_x_y()
        for cell in self.cells.cells:
            if (cell[0] >= self.curr_cell[0] - 1
                and cell[0] <= self.curr_cell[0] + self.x_cnt
                and cell[1] >= self.curr_cell[1] - 1
                and cell[1] <= self.curr_cell[1] + self.y_cnt):
                
                pg.draw.rect(self.screen, color, [
                    (cell[0] - self.curr_cell[0]) * curr_cell_size + curr_x,
                    (cell[1] - self.curr_cell[1]) * curr_cell_size + curr_y,
                    self.cell_size * self.scale,
                    self.cell_size * self.scale])
                    
    def curr_cell_update(self):
        self.curr_cell[0] = int(self.pov[0] // (self.cell_size * self.scale))
        self.curr_cell[1] = int(self.pov[1] // (self.cell_size * self.scale))
        
    def zoom_in(self, ws, mouse_pos):
        if (self.scale < 6):
            self.scale *= 1.1
            self.pov[0] += (mouse_pos[0] + self.pov[0]) * 0.1
            self.pov[1] += (mouse_pos[1] + self.pov[1]) * 0.1
                 
    def zoom_out(self, ws, mouse_pos):
        if (self.scale > 0.1):
            self.scale *= 0.9
            self.pov[0] -= (mouse_pos[0] + self.pov[0]) * 0.1
            self.pov[1] -= (mouse_pos[1] + self.pov[1]) * 0.1
            
    def events_handle(self, events):
        ws = self.screen.get_size()
        mouse_pos = pg.mouse.get_pos()
        for e in events:
            if not e.consumed:
                e.consume()
                if e.event.type == pg.MOUSEBUTTONDOWN:
                    if e.event.button == 1:
                        if not self.drag:
                            self.drag = True
                            self.saved_mouse_pos = list(mouse_pos)
                            self.old_pov = list(self.pov)
                    elif e.event.button == 4:
                        self.zoom_in(ws, mouse_pos)
                        self.update_grid_size()
                        self.curr_cell_update()
                    elif e.event.button == 5:
                        self.zoom_out(ws, mouse_pos)
                        self.update_grid_size()
                        self.curr_cell_update()
                if e.event.type == pg.MOUSEBUTTONUP:
                    if e.event.button == 1:
                        self.drag = False
                        if (abs(self.pov[0] - self.old_pov[0]) < 5 
                           and abs(self.pov[1] - self.old_pov[1]) < 5):
                            curr_cell_size, curr_x, curr_y = self.get_curr_x_y()
                            x_cell = int((mouse_pos[0] - curr_x) // curr_cell_size) + self.curr_cell[0]
                            y_cell = int((mouse_pos[1] - curr_y) // curr_cell_size) + self.curr_cell[1]
                            if not (x_cell, y_cell) in self.cells.cells:
                                self.cells.cells.add((x_cell, y_cell))
                            else:
                                self.cells.cells.remove((x_cell, y_cell))
                            
                if e.event.type == pg.VIDEORESIZE:
                    self.update_grid_size()
                    
    def update(self, dt):
        mouse_pos = pg.mouse.get_pos()
        
        if self.drag:    
            self.pov[0] = self.old_pov[0] + self.saved_mouse_pos[0] - mouse_pos[0]
            self.pov[1] = self.old_pov[1] + self.saved_mouse_pos[1] - mouse_pos[1]
            self.curr_cell_update()
            
        self.screen.fill((0, 0, 0))
        self.draw_rects((255, 255, 255))
        self.draw_lines((128, 128, 128))

class GameState(object):
    def __init__(self, csize = 50, ww = 1280, wh = 600, fps = 60):
        if not os.path.isdir('./maps'):
            try:
                os.mkdir('./maps')
            except Exception:
                print ("Creation of the maps directory is failed")
                exit(1)
        self.fps = fps
        self.running = True

        self.cells = Life()
        pg.init()
        pg.font.init()
        self.screen = pg.display.set_mode((ww, wh), pg.RESIZABLE)
        self.period = 100
        self.pause = True
        pg.display.set_caption("Life")
        self.clock = pg.time.Clock()
        self.objects = []
        self.pause_button = Button(self.pause_set, self.screen, 230, 10, 100, 30, "Play")
        self.save_dialog = SaveDialog(self.screen, self.cells, 10, 60)
        self.open_dialog = OpenDialog(self.screen, self.cells, 10, 180)
        self.objects.append(Button(lambda: self.change_speed(10), self.screen, 10, 10, 100, 30, "Slower"))
        self.objects.append(Button(lambda: self.change_speed(-10), self.screen, 120, 10, 100, 30, "Faster"))
        self.objects.append(self.pause_button)
        self.objects.append(Button(self.opend, self.screen, 340, 10, 130, 30, "Open map"))
        self.objects.append(Button(self.saved, self.screen, 480, 10, 130, 30, "Save map"))
        self.objects.append(self.save_dialog)
        self.objects.append(self.open_dialog)
        
        self.objects.append(Grid(self.screen, csize, self.cells))
        
    
    def change_speed(self, val):
        self.period += val
        if self.period <= 10:
            self.period = 10
     
    def saved(self):
        self.save_dialog.visible = True
        
    def opend(self):
        self.open_dialog.visible = True
        
    def pause_set(self):
        self.pause = not self.pause
        if self.pause:
            self.pause_button.color = (255, 255, 255)
            self.caption = 'Play'
        else:
            self.pause_button.color = (110, 110, 110)
            self.caption = 'Pause'
        
    def main_loop(self):
        curr_period = self.period
        
        while self.running:
            dt = self.clock.tick(self.fps)
            mouse_pos = pg.mouse.get_pos()
            
            if not self.pause:
                curr_period -= dt
            if curr_period <= 0:
                curr_period = self.period
                self.cells.step()
                
            events = []
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False               
                events.append(Event(event))
                
            for o in self.objects:
                o.events_handle(events)
            for o in reversed(self.objects):
                o.update(dt)
            
            pg.display.flip()

        pg.quit()

        
def main():
    state = GameState()
    state.main_loop()
    
    
if __name__ == "__main__":
    main()