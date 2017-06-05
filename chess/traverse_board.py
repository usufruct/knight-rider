from .knight import Knight

def traverse_board(board, knights):
    for knight in knights:
        distance = board.square_at_position(knight.position).distance
        knight_moves = knight.possible_moves()
        allowed_moves = board.in_bounds(knight_moves)
        unmeasured_positions = board.infinite_positions(allowed_moves)

        for position in unmeasured_positions:
            board.square_at_position(position).distance = distance + 1

def knights_on_point(board):
    farthest = board.biggest_measured_distance()
    positions = board.positions_matching_distance(farthest)

    return [Knight(p) for p in positions]