with open("input.txt", "r") as f:
    imageCode = f.read().replace("\n","")
largestZero = 100000
largestZeroLayer = 0
for i in range(100):
    zeroCount = 0
    for j in range(150*i, 150*i+150):
        if imageCode[j] == "0":
            zeroCount+=1
    if zeroCount < largestZero:
        largestZero = zeroCount
        largestZeroLayer = i
oneCount = 0
twoCount = 0
for k in range(150*largestZeroLayer, 150*largestZeroLayer+150):
    if imageCode[k] == "1":
        oneCount+=1
    elif imageCode[k] == "2":
        twoCount+=1
    


print(oneCount*twoCount)