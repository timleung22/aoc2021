from commons import readToArray


def solution1(input_file):
    depths = list(map(lambda a: int(a), readToArray(input_file)))
    return find_increasing(depths)


def solution2(input_file):
    depths = list(map(lambda a: int(a), readToArray(input_file)))
    curr = 0
    windowed_depths = []
    while curr < len(depths) - 2:
        windowed_depths.append(depths[curr] + depths[curr+1] + depths[curr+2])
        curr += 1
    return find_increasing(windowed_depths)


def find_increasing(depths):
    curr = 1
    inc = 0
    while curr < len(depths):
        if depths[curr-1] < depths[curr]:
            inc += 1
        curr += 1
    return inc


print(solution1('d1-input1.txt'))

print(solution2("d1-input1.txt"))