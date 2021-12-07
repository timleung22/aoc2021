def readToArray(filename):
    output = []
    with open(filename, "r") as f:
        for eachLine in f:
            output.append(eachLine.strip())
    return output


def readToTuples(filename):
    result = []
    with open(filename, "r") as f:
        for eachLine in f:
            result.append(tuple(eachLine.strip().split(' ')))
    return result


def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


def build_grid(size, init_value):
    return [[init_value for j in range(size)] for i in range(size)]


def text_to_coords(line):
    # line should be like 364,765 -> 364,285
    pairs = line.split(' -> ')
    return list(map(lambda p: tuple(map(lambda c: int(c), p.split(','))), pairs))


