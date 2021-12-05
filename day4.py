from commons import *
import functools


def read_input(input_file):
    curr = 0
    draws = []
    boards = []
    curr_board = []
    with open(input_file, "r") as f:
        for each_line in f:
            if curr == 0:
                draws = each_line.strip()
            else:
                if len(each_line.strip()) == 0:
                    if len(curr_board) > 0:
                        boards.append(curr_board)
                        curr_board = []
                else:
                    curr_board.append(list(map(lambda c: int(c), list(filter(lambda s: s != '', each_line.strip().split(' '))))))
            curr += 1
        if len(curr_board) > 0:
            boards.append(curr_board)

    return (draws, boards)


def solution1(input_file):
    (draws, boards) = read_input(input_file)
    draws = list(map(lambda c: int(c), draws.split(',')))
    for d in draws:
        for i in range(len(boards)):
            if bingo(boards[i], d):
                return cal_board_value(boards[i], d)


def solution2(input_file):
    (draws, boards) = read_input(input_file)
    draws = list(map(lambda c: int(c), draws.split(',')))
    last_board_to_win = -1
    max_draw = -1
    for i in range(len(boards)):
        for x in range(len(draws)):
            if not check_bingo(boards[i]):
                if bingo(boards[i], draws[x]) and x > max_draw:
                    max_draw = x
                    last_board_to_win = i

    return cal_board_value(boards[last_board_to_win], draws[max_draw])


def bingo(board, draw):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if draw == board[i][j]:
                board[i][j] = -1
    return check_bingo(board)


def check_bingo(board):
    for each_row in board:
        if check_row(each_row):
            return True
    transposed = transpose(board)
    for each_row in transposed:
        if check_row(each_row):
            return True
    return False


def check_row(row):
    if functools.reduce(lambda a, b: a+b, row) == -1*5:
        return True
    else:
        return False


def cal_board_value(board, steps):
    sum = 0
    for each_row in board:
        for each_index in each_row:
            if each_index != -1:
                sum += each_index
    return sum*steps


print(solution2('day4-input.txt'))


