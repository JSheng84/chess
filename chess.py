import pieces

class Board:
    def __init__(self):
        self.board = [[0 for x in range(8)] for y in range(8)]
        self.pieces_one = [pieces.King('king', 0, 4)]
        self.pieces_two = [pieces.King('king', 7, 5)]
    
    def print_board(self):
        for x in range(8):
            for y in range(8):
                print(self.board[x][y], end =' ')
            print()
        
    def list_pieces(self):
        print('Player One Pieces')
        for x in self.pieces_one:
            x.print_type()
            x.move()
        print ('Player Two Pieces')
        for x in self.pieces_two:
            x.print_type()
            x.move()

b1 = Board()
#b1.initialize_board()
b1.print_board()
b1.list_pieces()