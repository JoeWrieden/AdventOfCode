import itertools
def intCodeComputer(intCode, inputs, position):
    l = intCode.copy()
    i = position
    while True:
        i %= len(l)
        op = l[i] % 100
        ad1 = (l[i] // 100) %10
        ad2 = (l[i]//1000) % 10


        if op == 99:
            return x, None, None

        elif op == 1:
            if ad1 == 0:
                ac1 = l[l[i+1]]
            else:
                ac1 = l[i+1]
            if ad2 == 0:
                ac2 = l[l[i+2]]
            else:
                ac2 = l[i+2]
            l[l[i+3]] = ac1 + ac2
            i+=4

        elif op == 2:
            if ad1 == 0:
                ac1 = l[l[i+1]]
            else:
                ac1 = l[i+1]
            if ad2 == 0:
                ac2 = l[l[i+2]]
            else:
                ac2 = l[i+2]
            l[l[i+3]] = ac1 * ac2
            i+=4

        elif op == 3:
            l[l[i+1]] = inputs.pop(0)
            i+=2

        elif op == 4:
            if ad1 == 0:
                ac1 = l[l[i+1]]
            else:
                ac1 = l[i+1]
            i += 2
            return ac1, l, i

        elif op == 5:
            if ad1 == 0:
                ac1 = l[l[i+1]]
            else:
                ac1 = l[i+1]
            if ad2 == 0:
                ac2 = l[l[i+2]]
            else:
                ac2 = l[i+2]
            if ac1 != 0:
                i = ac2
            else:
                i+=3

        elif op == 6:
            if ad1 == 0:
                ac1 = l[l[i+1]]
            else:
                ac1 = l[i+1]
            if ad2 == 0:
                ac2 = l[l[i+2]]
            else:
                ac2 = l[i+2]
            if ac1 == 0:
                i = ac2
            else:
                i+=3     

        elif op == 7:
            if ad1 == 0:
                ac1 = l[l[i+1]]
            else:
                ac1 = l[i+1]
            if ad2 == 0:
                ac2 = l[l[i+2]]
            else:
                ac2 = l[i+2]
            
            if ac1 < ac2:
                l[l[i+3]] = 1
            else:
                l[l[i+3]] = 0
            i+=4
        
        elif op == 8:
            if ad1 == 0:
                ac1 = l[l[i+1]]
            else:
                ac1 = l[i+1]
            if ad2 == 0:
                ac2 = l[l[i+2]]
            else:
                ac2 = l[i+2]
            
            if ac1 == ac2:
                l[l[i+3]] = 1
            else:
                l[l[i+3]] = 0
            i+=4
            
         
        elif op == 7:
            if ad1 == 0:
                ac1 = l[l[i+1]]
            else:
                ac1 = l[i+1]
            if ad2 == 0:
                ac2 = l[l[i+2]]
            else:
                ac2 = l[i+2]
            
            if ac1 < ac2:
                l[l[i+3]] = 1
            else:
                l[l[i+3]] = 0
            i+=4
        
        elif op == 8:
            if ad1 == 0:
                ac1 = l[l[i+1]]
            else:
                ac1 = l[i+1]
            if ad2 == 0:
                ac2 = l[l[i+2]]
            else:
                ac2 = l[i+2]
            
            if ac1 == ac2:
                l[l[i+3]] = 1
            else:
                l[l[i+3]] = 0
            i+=4


def readIntCode():
    with open("input.txt","r") as f:
        for line in f:
            intCode = [int(i) for i in line.split(",")]
    return intCode



if __name__ == "__main__":
    intCode = readIntCode()
    maximums = []
    for ampSetting in itertools.permutations([5,6,7,8,9]):

        codes = [intCode.copy() for i in range(5)]
        positions = [0 for i in range(5)]
        inputs = [[ampSetting[i]] for i in range(5)]
        inputs[0].append(0)

        done = False
        while not done:
            for amp in range(5):
                x, codes[amp], positions[amp] = intCodeComputer(codes[amp], inputs[amp], positions[amp])
                if isinstance(codes[amp], list):
                    inputs[(amp+1)%5].append(x)
                else:
                    maximums.append(x)
                    done = True
                    break
    print(max(maximums))