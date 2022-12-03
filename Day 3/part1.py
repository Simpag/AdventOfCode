def prio(letter: str):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return letters.index(letter)+1


def findEqual(arr: list):
    # First split the input
    a, b = arr[:len(arr)//2], arr[len(arr)//2:]

    # Convert to them to sets
    a, b = set(a), set(b)

    # Find the intersections
    out = a.intersection(b)

    return list(out)


def solve(file_name: str):
    prioSum = 0
    
    with open(file_name) as f:
        lines = f.readlines()

        for line in lines:
            eq = findEqual(line)
            
            for letter in eq:
                prioSum += prio(letter)
                print(f'{letter}: {prio(letter)}')

    print(prioSum)


if __name__ == "__main__":
    solve('input_saltanat.txt')
