def intCodeComputer(intCode):
    l = intCode.copy()
    i = 0
    while l[i] != 99:
        if l[i] == 1:
            ac1 = l[l[i+1]]
            ac2 = l[l[i+2]]
            l[l[i+3]] = ac1 + ac2

        elif l[i] == 2:
            ac1 = l[l[i+1]]
            ac2 = l[l[i+2]]
            l[l[i+3]] = ac1 * ac2

        i+=4
    return l
def readIntCode():
    with open("input.txt","r") as f:
        for line in f:
            intCode = [int(i) for i in line.split(",")]
    return intCode


if __name__ == "__main__":
    intCode = readIntCode()
    intCode[1] = 12
    intCode[2] = 2
    print(intCodeComputer(intCode))        