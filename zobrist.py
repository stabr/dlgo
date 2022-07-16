import random
from dlgo.gotypes import Player, Point

def to_python(player_state):
    if player_state is None:
        return 'None'
    if player_state == Player.black:
        return Player.black
    return Player.white

MAX63 = 0x7fffffffffffffff

table = {}
empty_board = 0
for row in range(1, 20):
    for col in range(1, 20):
        for state in (Player.black, Player.white):
            code = random.randint(0, MAX63)
            table[Point(row, col), state] = code

snippet = '''from .gotypes import Player, Point

'__all__ = ["HASH_CODE", "EMTY_BOARD"]'

HASH_CODE = {'''
print(snippet)
for (pt, state), hash_code in table.items():
    print(f' ({pt}, {to_python(state)}): {hash_code},')
print('}')
print('')
print(f'EMPTY_BOARD = {(empty_board,)}')
