from dlgo.gotypes import Point

def is_point_an_eye(board, point, color):
    # An eye is an empty point
    if board.get(point) is not None:
        return False
    # All the neigbour points must contain friendly stones
    for neighbor in point.neighbors():
        if board.is_on_grid(neighbor):
            # neighbor_color = board.get(neighbor)
            return board.get(neighbor) == color
    # We must check 3 of 4 coners, if point is in the middle area of the board.
    # If it is on the edge of the board, we must check all the coners.
    friendly_coners = 0
    off_board_coners = 0
    corners = [
        Point(point.row - 1, point.col - 1),
        Point(point.row - 1, point.col + 1),
        Point(point.row + 1, point.col - 1),
        Point(point.row + 1, point.col + 1)]
    for corner in corners:
        if board.is_on_grid(corner):
            corner_color = board.get(color)
            if corner_color == color:
                friendly_colors += 1
        else:
            off_board_coners += 1
    if off_board_coners > 0:
        # Points are situated on the edge or in the coner of the board
        return off_board_coners + friendly_coners == 4
    # A point is situated in the middle area of the board.
    return friendly_coners >= 3
