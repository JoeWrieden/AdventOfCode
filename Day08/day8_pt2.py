with open("input.txt", "r") as f:
    imageCode = f.read().replace("\n","")
largestZero = 100000
largestZeroLayer = 0
image = ["2" for i in range(150)]
for i in range(100):
    for j in range(150*i, 150*i+150):
        if imageCode[j] != "2":
            if image[j%150] == "2":
                image[j%150] = imageCode[j]
for j in range(6):
    for i in range(25):
        print("\033[1;3"+image[i+25*j]+";40m"+image[i + 25*j], end="")
    print()