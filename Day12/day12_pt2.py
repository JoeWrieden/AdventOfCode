from numpy import lcm
def loadPlanets():
    with open("input.txt", "r") as f:
        planets = []
        for i in f.readlines():
            a = ""
            temp = []
            for x in i:
                if x == "," or x == ">":
                    temp.append(int(a))
                    a = ""
                try:
                    int(x)
                    a+=x
                except ValueError:
                    if x == "-":
                        a+=x
            planets.append([temp, [0,0,0]])
    return planets


def calculateGravity(planets, axis):
    for planet in planets:
        for other in planets:
            if planet != other:
                if planet[0][axis] > other[0][axis]:
                    planet[1][axis] -=1
                elif planet[0][axis] < other[0][axis]:
                    planet[1][axis] += 1
    return planets

def simulateTimeStep(planets, axis):
    planets = calculateGravity(planets, axis)
    for planet in planets:
        planet[0][axis] += planet[1][axis]
    return planets

planets = loadPlanets()

loops = [0, 0, 0]
axisForPrinting = ["x", "y", "z"]
for i in range(3):
    t = 0
    seen = set()
    while True:
        check = []
        planets = simulateTimeStep(planets, i)
        for planet in planets:
            check.append(planet[0][i])
            check.append(planet[1][i])
        if str(check) in seen:
            print("Finished: "+axisForPrinting[i])
            loops[i] = t
            break
        else:
            seen.add(str(check))
        t+=1
print("Step for loop:",lcm(lcm(loops[0], loops[1]), loops[2]))