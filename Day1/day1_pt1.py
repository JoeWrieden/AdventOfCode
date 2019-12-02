t = 0
with open("input.txt", "r") as f:
    for i in f:
        t += (int(i)//3 -2)

print(t)