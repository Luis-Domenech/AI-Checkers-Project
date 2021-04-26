# Assets: https://techwithtim.net/wp-content/uploads/2020/09/assets.zip
import csv
import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE, WHITE_NAME, RED_NAME
from checkers.game import Game
from minimax.ai_vs_ai import minimax
# from minimax.algorithm import minimax

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main(games = 10):

    winners = []

    for i in range(games):
        clock = pygame.time.Clock()
        game = Game(WIN)

        while True:
            clock.tick(FPS)

            ############## comment when playing human vs ai #################
            if game.turn == RED:
                value, new_board = minimax(game.get_board(), 4, RED, game)
                
                # This means we lost since we have no possible good moves
                if new_board is None:
                    print("Game", i, "Winner:", WHITE_NAME)
                    winners.append(WHITE_NAME)
                    break

                game.ai_move(new_board)

                if game.winner() is not None:
                    print("Game", i, "Winner:", game.winner())
                    winners.append(game.winner())
                    break
            #################################################################

            if game.turn == WHITE:
                value, new_board = minimax(game.get_board(), 4, WHITE, game)

                # This means we lost since we have now possible good moves
                if new_board is None:
                    print("Game", i, "Winner:", RED_NAME)
                    winners.append(RED_NAME)
                    break

                game.ai_move(new_board)

                if game.winner() is not None:
                    print("Game", i, "Winner:", game.winner())
                    winners.append(game.winner())
                    break
            

            game.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)
                    game.select(row, col)

    pygame.quit()

    with open('winners.csv', mode='w') as csv_file:
        fieldnames = ['game', 'winner']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        for i in range(len(winners)):
            writer.writerow({'game': i + 1, 'winner': winners[i]})

main()