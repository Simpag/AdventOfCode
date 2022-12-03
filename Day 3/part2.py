def prio(letter: str):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return letters.index(letter)+1


def findEqual(arr: list):
    # First split the input
    a, b, c = arr[0], arr[1], arr[2]

    # Convert to them to sets
    a, b, c = set(a), set(b), set(c)

    # Find the intersections
    out = a.intersection(b).intersection(c)

    return list(out)


def solve(file_name: str):
    prioSum = 0
    
    with open(file_name) as f:
        lines = f.readlines()

        i = 0
        while i < len(lines):
            eq = findEqual(lines[i:i+3])

            for letter in eq:
                if letter == '\n':
                    continue
                prioSum += prio(letter)
                print(f'{letter}: {prio(letter)}')

            i += 3

    print(prioSum)


if __name__ == "__main__":
    solve('input_saltanat.txt')
