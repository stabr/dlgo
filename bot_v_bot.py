import time
from agent.naive import RandomBot
from gotypes import Player
from goboard_slow import GameState
from utils import print_board, print_move

def main(board_size=9):
    game = GameState.new_game(board_size)
    bots = {
        str(Player.black): RandomBot(),
        str(Player.white): RandomBot()}
    while not game.is_over():
        time.sleep(0.3)
        print(chr(27) + '[2]')
        print_board(game.board)
        bot_move = bots[str(game.next_player)].select_move(game)
        print_move(game.next_player, bot_move)
        game = game.apply_move(bot_move)


if __name__ == '__main__':
    main()
    