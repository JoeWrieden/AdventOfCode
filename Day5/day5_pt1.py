def intCodeComputer(intCode):
    l = intCode.copy()
    i = 0
    while True:
        op = l[i] % 100
        ad1 = (l[i] // 100) %10
        ad2 = (l[i]//1000) % 10


        if op == 99:
            break

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
            s = int(input("Enter an int: "))
            l[l[i+1]] = s
            i+=2

        elif op == 4:
            if ad1 == 0:
                ac1 = l[l[i+1]]
            else:
                ac1 = l[i+1]
            print(ac1)
            i+=2    
            

    return l
def readIntCode():
    with open("input.txt","r") as f:
        for line in f:
            intCode = [int(i) for i in line.split(",")]
    return intCode


if __name__ == "__main__":
    intCode = readIntCode()
    intCodeComputer(intCode)