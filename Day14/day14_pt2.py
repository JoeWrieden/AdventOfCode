import math
def loadTable():
    table = {}
    useNum = {}
    with open("input.txt", "r") as f:
        for line in f.readlines():
            inp, output  = line.strip().split(" => ")
            count, out = output.split()
            temp = []

            for x in inp.split(", "):
                inCount, inVal = x.split()
                if inVal not in useNum:
                    useNum[inVal] = 0
                useNum[inVal] += 1

                temp.append((int(inCount), inVal))
            table[out] = (int(count), temp)
    return table, useNum

def calculateUsage(toFind, FuelToFind):
    table, useNum = loadTable()
    useNum["FUEL"] = 0
    need = {"FUEL":FuelToFind}
    while len(useNum) > 1:
        for element in useNum:
            if useNum[element] == 0:
                numberNeeded = need[element]
                count, inputs = table[element]
                amountToCreate = math.ceil(numberNeeded/count)
                for toCount, toVal in inputs:
                    if toVal not in need:
                        need[toVal] = 0
                    need[toVal] += toCount * amountToCreate
                    useNum[toVal] -= 1
                del useNum[element]
                break
    return need[toFind]

def calculateForOre(numOfOre):
    i = 10000
    x = 1
    t = 0
    while True:
        while t < numOfOre:
            t = calculateUsage("ORE", x)
            x += i
        x -= i*2
        t = calculateUsage("ORE", x)

        if i == 1:
            return x
        else:
            i//=10

print(calculateForOre(1000000000000))