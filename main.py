import pyglet
import random as rnd


class game_of_life:
    
    def __init__(self, window_width, window_height, cell_size):
        self.grid_width = int(window_width / cell_size)
        self.grid_height = int(window_height / cell_size)
        self.cell_size = cell_size
        self.cells = []
        self.generate_cells()

    def generate_cells(self):
        for row in range(0, self.grid_height):
            self.cells.append([])
            for col in range(0, self.grid_width):
                if rnd.random() < 0.4:
                    self.cells[row].append(1)
                else:
                    self.cells[row].append(0)
       # print(self.cells)

    def draw(self):
        for row in range(0, self.grid_height):
            for col in range(0, self.grid_width):
                if self.cells[row][col] == 1:
                    square_coords = (row * self.cell_size, col * self.cell_size,
                                    row * self.cell_size, col * self.cell_size + self.cell_size,
                                    row * self.cell_size + self.cell_size, col * self.cell_size ,
                                    row * self.cell_size + self.cell_size, col * self.cell_size + self.cell_size)

                    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
                                                [0, 1, 2, 1, 2, 3],
                                                ['v2i', (square_coords)])


    def rules(self):
        temp = []
        for row in range(0, self.grid_height):
            temp.append([])
            for col in range(0, self.grid_width):
                cell_sum = sum([self.get_cell_value(row-1,col),
                               self.get_cell_value(row-1,col-1),
                               self.get_cell_value(row,col-1),
                               self.get_cell_value(row+1,col),
                               self.get_cell_value(row,col+1),
                               self.get_cell_value(row+1,col+1),
                               self.get_cell_value(row+1,col-1),
                               self.get_cell_value(row-1,col+1)])
                
                if self.cells[row][col] == 0 and cell_sum == 3:
                    temp[row].append(1)
                elif self.cells[row][col] == 1 and (cell_sum == 3 or cell_sum == 2):
                    temp[row].append(1)
                else:
                    temp[row].append(0)
        self.cells = temp

    def get_cell_value(self, row, col):
        if row >= 0 and row < self.grid_height and col >= 0 and col < self.grid_width:
            return self.cells[row][col]
        else:
            return 0



class Window(pyglet.window.Window):

    def __init__(self):
        super().__init__(1000,1000)
        self.game_of_life = game_of_life(self.get_size()[0], self.get_size()[1], 10)
        pyglet.clock.schedule_interval(self.update, 1.0/24.0)

    def on_draw(self):
        self.clear()
        self.game_of_life.draw()     
          

    def update(self, dt):
        self.game_of_life.rules()


if __name__ == '__main__':
    window = Window()
    pyglet.app.run()


print('Code ok')



#.........................................



