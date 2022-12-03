def big_num(elves: list):

    calories = []
    for i in elves:
        calories.append(sum(i))

    calories.sort(reverse=True)
        
    return sum(calories[0:3])
            

def solve(file_name: str):
    elves = [[],]
    
    with open(file_name) as f:
        lines = f.readlines()
        
        for line in lines:
            if line == '\n':
                elves.append([])
                continue
            
            elves[-1].append(int(line))

    #print(elves)
    mostCalories = big_num(elves)

    print(mostCalories)


if __name__ == "__main__":
    solve('input_saltanat.txt')
