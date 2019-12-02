from day2_pt1 import intCodeComputer, readIntCode

intCode = readIntCode()

intCode[1] = 12
intCode[2] = 2
while intCodeComputer(intCode)[0] <= 19690720:
    intCode[1]+=1
intCode[1]-=1

while intCodeComputer(intCode)[0] != 19690720:
    intCode[2]+= 1

print(100*intCode[1] +intCode[2])