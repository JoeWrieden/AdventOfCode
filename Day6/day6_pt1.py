orbits = {}
with open("input.txt","r") as f:
    for i in f.readlines():
        if i[:3] not in orbits:
            orbits[i[:3]] = []
        orbits[i[:3]].append(i[4:7])

def countOrbits(orb):
    count = 0
    for a in orbits.get(orb, []):
        count += countOrbits(a) + 1
    return count 

total = 0
for i in orbits:
    total+= countOrbits(i)
print(total)