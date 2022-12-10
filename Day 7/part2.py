class Dir:
    def __init__(self, name: str, parent):
        self.name = name
        self.bytes:int = 0 
        self.dirs: dict[str,Dir]  = {}
        self.parent:Dir = parent

    def __repr__(self) -> str:
        return f'- {self.name} (size={self.bytes})'

class RootDir:
    def __init__(self):
        self.currentDir:Dir = self
        self.bytes:int = 0 
        self.dirs: dict[str,Dir] = {} 
        # {'a' : Dir, 'c' : Dir}
        # a dirs: {'b': Dir}

    def printTree(self):
        print(self)
        for dir in self.dirs:
            self._printTree(self.dirs[dir], '  ')

    def _printTree(self, parent: Dir, indentation):
        print(indentation + str(parent))
        for dir in parent.dirs:
            self._printTree(parent.dirs[dir], indentation+'  ')

    def addBytes(self):
        res = 0
        for dir in self.dirs:
            res += self._addBytes(self.dirs[dir])

        self.bytes += res

    def _addBytes(self, parent: Dir):
        res = 0
        for dir in parent.dirs:
            res += self._addBytes(parent.dirs[dir])

        parent.bytes += res
        return parent.bytes

    def findDirToFreeSpace(self, requiredSpace: int):
        dirToRemove = ['/', self.bytes]

        for dir in self.dirs:
            self._findDirToFreeSpace(self.dirs[dir], dirToRemove, requiredSpace)

        return dirToRemove

    def _findDirToFreeSpace(self, parent: Dir, currentDirToRemove: list[str, int], requiredSpace: int):
        if parent.bytes >= requiredSpace and parent.bytes < currentDirToRemove[1]:
            currentDirToRemove[0] = parent.name
            currentDirToRemove[1] = parent.bytes

        for dir in parent.dirs:
            self._findDirToFreeSpace(parent.dirs[dir], currentDirToRemove, requiredSpace)

    def __repr__(self) -> str:
        return f'- / (size={self.bytes})' 


def makeMove(root: RootDir, terminalOut: str):
    # cd X => change rootDir currentDir
    # ls => do nothing
    # cd .. => change rootDir currentDir to parent of currentDir
    if terminalOut == '$ ls':
        return
    
    # else its a cd
    terminalOut = terminalOut.split(' ')
    movDir = terminalOut[-1]

    if movDir == '/':
        root.currentDir = root
    elif movDir == '..':
        root.currentDir = root.currentDir.parent
    else:
        subDirs = root.currentDir.dirs
        if movDir in subDirs:
            root.currentDir = root.currentDir.dirs[movDir]
        else:
            root.currentDir.dirs[movDir] = Dir(name= movDir, parent=root.currentDir)
            root.currentDir = root.currentDir.dirs[movDir]

def saveBytes(root: RootDir, terminalOut: str):
    a = terminalOut.split(' ')
    root.currentDir.bytes += int(a[0])

def saveDir(root: RootDir, terminalOut: str):
    dirName = terminalOut.split(' ')[1]
    if dirName in root.currentDir.dirs:
        return
    root.currentDir.dirs[dirName] = Dir(name = dirName, parent=root.currentDir)

def solve(file_name: str): 
    root = RootDir()

    with open(file_name) as f:
        lines = f.readlines()

        for line in lines:
            line = line.strip()
            if line[0] == '$':
                makeMove(root, line)
            elif line[0] == 'd':
                saveDir(root, line)
            else:
                saveBytes(root, line)


    root.addBytes()
    totalUsedSpace = root.bytes
    spaceLeft = 70_000_000 - totalUsedSpace
    spaceNeeded = 30_000_000 - spaceLeft
    
    dirToRemove = root.findDirToFreeSpace(spaceNeeded)

    print(dirToRemove)


if __name__ == "__main__":
    solve('input_saltanat.txt')
