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


def calculateGravity(planets):
    for planet in planets:
        for other in planets:
            if planet != other:
                for axis in range(3):
                    if planet[0][axis] > other[0][axis]:
                        planet[1][axis] -=1
                    elif planet[0][axis] < other[0][axis]:
                        planet[1][axis] += 1
    return planets

def simulateTimeStep(planets):
    planets = calculateGravity(planets)
    for planet in planets:
        for i in range(3):
            planet[0][i] += planet[1][i]
    return planets

def calculateEnergy(planets):
    tot = 0
    for planet in planets:
        pot = 0
        kin = 0
        for i in range(3):
            pot+= abs(planet[0][i])
            kin += abs(planet[1][i])
        tot += (kin*pot)
    return tot


planets = loadPlanets()
for i in range(1000):
    planets = simulateTimeStep(planets)
print(calculateEnergy(planets))