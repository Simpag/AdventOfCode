def big_num(elves: list):
    res = 0
    mysum = 0
    for elf in elves:
        mysum = sum(elf)
        if res < mysum:
            res = mysum

    return res
            

def solve(file_name: str):
    elves = [[],]
    
    with open(file_name) as f:
        lines = f.readlines()
        
        for line in lines:
            if line == '\n':
                elves.append([])
                continue
            
            elves[-1].append(int(line))

    print(elves)
    mostCalories = big_num(elves)

    print(mostCalories)


if __name__ == "__main__":
    solve('input_simon.txt')
