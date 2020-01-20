import pieces

class Board:
    def __init__(self):
        self.board = [['* ' for x in range(8)] for y in range(8)]
        self.pieces_one = []
        self.pieces_two = []
    
    def initialize_board(self):
        # initialize pawns
        for x in [1 ,6]:
            for y in range(8):
                if x == 1:
                    self.pieces_one.append(pieces.Pawn('pawn', x, y))
                    self.board[x][y] = 'p1'
                else:
                    self.pieces_two.append(pieces.Pawn('pawn', x, y))
                    self.board[x][y] = 'p2'
                
        # initialize rooks
        for x in [0, 7]:
            for y in [0,7]:
                if x == 0:
                    self.pieces_one.append(pieces.Rook('rook', x, y))
                    self.board[x][y] = 'r1'
                else:
                    self.pieces_two.append(pieces.Rook('rook', x, y))
                    self.board[x][y] = 'r2'
        
            # initialize horse
            for y in [1,6]:
                if x == 0:
                    self.pieces_one.append(pieces.Horse('horse', x, y))
                    self.board[x][y] = 'h1'
                else:
                    self.pieces_two.append(pieces.Horse('horse', x, y))
                    self.board[x][y] = 'h2'

            # initialize bishop
            for y in [2,5]:
                if x == 0:
                    self.pieces_one.append(pieces.Bishop('bishop', x, y))
                    self.board[x][y] = 'b1'
                else:
                    self.pieces_two.append(pieces.Bishop('bishop', x, y))
                    self.board[x][y] = 'b2'
            
        # initialize queen
        self.pieces_one.append(pieces.Queen('queen', 0, 4))
        self.board[0][4] = 'q1'
        self.pieces_two.append(pieces.Queen('queen', 7, 4))
        self.board[7][4] = 'q2'
            
        # initialize king
        self.pieces_one.append(pieces.King('king', 0, 3))
        self.board[0][3] = 'k1'
        self.pieces_two.append(pieces.King('king', 7, 3))
        self.board[7][3] = 'k2'


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
b1.initialize_board()
b1.print_board()
b1.list_pieces()