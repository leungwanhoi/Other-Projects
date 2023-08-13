#SID: 1155142877

from abc import abstractmethod
from enum import Enum

dic = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5}

class Color(Enum): 
    BLACK = 'X' 
    RED = 'O' 
    
#c = Color.RED
#c.name = RED
#c.value = O

#class Piece(Color):
#    def __init__(self):
#        super().__init(color)
#        self.color = color

class Player():
    def __init__(self, player):
        self.player = player

    def get_input(self):
        try:
            in_put = input(f"Player {self.player}'s turn")
            x = in_put.replace(" ", "")
            x1 = x[0]
            x2 = x[1]
            return(dic.get(x1),int(x2))
        except dic.get(x1) == None or int(x2) < 0 or int(x2) > 6 or isinstance(x2, int) == False : #####################
            print("Invalid move!")


class Gekitai():
    def __init__(self, n, p, l, board_list):
        super().__init__(board_list)
        self.n = n # size
        self.p = p # no. of pieces
        self.l = l # no. of pieces to win

    def is_move_valid(self, y, x):
        if self.board_list[y][x]!= " ":
            return False
        else:
            return True

    def move(self, piece, y, x):
        # add on the new piece
        if Gekitai.is_move_valid(y, x) == True:
            self.board_list[y][x] = piece
            # check surrounding pieces and position to be repelled
            # left
            # the piece is placed in the centre
            if x-1 > 0 and self.board_list[y][x-1] != " " :
                if self.board_list[y][x-2] == " " :
                    self.board_list[y][x-2] = self.board_list[y][x-1]
                    self.board_list[y][x-1] = " "
            # the adjacent piece of the placed piece is on the edge
            if x-1 == 0 and self.board_list[y][x-1] != " " :
                self.board_list[y][x-1] = " " 
            # the piece is placed on the edge
            if x-1 < 0 :
                pass
            

            # lower-left
            # the piece is placed in the centre
            if x-1 > 0 and y+1 < self.n-1 and self.board_list[y+1][x-1] != " " :
                if self.board_list[y+2][x-2] == " " :
                    self.board_list[y+2][x-2] = self.board_list[y+1][x-1]
                    self.oard_list[y+1][x-1] = " "
            # the adjacent piece of the placed piece is on the edge
            if (x-1 == 0 or y+1 == self.n-1) and self.board_list[y][x-1] != " " :
                self.board_list[y+1][x-1] = " " 
            # the piece is placed on the edge
            if x-1 < 0 or y+1 > self.n-1:
                pass


            # upper-left
            # the piece is placed in the centre
            if y-1 > 0 and x-1 > 0 and self.board_list[y-1][x-1] != " " :
                if self.oard_list[y-2][x-2] == " " :
                    self.board_list[y-2][x-2] = self.board_list[y-1][x-1]
                    self.board_list[y-1][x-1] = " "
            # the adjacent piece of the placed piece is on the edge
            if (x-1 == 0 or y-1 == 0) and self.board_list[y-1][x-1] != " " :
                self.board_list[y-1][x-1] = " " 
            # the piece is placed on the edge
            if x-1 < 0 or y-1 < 0 :
                pass

            # right
            # the piece is placed in the centre
            if x+1 < self.n-1 and self.board_list[y][x+1] != " " :
                if self.board_list[y][x+2] == " " :
                    self.board_list[y][x+2] = self.board_list[y][x+1]
                    self.board_list[y][x+1] = " "
            # the adjacent piece of the placed piece is on the edge
            if x+1 == self.n-1 and self.board_list[y][x+1] != " " :
                self.board_list[y][x+1] = " " 
            # the piece is placed on the edge
            if x+1 > self.n-1 :
                pass


            # lower-right
            # the piece is placed in the centre
            if x+1 < self.n-1 and y+1 < self.n-1 and self.board_list[y+1][x+1] != " " :
                if self.board_list[y+2][x+2] == " " :
                    self.board_list[y+2][x+2] = self.board_list[y+1][x+1]
                    self.board_list[y+1][x+1] = " "
            # the adjacent piece of the placed piece is on the edge
            if (x+1 == self.n-1 or y+1 == self.n-1) and self.board_list[y+1][x+1] != " " :
                self.board_list[y+1][x+1] = " " 
            # the piece is placed on the edge
            if x+1 > self.n-1 or y+1 > self.n-1 :
                pass


            # upper-right
            # the piece is placed in the centre
            if y-1 > 0 and x+1 < self.n-1 and self.board_list[y-1][x+1] != " " :
                if self.board_list[y-2][x+2] == " " :
                    self.board_list[y-2][x+2] = self.board_list[y-1][x+1]
                    self.board_list[y-1][x+1] = " "
            # the adjacent piece of the placed piece is on the edge
            if (y-1 == 0 or x+1 == self.n-1)and self.board_list[y-1][x+1] != " " :
                self.board_list[y-1][x+1] = " " 
            #the piece is placed on the edge
            if y-1 < 0 or x+1 > self.n-1 :
                pass


            # down
            # the piece is placed in the centre
            if y+1 < self.n-1 and self.board_list[y+1][x] != " " :
                if self.board_list[y+2][x] == " " :
                    self.board_list[y+2][x] = self.board_list[y+1][x]
                    self.board_list[y+1][x] = " "
            # the adjeacent piece of the placed piece is on the edge
            if y+1 == self.n-1 and self.board_list[y+1][x] != " " :
                self.board_list[y+1][x] = " " 
            # the piece is placed on the edge
            if y+1 > self.n-1 :
                pass

            # up
            # the piece is placed in the centre
            if y-1 > 0 and self.board_list[y-1][x] != " " :
                if self.board_list[y-2][x] == " " :
                    self.board_list[y-2][x] = self.board_list[y-1][x]
                    self.board_list[y-1][x] = " "
            # the adjacent piece of the placed piece is on the edge
            if y-1 == 0 and self.board_list[y-1][x] != " " :
                self.board_list[y-1][x] = " " 
            # the piece is placed on the edge
            if y-1 < 0 :
                pass


    def pieces_in_line(self, player):
        win = False
        # checking rows
        for i in range(0, self.n):
            for j in range(0, self.n-2):   
                if self.board_list[i][j] != " " and self.board_list[i][j] == self.board_list[i][j + 1] and self.board_list[i][j + 1] == self.board_list[i][j + 2]:
                    win = True
                    return win
                
        # checking columns
        for i in range(0, self.n-2):
            for j in range(0, self.n):   
                if self.board_list[i][j] != " " and self.board_list[i][j] == self.board_list[i + 1][j] and self.board_list[i + 1][j] == self.board_list[i + 2][j]:
                    win = True
                    return win

        # checking diagonals
        # If have diagonals, then check diagonals elements
        for i in range(0, self.n):
            for j in range(0, self.n):   
                if self.board_list[i][j] != " " and i <= self.n - 3 and j <= self.n - 3 :
                #diagonally to the bottom right
                    if self.board_list[i][j] == self.board_list[i+1][j+1] and self.board_list[i][j] == self.board_list[i+2][j+2] :
                        win = True
                        return win

        # If have diagonals, then check diagonals elements 
        for i in range(0, self.n):
            for j in range(0, self.n):   
                if self.board_list[i][j] != " " and i <= self.n - 3 and j >= self.n - 4 :
                #diagonally to the bottom left
                    if self.board_list[i][j] == self.board_list[i+1][j-1] and self.board_list[i][j] == self.board_list[i+2][j-2] :
                        win = True
                        return win

        # 3 elements lines not detected
        return win

    # join lines/no more piece
    def game_over(self):
        #current one player wins
        if Gekitai.pieces_in_line(self.board_list) == True:
            return True

    # players' current list of pieces
    def print(self):
        #count the no. of pieces on the board
        count_x = self.p
        count_o = self.p
        for i in range(0, self.n):
            for j in range(0, self.n):
                if self.board_list[i][j] == "X":
                    count_x -= 1
                if self.board_list[i][j] == "O":
                    count_o -= 1
        if count_o > 0  and count_x > 0 :
            Board.print_board()
            print("X:",list("X" for i in range(count_x)))
            print("O:",list("O" for j in range(count_o)))
        else:
            Gekitai.game_over(self.board_list) == True

#board[get_piece,print_board~,move~]
#Gekitai[is_move_valid,move,pieces_in_lines,game_over,print_pieces&board,start]
#Piece
#Player[get_input]

    def start(self):
        player = 'X'
        while True:
            Gekitai.print()
            # get user input
            row = Player(player).get_input()[0]
            col = Player(player).get_input()[1] 
            # checking move valid and move
            Gekitai.is_move_valid(row, col) 
            Gekitai.move(player, row, col)
            # checking whether current player won or not
            if Gekitai.game_over() == True :
                print("Game over:")
                Gekitai.print()
                print(f"Player {player} wins!")
                break
            # swapping the turn
            if player == 'X' :
                player = 'O'
            else :
                player = 'X'

    
class Board(Gekitai):
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols 
        self.board_list = [[" "] * cols] * rows
    
    def get_piece(self, y, x):
        if self.board_list[y][x]!= " ":
            return(self.board_list[y][x])
        else:
            return(None)

    def print_board(self):
        print("     A   B   C   D   E   F")
        x="   +---+---+---+---+---+---+"
        for i in range(1,self.rows+1):
            print(x,"\n",i,end=" ")
            for j in range(0,self.cols):
                print("|", self.board_list[i-1][j],end=" ")
                if j == self.cols-1:
                    print("|")
        print(x)
    
    @abstractmethod
    def move(self, piece, y, x):
        pass

    
# start a default game  
from gekitai import Gekitai 
game = Gekitai() 
game.start()
