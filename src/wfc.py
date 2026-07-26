import sys

board_size = 5

def print_board(board):
        for y in board:
            print([c.get_color() for c in y])

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
            self.can_be_blue = False
            self.can_be_green = False
            self.can_be_red = False

    def get_color(self):
        if self.can_be_blue == True and self.can_be_green == False and self.can_be_red == False:
             return 'b'
        elif self.can_be_blue == False and self.can_be_green == True and self.can_be_red == False:
            return 'g'
        elif self.can_be_blue == False and self.can_be_green == False and self.can_be_red == True:
             return 'r'
        else:
             return '_'

        
     

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

