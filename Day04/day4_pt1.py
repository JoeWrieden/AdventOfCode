def passCheck(num):
    strNum = str(num)
    for i in range(len(strNum)-1):
        if strNum[i+1] < strNum[i]:
            return False
    
    for n in strNum:
        if strNum.count(n) >=2:
            return True
    return False

n = 0

for i in range (402328,864247):
    if passCheck(i):
        n+= 1
print(n)