class Board():
    
    def __init__(self):
        self.moves = []
        
    
    def display(self):
        board = [["-","-","-"],["-","-","-"],["-","-","-"]]
        
        for move in self.moves:
            board[int(move.position[0])][int(move.position[1])] = move.author

        for column in board:
            print(f"{column[0]} {column[1]} {column[2]}")
        

    def add_move(self, move):
        self.moves.append(move)


class Move():

    def __init__(self, author, position):
        self.author = author
        self.position = position


class Player():

    def __init__(self, game_piece, name):
        self.game_piece = game_piece
        self.name = name


class Game():
    
    def __init__(self, board, player_1, player_2):
        self.board = board
        self.player_1 = player_1
        self.player_2 = player_2
        self.started_at = None
        self.finished_at = None



player_1_name = input("Player 1 name: ")
player_2_name = input("player 2 name: ")

player_x = Player("X",player_1_name)
player_o = Player("O",player_2_name)

test_board = Board()
test_game = Game(test_board,player_x,player_o)
test_board.display()

end = False
while end != True:
    x_move = input("Player X move:(00 - 22) ")
    o_move = input("Player O move: (00 - 22) ")
    x_move = Move(player_x.game_piece, x_move)
    o_move = Move(player_o.game_piece, o_move)

    test_board.add_move(x_move)
    test_board.add_move(o_move)
    test_board.display()

    if input("End?") == "y":
        end = True