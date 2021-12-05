from commons import *

def solution1(input_file):
    input = readToArray(input_file)
    transposed = transpose(input)
    most_common = []
    least_common = []
    for each_line in transposed:
        most_and_least_commons = find_most_and_least_common(each_line)
        most_common.append(most_and_least_commons[0])
        least_common.append(most_and_least_commons[1])

    gamma = int(''.join(most_common), 2)
    epsilon = int(''.join(least_common), 2)
    return gamma * epsilon


def solution2(input_file):
    input = readToArray(input_file)
    oxygen_rating = do_filter(input, True)
    co2_scrbber_rating = do_filter(input, False)
    return int(oxygen_rating[0], 2) * int(co2_scrbber_rating[0], 2)


def do_filter(arr, most_common = True, pos = 0):
    bits = [arr[i][pos] for i in range(len(arr))]
    zeroes = len(list(filter(lambda b: b == '0', bits)))
    ones = len(list(filter(lambda b: b == '1', bits)))
    bit_to_match = find_bit_to_match(zeroes, ones, most_common)

    filtered = list(filter(lambda each_line: each_line[pos] == bit_to_match, arr))
    if len(filtered) > 1:
        return do_filter(filtered, most_common, pos+1)
    else:
        return filtered


def find_bit_to_match(zeroes_len, ones_len, most_common):
    if most_common:
        return '0' if zeroes_len > ones_len else '1'
    else:
        return '1' if zeroes_len > ones_len else '0'


def find_most_and_least_common(line):
    zeroes = 0
    ones = 0
    for v in line:
        if v == '0':
            zeroes += 1
        else:
            ones += 1
    if zeroes > ones:
        return ('0', '1')
    else:
        return ('1', '0')


#print(solution1('day3-input.txt'))
print(solution2('day3-input.txt'))
