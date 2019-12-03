def loadInput():
    l = []
    with open ("input.txt","r") as f:
        for i in f:
            l.append([i.replace("\n","") for i in i.split(",")])
    return l

def calcGridSize(wires):
    x = y = u = d = l = r = 0
    dim = []
    for wire in wires:
        for command in wire:
            if command[0] == "R":
                x += int(command[1:])
                if x > r:
                    r = x
            elif command[0] == "L":
                x -= int(command[1:])
                if x < l:
                    l = x
            elif command[0] == "D":
                y += int(command[1:])
                if y > d:
                    d = y
            elif command[0] == "U":
                y -= int(command[1:])
                if y < u:
                    u = y
        dim.append([x,y,r,l,d,u])
    r = max([dim[0][2],dim[1][2]])
    l = min([dim[0][3],dim[1][3]])
    d = max([dim[0][4],dim[1][4]])
    u = min([dim[0][5],dim[1][5]])
    return [(r-l)+2, (d-u)+2], [(-l), (-u)]

def calcDistance(pt1, pt2):
    return abs(pt1[0] - pt2[0]) + abs((pt1[1] - pt2[1]))

def moveWire(grid, currentLocation, command, largestDistance, centralPort):
    direction = {"R": [0, 1], "L": [0,-1], "D": [1,0], "U": [-1,0]}
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

def calcWires(wires):
    gridsize, centralPort = calcGridSize(wires)
    grid = [["." for i in range(gridsize[0])] for y in range (gridsize[1])]
    print("Grid Made")

    largestDistance = 1000000000000000000000
    grid[centralPort[1]][centralPort[0]] = "o"
    for z in range(2):
        currentLocation = centralPort.copy()
        for command in wires[z]:
            currentLocation, largestDistance = moveWire(grid, currentLocation, command, largestDistance, centralPort)
            print("Command Complete")
        print("Wire Complete")
    return largestDistance

wires = loadInput()
print(calcWires(wires))