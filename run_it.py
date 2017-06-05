import time, random
import inflect
from chess import Board, Knight, traverse_board, knights_on_point

inflector = inflect.engine()

def main():
    board = Board()

    print("\n")
    print("#" * 60)
    print("Welcome to Chess")
    print("#" * 60)
    print("\n")

    print("board before traversal")
    print(board)

    count = 1

    while board.incomplete():
        print(inflector.ordinal(count), " traversal\n")
        time.sleep(1)
        print("traversing...")
        time.sleep(2)
        knights = knights_on_point(board)
        traverse_board(board, knights)
        count = count + 1
        print(board)

    time.sleep(2)

    print("\n")
    print("#" * 60)
    print("All paths have been processed")
    print("#" * 60)
    print("\n")
    print("let's look at some examples")

    while True:
        position = [random.randint(0, 7), random.randint(0, 7)]
        print("moves for knight at ", position)
        distance = board.square_at_position(position).distance
        print("knight is ", distance, " moves out")
        single = Board()
        single.square_at_position(position).distance = board.square_at_position(position).distance
        print(single)
        time.sleep(2)

        positions = [position]
        while distance > 0:
            distance = distance - 1
            knight = Knight(positions[-1])
            knight_moves = knight.possible_moves()
            closer_positions = board.positions_matching_distance(distance)
            possibles = [val for val in knight_moves if val in closer_positions]

            positions.append(possibles[0])

        demo = Board()
        for index, position in enumerate(reversed(positions)):
            demo.square_at_position(position).distance = index

        print("results:")
        print(demo)
        time.sleep(4)


if __name__ == "__main__":
    main()