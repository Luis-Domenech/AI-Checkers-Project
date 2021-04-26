from copy import deepcopy
import pygame

RED = (255, 0, 0)
WHITE = (255, 255, 255)

def minimax(position, depth, max_player, game):
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position
    
    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, WHITE, game):
            evaluation = minimax(move, depth-1, False, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move
        
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, RED, game):
            evaluation = minimax(move, depth-1, True, game)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move
        
        return minEval, best_move

def alpha_beta_search(position, color, depth,game):
    infinity = float('inf')
    best_val = -infinity
    beta = infinity
    best_move = None 

    for move in get_all_moves(position, color, game):
        value = min_value(game, position, depth, best_val, beta, color)
            
        if value > best_val:
            best_val = value
            best_move = position
                
                
    return best_move, best_val

def max_value(game, position, depth, alpha, beta, color):
    infinity = float('inf')
    best_val = -infinity
          
    for move in get_all_moves(position, color, game):
        evaluation = minimax(move, depth-1, False, game)[0]
        value = max(beta, evaluation)
            
        if value >= beta:
            return value
            
            
                
        alpha =  max(alpha, evaluation)

    return value
        

def min_value(game, position, depth, alpha, beta, color):
    infinity = float('inf')
    value = infinity
    for move in get_all_moves(position, color, game):
        evaluation = minimax(move, depth-1, True, game)[0]
        value = min(alpha, evaluation)
            
        if value <= alpha:
            return value
            
            
        beta =  min(beta, evaluation)

    return value

def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board


def get_all_moves(board, color, game):
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            # draw_moves(game, board, piece)
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)
    
    return moves


def draw_moves(game, board, piece):
    valid_moves = board.get_valid_moves(piece)
    board.draw(game.win)
    pygame.draw.circle(game.win, (0,255,0), (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()
    #pygame.time.delay(100)

