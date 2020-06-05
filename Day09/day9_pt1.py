def intCodeComputer(intCode, inputs):
    l = intCode.copy()
    i = 0
    relativeBase = 0
    while True:
        i %= len(l)
        op = l[i] % 100


        if op == 99:
            break

        elif op == 1:
            ac1 = returnValue(l, i, relativeBase, 1)
            ac2 = returnValue(l, i, relativeBase, 2)
            st3 = returnValue(l, i, relativeBase, 3)
            l[st3] = l[ac1] + l[ac2]
            i+=4

        elif op == 2:
            ac1 = returnValue(l, i, relativeBase, 1)
            ac2 = returnValue(l, i, relativeBase, 2)
            st3 = returnValue(l, i, relativeBase, 3)
            l[st3] = l[ac1] * l[ac2]
            i+=4

        elif op == 3:
            st3 = returnValue(l, i, relativeBase, 3)
            l[st3] = inputs.pop(0)
            i+=2

        elif op == 4:
            ac1 = returnValue(l, i, relativeBase, 1)
            print(l[ac1])
            i+=2

        elif op == 5:
            ac1 = returnValue(l, i, relativeBase, 1)
            ac2 = returnValue(l, i, relativeBase, 2)
            if l[ac1] != 0:
                i = l[ac2]
            else:
                i+=3

        elif op == 6:
            ac1 = returnValue(l, i, relativeBase, 1)
            ac2 = returnValue(l, i, relativeBase, 2)
            if l[ac1] == 0:
                i = l[ac2]
            else:
                i+=3   

        elif op == 7:
            ac1 = returnValue(l, i, relativeBase, 1)
            ac2 = returnValue(l, i, relativeBase, 2)
            st3 = returnValue(l, i, relativeBase, 3)
            
            if l[ac1] < l[ac2]:
                l[st3] = 1
            else:
                l[st3] = 0
            i+=4
        
        elif op == 8:
            ac1 = returnValue(l, i, relativeBase, 1)
            ac2 = returnValue(l, i, relativeBase, 2)
            st3 = returnValue(l, i, relativeBase, 3)
            
            if l[ac1] == l[ac2]:
                l[st3] = 1
            else:
                l[st3] = 0
            i+=4
            
        elif op == 9:
            ac1 = returnValue(l, i, relativeBase, 1)

            relativeBase += l[ac1]
            i+=2
            
            
            

    return l

def returnValue(l, i, relativeBase, pos):
    ad = (l[i] // (10 * 10**pos)) % 10

    if ad == 0:
        ac = l[i+pos]
    elif ad == 2:
        ac = l[i+pos]+relativeBase
    else:
        ac = i+pos
    return ac
def readIntCode():
    with open("input.txt","r") as f:
        for line in f:
            intCode = [int(i) for i in line.split(",")]
    intCode += [0] * 9999999
    return intCode


if __name__ == "__main__":
    intCode = readIntCode()
    intCodeComputer(intCode, [1])