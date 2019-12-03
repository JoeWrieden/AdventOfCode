def loadInput():
    l = []
    with open ("input.txt","r") as f:
        for i in f:
            l.append([i.replace("\n","") for i in i.split(",")])
    return l

def calcDistance(pt1, pt2):
    return abs(pt1[0] - pt2[0]) + abs((pt1[1] - pt2[1]))

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
            if command[0] == "R":
                for i in range(int(command[1:])):
                    if grid[currentLocation[1]][currentLocation[0]+i] == ".":
                        grid[currentLocation[1]][currentLocation[0]+i] = "A"
                    elif grid[currentLocation[1]][currentLocation[0]+i] == "A":
                        grid[currentLocation[1]][currentLocation[0]+i] = "X"
                        temp = currentLocation.copy()
                        temp[0] += i
                        dist = calcDistance(centralPort,temp)
                        if dist < largestDistance:
                            largestDistance = dist

                currentLocation[0] += int(command[1:])


            elif command[0] == "L":
                for i in range(int(command[1:])):
                    if grid[currentLocation[1]][currentLocation[0]-i] == ".":
                        grid[currentLocation[1]][currentLocation[0]-i] = "A"
                    elif grid[currentLocation[1]][currentLocation[0]-i] == "A":
                        grid[currentLocation[1]][currentLocation[0]-i] = "X"
                        temp = currentLocation.copy()
                        temp[0] -= i
                        dist = calcDistance(centralPort,temp)
                        if dist < largestDistance:
                            largestDistance = dist
                currentLocation[0] -= int(command[1:])


            elif command[0] == "D":
                for i in range(int(command[1:])):
                    if grid[currentLocation[1]+i][currentLocation[0]] == ".":
                        grid[currentLocation[1]+i][currentLocation[0]] = "A"
                    elif grid[currentLocation[1]+i][currentLocation[0]] == "A":
                        grid[currentLocation[1]+i][currentLocation[0]] = "X"
                        temp = currentLocation.copy()
                        temp[1] += i
                        dist = calcDistance(centralPort,temp)
                        if dist < largestDistance:
                            largestDistance = dist

                currentLocation[1] += int(command[1:])


            elif command[0] == "U":
                for i in range(int(command[1:])):
                    if grid[currentLocation[1]-i][currentLocation[0]] == ".":
                        grid[currentLocation[1]-i][currentLocation[0]] = "A"
                    elif grid[currentLocation[1]-i][currentLocation[0]] == "A":
                        grid[currentLocation[1]-i][currentLocation[0]] = "X"
                        temp = currentLocation.copy()
                        temp[1] -= i
                        dist = calcDistance(centralPort,temp)
                        if dist < largestDistance:
                            largestDistance = dist
                            
                currentLocation[1] -= int(command[1:])

            print("Command Complete")
        print("Wire Complete")
    return largestDistance

wires = loadInput()

print(printLine(wires))