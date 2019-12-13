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
    intCode += [0] * 999
    return intCode


def paintingRobot(intCode):
    computer = IntCode(intCode)
    
    directionsX = [0, 1, 0, -1]
    directionsY = [1, 0, -1, 0]
    direction = 0
    painted = []
    grid = [[0 for i in range(200)] for j in range(200)]
    x = y = 100
    toPaint = computer.run([grid[y][x]])
    toDir= computer.run([])

    while toPaint != None:
        grid[y][x] = toPaint
        painted.append((x, y))
        if toDir == 0:
            if direction == 0:
                direction = 3
            else:
                direction-=1
        elif toDir == 1:
            if direction == 3:
                direction = 0
            else:
                direction+=1

        x += directionsX[direction]
        y += directionsY[direction]

        toPaint = computer.run([grid[y][x]])
        toDir= computer.run([])
    
    return len(set(painted))
                

if __name__ == "__main__":
    intCode = readIntCode()
    print(paintingRobot(intCode))

    