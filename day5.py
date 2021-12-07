from commons import *


def solution1(input_file):
    input = readToArray(input_file)
    lines = list(map(lambda i: text_to_coords(i), input))
    h_or_v_lines = list(filter(lambda line: line[0][0] == line[1][0] or line[0][1] == line[1][1], lines))
    grid = build_grid(999, 0)
    for each_h_or_v in h_or_v_lines:
        mark_line_on_grid(each_h_or_v, grid)

    dangers = 0
    for i in range(999):
        for j in range(999):
            if grid[i][j] >= 2:
                dangers += 1
    return dangers


def solution2(input_file):
    input = readToArray(input_file)
    lines = list(map(lambda i: text_to_coords(i), input))
    h_or_v_lines = list(filter(lambda line: line[0][0] == line[1][0] or line[0][1] == line[1][1], lines))
    diagonal_lines = list(filter(lambda line: abs(line[0][0]-line[1][0]) == abs(line[0][1]-line[1][1]), lines))
    grid = build_grid(999, 0)
    for each_h_or_v in h_or_v_lines:
        mark_line_on_grid(each_h_or_v, grid)
    for each_diag in diagonal_lines:
        mark_diag_line_on_grid(each_diag, grid)

    dangers = 0
    for i in range(999):
        for j in range(999):
            if grid[i][j] >= 2:
                dangers += 1
    return dangers


def mark_line_on_grid(line, grid):
    if line[0][0] == line[1][0]:
        # x equals, so this is a vertical line
        for j in range(min(line[0][1], line[1][1]), max(line[0][1], line[1][1])+1):
            grid[line[0][0]][j] += 1
    elif line[0][1] == line[1][1]:
        # horizontal line
        for i in range(min(line[0][0], line[1][0]), max(line[0][0], line[1][0])+1):
            grid[i][line[0][1]] += 1
    else:
        raise RuntimeError('unexpected')


def mark_diag_line_on_grid(line, grid):
    start_x = min(line[0][0], line[1][0])
    end_x = max(line[0][0], line[1][0]) + 1
    slope = (line[0][1] - line[1][1]) / (line[0][0] - line[1][0])
    if slope > 0:
        y = min(line[0][1], line[1][1])
        for x in range(start_x, end_x):
            grid[x][y] += 1
            y += 1
    else:
        y = max(line[0][1], line[1][1])
        for x in range(start_x, end_x):
            grid[x][y] += 1
            y -= 1


print(solution2('day5-input.txt'))