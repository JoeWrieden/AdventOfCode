import math
def loadMap():
    l = []
    with open("input.txt", "r") as f:
        for i in f.readlines():
            l.append([x for x in i.replace("\n","")])
    return l

asteroidMap = loadMap()
asteriods = []

for y in range(len(asteroidMap)):
    for x in range(len(asteroidMap[y])):
        if asteroidMap[y][x] == "#":
            asteriods.append((x,y))
    
print(asteriods)
mostSeen = 0
for curr in asteriods:
    canSee = []
    for look in asteriods:
        if look != curr:
            yDiff = curr[1] - look[1]
            xDiff = look[0] - curr[0]
            canSee.append(math.atan2(xDiff, yDiff)) 
    canSee = set(canSee)
    if len(canSee) > mostSeen:
        mostSeen = len(canSee)
        p = curr
print(p)