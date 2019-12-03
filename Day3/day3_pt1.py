def loadInput():
    l = []
    with open ("input.txt","r") as f:
        for i in f:
            l.append([i.replace("\n","") for i in i.split(",")])
    return l

def calcDistance(pt1, pt2):
    return abs(pt1[0] - pt2[0]) + abs((pt1[1] - pt2[1]))

def moveWire(grid, currentLocation, command, largestDistance, centralPort):
    direction = {"R": [0, 1], 
                  "L": [0,-1],
                  "D": [1,0],
                  "U": [-1,0]}

    for i in range(int(command[1:])):
        if grid[currentLocation[1]+direction[command[0]][0]*i][currentLocation[0]+direction[command[0]][1]*i] == ".":
            grid[currentLocation[1]+direction[command[0]][0]*i][currentLocation[0]+direction[command[0]][1]*i] = "A"
        elif grid[currentLocation[1]+direction[command[0]][0]*i][currentLocation[0]+direction[command[0]][1]*i] == "A":
            grid[currentLocation[1]+direction[command[0]][0]*i][currentLocation[0]+direction[command[0]][1]*i] = "X"
            temp = currentLocation.copy()
            temp[0] += direction[command[0]][1]*i
            temp[1] += direction[command[0]][0]*i
            dist = calcDistance(centralPort,temp)
            if dist < largestDistance:
                largestDistance = dist

    currentLocation[0] += direction[command[0]][1]*int(command[1:])
    currentLocation[1] += direction[command[0]][0]*int(command[1:])
    return currentLocation,largestDistance

l = loadInput()
def printLine(wires):
    largestDistance = 1000000000000000000000
    grid = [["." for i in range(20000)] for y in range (20000)]
    print("Grid Made")
    centralPort = [10000, 10000]
    grid[centralPort[1]][centralPort[0]] = "o"
    for z in range(2):
        currentLocation = centralPort.copy()
        for command in wires[z]:
            currentLocation, largestDistance = moveWire(grid, currentLocation, command, largestDistance, centralPort)

            print("Command Complete")
        print("Wire Complete")
    return largestDistance

wires = loadInput()

print(printLine(wires))