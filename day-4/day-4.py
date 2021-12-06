import copy
import functools
# Read File


def read_file(filename):
    """
    Reads in Test File line by line and adds to list

    Args:
        filename (string): Filename/Filepath

    Returns:
        list{list}: List of commands represented by dictionaries
    """
    pulled_nums = None
    boards = []
    with open(filename, 'r') as f:
        board = []
        for line in f:
            stripped = line.strip()
            # Append to board-list
            if stripped == '':
                if pulled_nums != None and len(board) != 0:
                    boards.append(board)
                    board = []
                    continue
                else:
                    continue
            # Found pulled numbers line
            elif ',' in stripped:
                pulled_nums = [int(x) for x in stripped.split(',')]
            # Split on white space and then remove whitespace again
            else:
                split_once = stripped.split(' ')
                split_final = [int(x) for x in split_once if x != '']
                board.append(split_final)
        # append the last board as well
        boards.append(board)

    return (pulled_nums, boards)


def print_board(board):
    for row in board:
        print(row)
    print("")

# Part 1


def get_solution(board, last_pulled):
    sum_unmarked = 0
    for row in board:
        for x in row:
            if x != -1:
                sum_unmarked += x
    return (sum_unmarked, last_pulled, (sum_unmarked * last_pulled))


def check_win(board):
    for i in range(5):
        # Do row check
        row_check = [board[i][j] == -1 for j in range(5)]
        if not(False in row_check):
            return True
        # Do column check
        column_check = [board[j][i] == -1 for j in range(5)]
        if not(False in column_check):
            return True
    return False


def play_bingo(pulled_nums: list, boards: list):
    res_boards = copy.deepcopy(boards)
    for y, pulled_number in enumerate(pulled_nums):
        for i in range(len(res_boards)):
            if check_win(res_boards[i]):
                return get_solution(res_boards[i], pulled_nums[y-1])
            for j in range(len(res_boards[i])):
                for x in range(len(res_boards[i][j])):
                    if res_boards[i][j][x] == pulled_number:
                        res_boards[i][j][x] = -1

# Part 2


def play_bingo_squid_wins(pulled_nums: list, boards: list):
    res_boards = copy.deepcopy(boards)
    boards_won = []
    for y, pulled_number in enumerate(pulled_nums):
        for i in range(len(res_boards)):
            if check_win(res_boards[i]):
                if not(i in boards_won):
                    boards_won.append(i)
                if len(boards_won) == len(res_boards):
                    return get_solution(res_boards[boards_won[-1]], pulled_nums[y-1])
            for j in range(len(res_boards[i])):
                for x in range(len(res_boards[i][j])):
                    if res_boards[i][j][x] == pulled_number:
                        res_boards[i][j][x] = -1


input_pulled, input_boards = read_file("input.txt")
test_pulled, test_boards = read_file("test.txt")

unmarked, last_pulled, solution_part_1 = play_bingo(input_pulled, input_boards)
unmarked_2, last_pulled_2, solution_part_2 = play_bingo_squid_wins(
    input_pulled, input_boards)

print(
    f"Solution (Part 1): Unmarked: {unmarked}, Last Pulled Number: {last_pulled}, Solution: {solution_part_1}")
print(
    f"Solution (Part 2): Unmarked: {unmarked_2}, Last Pulled Number: {last_pulled_2}, Solution: {solution_part_2}")
