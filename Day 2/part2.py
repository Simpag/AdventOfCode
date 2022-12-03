def outcome(line : str):
    score = {'X': ['A Y', 'C Z', 'B X'], 'Y': ['A Z', 'B Y', 'C X'], 'Z': ['B Z', 'A X', 'C Y']}

    res = ''
    for i in score:
        if line in score[i]:
            res = i
            break

    return scoreOfRound(line[-1]) + scoreOfShape(res)

def scoreOfShape(shape: str):
    # X: rock, 'Y': paper, 'Z': scissor
    shapes = 'XYZ'
    return shapes.index(shape) + 1

def scoreOfRound(requiredResult: str):
    # lose: X, draw: Y, win: Z
    shapes = 'XYZ'
    return 3*shapes.index(requiredResult)


def solve(file_name: str):
    totalScore = 0
    
    with open(file_name) as f:
        lines = f.readlines()

        for line in lines:
            line = line.strip()
            totalScore += outcome(line)
            print(f'{line}: {outcome(line)}')

    print(totalScore)


if __name__ == "__main__":
    solve('input_saltanat.txt')
