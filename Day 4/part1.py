def containsInPair(a,b):
    return a[0] <= b[0] and a[1] >= b[1]

def solve(file_name: str): 
    total = 0

    with open(file_name) as f:
        lines = f.readlines()

        for line in lines:
            line = line.split(',')
            a = line[0]
            b = line[1]
            a = a.split('-')
            b = b.split('-')

            a = [int(x) for x in a]
            b = [int(x) for x in b]

            if containsInPair(a,b) or containsInPair(b,a):
                total += 1

    print(total)



if __name__ == "__main__":
    solve('input_simon.txt')
