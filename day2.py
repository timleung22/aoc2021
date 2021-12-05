from commons import *

def solution1(input_file):
    forward = 0
    depth = 0
    input = readToTuples(input_file)
    for each_tuple in input:
        if each_tuple[0] == 'forward':
            forward += int(each_tuple[1])
        elif each_tuple[0] == 'down':
            depth += int(each_tuple[1])
        elif each_tuple[0] == 'up':
            depth -= int(each_tuple[1])
        else:
            raise RuntimeError('unexpected input')

    return forward * depth


def solution2(input_file):
    forward = 0
    depth = 0
    aim = 0
    input = readToTuples(input_file)
    for each_tuple in input:
        operation = each_tuple[0]
        value = int(each_tuple[1])
        if operation == 'forward':
            forward += value
            depth += aim*value
        elif operation == 'down':
            aim += value
        elif operation == 'up':
            aim -= value
        else:
            raise RuntimeError('unexpected input')

    return forward * depth


print(solution1('day2-input.txt'))

print(solution2('day2-input.txt'))