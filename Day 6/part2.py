def importStacks(lines: list[str], stacks: list[list]):
    # 1   2   3   4   5   6   7   8   9
    indexMap = [1, 5, 9, 13, 17, 21, 25, 29, 33] 
    lines.reverse() # so we read from bottom to top
    for line in lines:
        for i in indexMap:
            if line[i].isalpha():
                stacks[indexMap.index(i)].append(line[i])

    return stacks


def followInstruction(inst: str, stacks: list[list]):
    inst = inst.split(' ') # ex: move 3 from 6 to 2
    stacksToMove = int(inst[1])
    moveFrom = int(inst[3])-1
    moveTo = int(inst[5])-1
    

    print(f'Move: {stacksToMove} from {moveFrom+1} to {moveTo+1} - StackFrom: {stacks[moveFrom]} StackTo: {stacks[moveTo]}')
    itemsToMove = stacks[moveFrom][-stacksToMove:]
    
    del stacks[moveFrom][-stacksToMove:] # remove the items to move
    stacks[moveTo] += itemsToMove # add them in the new stack

    return stacks


def getTopCrates(stacks: list[list]):
    ret = ''
    for stack in stacks:
        ret += str(stack[-1])
    
    return ret


def solve(file_name: str): 
    stacks = [[] for i in range(9)]

    with open(file_name) as f:
        lines = f.readlines()

        stacks = importStacks(lines[:8], stacks)

        lines = lines[10:] # remove the stacks and the blank line so we're only left with instructions

        for line in lines:
            stacks = followInstruction(line, stacks)

    print(getTopCrates(stacks))


if __name__ == "__main__":
    solve('input_saltanat.txt')
