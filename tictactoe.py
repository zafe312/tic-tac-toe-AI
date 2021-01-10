import random
from copy import deepcopy

X='X'
O='O'
EMPTY='EMPTY'

def initial_state():
    return [[EMPTY,EMPTY,EMPTY],[EMPTY,EMPTY,EMPTY],[EMPTY,EMPTY,EMPTY]]


def terminal(board):
    status = 0
    if board[0].count(EMPTY)+board[1].count(EMPTY)+board[2].count(EMPTY)==0:
        status = 1
    else:
        if board[0][0]==board[1][1]==board[2][2]!=EMPTY or board[2][0]==board[1][1]==board[0][2]!=EMPTY:
            status = 1
        else:
            for i in range(3):
                if board[i][0]==board[i][1]==board[i][2]!=EMPTY or board[0][i]==board[1][i]==board[2][i]!=EMPTY:
                    status = 1
                    break
    if status == 1:
        return True
    else:
        return False
    
    
    
    
def winner(board):
    winr=''
    if board[0][0]==board[1][1]==board[2][2]==X or board[2][0]==board[1][1]==board[0][2]==X:
            winr = 'X'
    elif board[0][0]==board[1][1]==board[2][2]==O or board[2][0]==board[1][1]==board[0][2]==O:
            winr = 'O'
    else:
        for i in range(3):
            if board[i][0]==board[i][1]==board[i][2]==X or board[0][i]==board[1][i]==board[2][i]==X:
                winr = 'X'
                break
            elif board[i][0]==board[i][1]==board[i][2]==O or board[0][i]==board[1][i]==board[2][i]==O:
                winr = 'O'
                break
    if winr == '' and board[0].count(EMPTY)+board[1].count(EMPTY)+board[2].count(EMPTY)==0:
        winr = None
    return winr






# This function returns true if there are moves 
# remaining on the board. It returns false if 
# there are no moves left to play. 
def isMovesLeft(board) : 
 
    for i in range(3) :
        for j in range(3) :
            if (board[i][j] == EMPTY) :
                return True
    return False

def evaluate(b, depth) : 
   
    # Checking for Rows for X or O victory. 
    for row in range(3) :     
        if (b[row][0] == b[row][1] and b[row][1] == b[row][2]) :        
            if (b[row][0] == 'X') :
                return 10 - depth
            elif (b[row][0] == 'O') :
                return -10 + depth
 
    # Checking for Columns for X or O victory. 
    for col in range(3) :
      
        if (b[0][col] == b[1][col] and b[1][col] == b[2][col]) :
         
            if (b[0][col] == 'X') : 
                return 10 - depth
            elif (b[0][col] == 'O') :
                return -10 + depth
 
    # Checking for Diagonals for X or O victory. 
    if (b[0][0] == b[1][1] and b[1][1] == b[2][2]) :
     
        if (b[0][0] == 'X') :
            return 10 - depth
        elif (b[0][0] == 'O') :
            return -10 + depth
 
    if (b[0][2] == b[1][1] and b[1][1] == b[2][0]) :
     
        if (b[0][2] == 'X') :
            return 10 - depth
        elif (b[0][2] == 'O') :
            return -10 + depth
 
    # Else if none of them have won then return 0 
    return 0

def minimax_score(board, depth, isMax) : 
    board_copy = deepcopy(board)
    
    score = evaluate(board, depth)
 
    if winner(board) != '' : 
        return [score,(4,4)]
 
    # If there are no more moves and no winner then 
    # it is a tie 
    if (isMovesLeft(board) == False) :
        return [0,(4,4)]
    
    depth += 1
    score = []
    moves = []
    
    if isMax:
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    new_board = result(board_copy,(i,j))
                    board_copy = deepcopy(board)
                    score.append(minimax_score(new_board,depth,False)[0])
                    moves.append((i,j))
    else:
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    new_board = result(board_copy,(i,j))
                    board_copy = deepcopy(board)
                    score.append(minimax_score(new_board,depth,True)[0])
                    moves.append((i,j))
                
    if isMax:
        return [max(score),moves[score.index(max(score))]]
    else:
        return [min(score),moves[score.index(min(score))]]
    
# This will return the best possible move for the player 
def minimax(board):
    # make copy of board
    board_copy = deepcopy(board)
    
    # before using minimax algorithm, check whether you can win in single move, otherwise check if opposition is about to win

    # if board is empty: return a corner position
    corner_pos = [(0,0),(0,2),(2,0),(2,2)]
    if board == initial_state():
        return corner_pos[random.randrange(4)]
    # else if board is almost empty with an X at a corner: return (1,1)
    elif board == [[X,EMPTY,EMPTY],[EMPTY,EMPTY,EMPTY],[EMPTY,EMPTY,EMPTY]] or board == [[EMPTY,EMPTY,X],[EMPTY,EMPTY,EMPTY],[EMPTY,EMPTY,EMPTY]] or board == [[EMPTY,EMPTY,EMPTY],[EMPTY,EMPTY,EMPTY],[X,EMPTY,EMPTY]] or board == [[EMPTY,EMPTY,EMPTY],[EMPTY,EMPTY,EMPTY],[EMPTY,EMPTY,X]]:
        return (1,1)
    else:
        #loop through available positions of the board: nodes: check for winning move
        for i in range(3):
            for j in range(3):
                if board[i][j]==EMPTY:
                    # if X is playing
                    if player(board) == 'X':
                        # evaluate node: first move
                        u = utility(result(board_copy,(i,j)))
                        board_copy = deepcopy(board)
                        # check if this move makes X win, i.e node score == 1: immediately return this position
                        if u == 1:
                            return (i,j)
                    # if O is playing
                    else:
                        # evaluate node
                        u = utility(result(board_copy,(i,j)))
                        board_copy = deepcopy(board)
                        # check if this move makes O win, i.e node score == -1: immediately return this position
                        if u == -1:
                            return (i,j)

        #loop again if opposite is about to win
        for i in range(3):
            for j in range(3):
                if board[i][j]==EMPTY:
                    # if X is playing
                    if player(board) == 'X':
                        # check if making this move makes O win in the next move, i.e. node score of next move == -1: immediately return this position
                        v = utility(result_opp(board_copy,(i,j)))
                        board_copy = deepcopy(board)
                        if v == -1:
                            return (i,j)

                    # if O is playing
                    else:
                        # check if making this move makes X win in the next move: immediately return this position
                        v = utility(result_opp(board_copy,(i,j)))
                        board_copy = deepcopy(board)
                        if v == 1:
                            return (i,j)
    
    if player(board) == 'X':
        return minimax_score(board, 0, True)[1]
    else:
        return minimax_score(board, 0, False)[1]
    
    
    
def result(board, move):
    temp_board=board
    temp_board[move[0]][move[1]]=player(board)
    return temp_board

def result_opp(board, move):
    temp_board=board
    if player(board)=='X':
        temp_board[move[0]][move[1]]='O'
    else:
        temp_board[move[0]][move[1]]='X'
    return temp_board
    
# gives scores to terminal boards based on winner       
def utility(board):
    if terminal(board)==True:
        if winner(board) == 'X':
            return 1
        elif winner(board) == 'O':
            return -1
        elif winner(board) == None:
            return 0
    else:
        return 2 # board is not terminal

    
def player(board):
    X=0
    O=0
    for i in range(3):
        X+=board[i].count('X')
        O+=board[i].count('O')
    if X>O:
        return 'O'
    else:
        return 'X'