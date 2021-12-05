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