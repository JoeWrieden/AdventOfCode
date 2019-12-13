import os
class IntCode():
    def __init__(self, intCode):
        self.intCode = intCode
        self.i = 0
        self.relativeBase = 0

    def run(self, inputs):
        while True:
            self.i %= len(self.intCode)
            op = self.intCode[self.i] % 100

            if op == 99:
                return None
            elif op == 1:
                ac1 = self.getValue(1)
                ac2 = self.getValue(2)
                str3 = self.getAddressingMode(3)
                self.intCode[str3] = ac1 + ac2
                self.i += 4
            elif op == 2:
                ac1 = self.getValue(1)
                ac2 = self.getValue(2)
                str3 = self.getAddressingMode(3)
                self.intCode[str3] = ac1 * ac2
                self.i += 4
            elif op == 3:
                str1 = self.getAddressingMode(1)
                self.intCode[str1] = inputs.pop(0)
                self.i += 2
            elif op == 4:
                ac1 = self.getValue(1)
                self.i += 2
                return ac1
            elif op == 5:
                ac1 = self.getValue(1)
                ac2 = self.getValue(2)
                if ac1 == 1:
                    self.i = ac2
                else:
                    self.i+=3
            elif op == 6:
                ac1 = self.getValue(1)
                ac2 = self.getValue(2)
                if ac1 == 0:
                    self.i = ac2
                else:
                    self.i+=3
            elif op == 7:
                ac1 = self.getValue(1)
                ac2 = self.getValue(2)
                str3 = self.getAddressingMode(3)
                if ac1<ac2:
                    self.intCode[str3] = 1
                else:
                    self.intCode[str3] = 0
                self.i += 4
            elif op == 8:
                ac1 = self.getValue(1)
                ac2 = self.getValue(2)
                str3 = self.getAddressingMode(3)
                if ac1==ac2:
                    self.intCode[str3] = 1
                else:
                    self.intCode[str3] = 0
                self.i += 4
            elif op == 9:
                ac1 = self.getValue(1)
                self.relativeBase += ac1
                self.i += 2

    def getAddressingMode(self, pos):
        ad = (self.intCode[self.i] // (10 * 10**pos)) % 10

        if ad == 0:
            ac = self.intCode[self.i+pos]
        elif ad == 1:
            ac  = self.i+pos
        elif ad == 2:
            ac = self.intCode[self.i+pos]+self.relativeBase
        return ac
    
    def getValue(self, pos):
        return self.intCode[self.getAddressingMode(pos)]

def readIntCode():
    with open("input.txt","r") as f:
        intCode = [int(i) for i in f.read().split(",")]
    intCode += [0] * 9999999
    return intCode

def countBlock(grid):
    blockCount = 0
    for i in grid:
        for x in i:
            if x == 2:
                blockCount += 1
    return blockCount

def createboard(arcadeMachine, move):
    arcadeMachine.i = 0
    grid = [[0 for i in range(35)] for j in range(25)]
    loop = True
    while loop:
        x = y = 0
        for i in range(3):
            n = arcadeMachine.run([move])
            if n == None:
                loop = False
                break
            elif i == 0:
                x = n
            elif i == 1:
                y = n
            else:
                grid[y][x] = n
                if n == 4:
                    ball = x
                elif n == 3:
                    padd = x
    if ball < padd:
        return grid, arcadeMachine, -1
    elif ball > padd:
        return grid, arcadeMachine, 1
    else:
        return grid, arcadeMachine, 0

def printGrid(grid):
    os.system("clear")
    for i in grid:
        for x in i:
            if x > 4:
                print("\033[1;36;40m"+str(x), end="")
            else:
                print("\033[1;3"+str(x)+";40m"+str(x), end="")
        print()


intCode = readIntCode()
intCode[0] = 2
move = 0
arcadeMachine = IntCode(intCode)

autoMode = 0

while True:
    if autoMode:
        grid, arcadeMachine, move = createboard(arcadeMachine, move)
    else:
        try:
            move = int(input("-1 = left, 0 = stay, 1 = right: "))
        except ValueError:
            move = 0
        grid, arcadeMachine, move = createboard(arcadeMachine, move)
    
    printGrid(grid)
    if not countBlock(grid):
        break