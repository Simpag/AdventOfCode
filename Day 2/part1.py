def outcome(line : str):
    score = {2: ['A Y', 'B Z', 'C X'], 1: ['A X', 'B Y', 'C Z'], 0: ['A Z', 'B X', 'C Y']}

    res = 0
    for i in score:
        if line in score[i]:
            res = i
            break

    return scoreOfRound(res) + scoreOfShape(line[-1])

def scoreOfShape(shape: str):
    # X: rock, 'Y': paper, 'Z': scissor
    shapes = 'XYZ'
    return shapes.index(shape) + 1

def scoreOfRound(ldw: int):
    # lose : 0, draw : 1, win: 2
    return 3*ldw


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
