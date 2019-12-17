import numpy

with open("input.txt", "r") as f:
    line = numpy.array([int(c) for c in f.read().replace("\n", "")] * 10000)

offset = ""
for i in range(7):
    offset += str(line[i])
offset = int(offset)

line = line[offset:]

for i in range(100):
    line = line[::-1]
    line = numpy.cumsum(line) %10
    line = line[::-1]

for x in range(8):
    print(line[x], end="")
print()