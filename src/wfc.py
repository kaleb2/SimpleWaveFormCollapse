import sys
import datetime

board_size = 5

def print_board(board):
        for y in board:
            print([c.get_color() for c in y])

def zero_or_one():
    return datetime.now().time.microsecond % 2 == 0

class Tile:
    can_be_red = True
    can_be_blue = True
    can_be_green = True

    def __init__(self, color):
        if color == 'r':
            self.can_be_blue = False
            self.can_be_green = False
        elif color == 'g':
            self.can_be_blue = False
            self.can_be_red = False
        elif color == 'b':
            self.can_be_green = False
            self.can_be_red = False
        else:
            self.can_be_blue = True
            self.can_be_green = True
            self.can_be_red = True

    def get_color(self):
        color = ''
        if self.can_be_red:
            color += 'r'
        if self.can_be_green:
            color += 'g'
        if self.can_be_blue:
            color += 'b'
        return color

    def set_color_off(self, c):
        if c == 'r':
            self.can_be_red = False
        elif c == 'g':
            self.can_be_green = False
        elif c == 'b':
            self.can_be_blue = False

    def set_any_color_except(self, c):
        num = zero_or_one()
        if c == 'r':
            self.can_be_red = False
            if num == 0:
                self.can_be_blue = False
            else:
                self.can_be_green = False
        elif c == 'g':
            self.can_be_green = False
            if num == 0:
                self.can_be_blue = False
            else:
                self.can_be_red = False
        elif c == 'b':
            self.can_be_blue = False
            if num == 0:
                self.can_be_red = False
            else:
                self.can_be_green = False

    def is_collapsed(self):
        return len([t for t in [self.can_be_blue, self.can_be_green, self.can_be_red] if t == True]) == 1

def get_neighbor_indices(x, y):
    x_neighbors = []
    if x == 1:
         x_neighbors.append(2)
    elif x == board_size:
        x_neighbors.append(x - 1)
    else:
        x_neighbors.append(x - 1)
        x_neighbors.append(x + 1)

    y_neighbors = []
    if y == 1:
        y_neighbors.append(2)
    elif y == board_size:
        y_neighbors.append(y - 1)
    else:
        y_neighbors.append(y - 1)
        y_neighbors.append(y + 1)

    neighbors = list(zip([x] * len(y_neighbors), y_neighbors)) + list(zip(x_neighbors, [y] * len(x_neighbors)))
    return neighbors



if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Please supply 3 arguments: x, y, and color")
        exit()

    print(f"Arguments: ({sys.argv[1]}, {sys.argv[2]}), {sys.argv[3]} ")

    x = int(sys.argv[1]) - 1
    y = int(sys.argv[2]) - 1
    c = sys.argv[3]

    if x > board_size - 1 or y > board_size - 1:
         print(f"Please enter coordinates within the board size {board_size}")
         exit()

    if c != 'r' and c != 'g' and c != 'b':
         print(f"Please enter a color r, g, or b")
         exit()

    board = [[Tile('_'), Tile('_'), Tile('_'), Tile('_'), Tile('_')],
            [Tile('_'), Tile('_'), Tile('_'), Tile('_'), Tile('_')],
            [Tile('_'), Tile('_'), Tile('_'), Tile('_'), Tile('_')],
            [Tile('_'), Tile('_'), Tile('_'), Tile('_'), Tile('_')],
            [Tile('_'), Tile('_'), Tile('_'), Tile('_'), Tile('_')]]

    board[y][x] = Tile(c)
    print_board(board)

    stack = [(x, y)]

    # propogate
    while len(stack) != 0:
        c = stack.pop()
        tile = board[c[1]][c[0]]
        if tile.is_collapsed():
            neighbors = get_neighbor_indices(x, y)
            stack += neighbors
            for n in neighbors:
                board[n[1]][n[0]].set_color_off(tile.get_color())
        

    # observe
    print_board(board)
    print(stack)
