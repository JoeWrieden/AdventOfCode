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
        t = -1
        currentLocation = centralPort.copy()
        for command in wires[z]:
            if command[0] == "R":
                for i in range(int(command[1:])):
                    t += 1
                    if grid[currentLocation[1]][currentLocation[0]+i] == ".":
                        grid[currentLocation[1]][currentLocation[0]+i] = [t,z]
                    elif isinstance(grid[currentLocation[1]][currentLocation[0]+i],list) and grid[currentLocation[1]][currentLocation[0]+i][1] != z :
                        x = grid[currentLocation[1]][currentLocation[0]+i][0]
                        grid[currentLocation[1]][currentLocation[0]+i] = "X"
                        dist = x +t
                        if dist < largestDistance:
                            largestDistance = dist
                            print("\nAAAAAA\n")

                currentLocation[0] += int(command[1:])


            elif command[0] == "L":
                for i in range(int(command[1:])):
                    t += 1
                    if grid[currentLocation[1]][currentLocation[0]-i] == ".":
                        grid[currentLocation[1]][currentLocation[0]-i] = t
                    elif isinstance(grid[currentLocation[1]][currentLocation[0]-i],list) and grid[currentLocation[1]][currentLocation[0]-i][1] != z:
                        x = grid[currentLocation[1]][currentLocation[0]-i][0]
                        grid[currentLocation[1]][currentLocation[0]-i] = "X"
                        dist = x +t
                        if dist < largestDistance:
                            largestDistance = dist
                            print("\nAAAAAA\n")
                currentLocation[0] -= int(command[1:])


            elif command[0] == "D":
                for i in range(int(command[1:])):
                    t += 1
                    if grid[currentLocation[1]+i][currentLocation[0]] == ".":
                        grid[currentLocation[1]+i][currentLocation[0]] = t
                    elif isinstance(grid[currentLocation[1]+i][currentLocation[0]],list) and grid[currentLocation[1]+i][currentLocation[0]][1] != z:
                        x = grid[currentLocation[1]+i][currentLocation[0]][0]
                        grid[currentLocation[1]+i][currentLocation[0]] = "X"
                        dist = x + t
                        if dist < largestDistance:
                            largestDistance = dist
                            print("\nAAAAAA\n")

                currentLocation[1] += int(command[1:])


            elif command[0] == "U":
                for i in range(int(command[1:])):
                    t += 1
                    if grid[currentLocation[1]-i][currentLocation[0]] == ".":
                        grid[currentLocation[1]-i][currentLocation[0]] = t
                    elif isinstance(grid[currentLocation[1]-i][currentLocation[0]],list) and grid[currentLocation[1]-i][currentLocation[0]][1] != z:
                        x = grid[currentLocation[1]-i][currentLocation[0]][0]
                        grid[currentLocation[1]-i][currentLocation[0]] = "X"
                        dist = x +t
                        if dist < largestDistance:
                            largestDistance = dist
                            print("\nAAAAAA\n")
                currentLocation[1] -= int(command[1:])

            print("Command Complete")
        print("Wire Complete")

    return largestDistance


wires = loadInput()

print(printLine(wires))