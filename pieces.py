from abc import ABC, abstractmethod
import enum

class Piece(ABC):
    def __init__(self, name, x, y):
        self.name = self.check_name(name)
        self.x = x
        self.y = y

    def check_name(self, name):
        piece_list =['pawn', 'bishop', 'rook', 'horse', 'queen', 'king']
        if (name in piece_list):
            return name
        else:
            raise ValueError('%s is not a chess piece' % name)
    
    def print_type(self):
        print(self.name + ' : ' + str(self.x) + ',' + str(self.y))

    @abstractmethod
    def move(self):
        return NotImplemented

class Pawn(Piece):
    def move(self):
        print("I can only move forward")

class Bishop(Piece):
    def move(self):
        print("I can only move diagonal")

class Rook(Piece):
    def move(self):
        print("I can only move horizontal")

class Queen(Piece):
    def move(self):
        print("I can move anywhere")

class King(Piece):
    def move(self):
        print("I can move anywhere one space")

class Horse(Piece):
    def move(self):
        print("I can move only in an L shape")