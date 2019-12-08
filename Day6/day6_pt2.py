orbits = {}
with open("input.txt","r") as f:
    for i in f.readlines():
        if i[4:7] not in orbits:
            orbits[i[4:7]] = []
        orbits[i[4:7]].append(i[0:3])

def meet(orb):
    traverse = []
    while orb[0] != "COM":
        traverse.append(orb)
        orb = orbits[orb[0]]
    return traverse

def findPaths():
    sanPath = meet(["SAN"])
    youPath = meet(["YOU"])
    same = [i for i in sanPath if i in youPath]
    for i in same:
        youPath.remove(i)
        sanPath.remove(i)
    return youPath+sanPath

print(len(findPaths()) -2)