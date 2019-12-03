def loadInput():
    l = []
    with open ("input.txt","r") as f:
        for i in f:
            l.append([i.replace("\n","") for i in i.split(",")])
    return l

def moveWire(grid, currentLocation, command, largestDistance, centralPort, z, t):
    direction = {"R": [0, 1], "L": [0,-1], "D": [1,0], "U": [-1,0]}
    for i in range(int(command[1:])):
        t+=1
        if grid[currentLocation[1]+direction[command[0]][0]*i][currentLocation[0]+direction[command[0]][1]*i] == ".":
            grid[currentLocation[1]+direction[command[0]][0]*i][currentLocation[0]+direction[command[0]][1]*i] = [t,z]

        elif isinstance(grid[currentLocation[1]+direction[command[0]][0]*i][currentLocation[0]+direction[command[0]][1]*i],list) and grid[currentLocation[1]+direction[command[0]][0]*i][currentLocation[0]+direction[command[0]][1]*i][1] != z :
            x = grid[currentLocation[1]+direction[command[0]][0]*i][currentLocation[0]+direction[command[0]][1]*i][0]
            grid[currentLocation[1]+direction[command[0]][0]*i][currentLocation[0]+direction[command[0]][1]*i] = "X"
            dist = x +t
            if dist < largestDistance:
                largestDistance = dist

    currentLocation[0] += direction[command[0]][1]*int(command[1:])
    currentLocation[1] += direction[command[0]][0]*int(command[1:])
    return currentLocation,largestDistance, t

def calcWires(wires):
    grid = [["." for i in range(20000)] for y in range (20000)]
    print("Grid Made")

    largestDistance = 1000000000000000000000
    centralPort = [10000, 10000]
    grid[centralPort[1]][centralPort[0]] = "o"
    for z in range(2):
        t = -1
        currentLocation = centralPort.copy()
        for command in wires[z]:
            currentLocation, largestDistance, t = moveWire(grid, currentLocation, command, largestDistance, centralPort, z, t)
            print("Command Complete")
        print("Wire Complete")
    return largestDistance


wires = loadInput()
print(calcWires(wires))