def checkIfDifferent(arr: str):
    # arr = 'abcd'
    buffer = []

    for i in arr:
        if i in buffer:
            return False

        buffer.append(i)

    return True


def getMarkerIndex(line: str):
    i = 0
    while i < len(line):
        if checkIfDifferent(line[i:i+4]):
            break
        i += 1

    return i+4


def solve(file_name: str): 
    res = 0

    with open(file_name) as f:
        lines = f.readlines()

        for line in lines:
            res = getMarkerIndex(line)

    print(res)


if __name__ == "__main__":
    solve('input_simon.txt')
