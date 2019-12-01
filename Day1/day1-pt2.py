def fuel(i):
    if i <= 0:
        return 0
    else:
        return i + fuel(i//3 - 2)

t = 0

with open("input.txt","r") as f:
    for i in f:
        t += fuel(int(i)//3 -2)

print(t)