import math
def loadMap():
    l = []
    with open("input.txt", "r") as f:
        for i in f.readlines():
            l.append([x for x in i.replace("\n","")])
    return l

def loadAsteroids():
    asteroidMap = loadMap()
    asteriods = []
    for y in range(len(asteroidMap)):
        for x in range(len(asteroidMap[y])):
            if asteroidMap[y][x] == "#":
                asteriods.append((x,y))
    return asteriods

def takeFirst(elem):
    return elem[0]

def lazerLoop():
    destroyNum = 1
    station = (37, 25)
    asteriods = loadAsteroids()
    while True:
        canSee, asteriodsSeen = discoverAsteriods(asteriods, station)
        astAng = [[canSee[i], asteriodsSeen[i]] for i in range(len(canSee))]

        pos = []
        neg = []
        for asteroid in astAng:
            if asteroid[0] > 0.0:
                pos.append(asteroid)
            else:
                neg.append(asteroid)

        pos = sorted(pos, key=takeFirst)
        neg = sorted(neg, key=takeFirst)

        for i in pos:
            asteriods.remove(i[1])
            destroyNum+=1
            if destroyNum == 200:
                return i
        for i in neg:
            asteriods.remove(i[1])
            destroyNum+=1
            if destroyNum == 200:
                return i

def discoverAsteriods(asteriods, curr):
    canSee = []
    asteroidsSeen = []
    for look in asteriods:
        if look != curr:
            yDiff = curr[1] - look[1]
            xDiff = look[0] - curr[0]
            if math.atan2(xDiff, yDiff) not in canSee:
                canSee.append(math.atan2(xDiff, yDiff))
                asteroidsSeen.append(look)
    return canSee, asteroidsSeen

print(lazerLoop())
