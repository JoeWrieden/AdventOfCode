with open("input.txt", "r") as f:
    line = [int(c) for c in f.read().replace("\n", "")]
pattern = [0, 1, 0, -1]

def getPattern(pattern, level):
    n = []
    for i in pattern:
        n+= [i] * level
    return n


def cycle(line, pattern):
    fin = []
    for i in range(len(line)):
        res = 0
        newpattern = getPattern(pattern, i+1)
        for j in range(len(line)):   
            res+= line[j] * newpattern[(j+1)%len(newpattern)]   
        fin.append(abs(res)%10)
    return fin


for i in range(100):
    line = cycle(line, pattern)


for x in range(8):
    print(line[x], end="")
print()