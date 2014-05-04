def conflict(nextX, nowX):
    for i in nowX:
        if (nextX == i or abs(len(nowX) - nowX.index(i)) == abs(nextX - i)):
            return True
    return False

def cal(num, nowX):
    for i in range(0,num):
        if not conflict(i,nowX):
            #nowX.append(i)
            print "1"
            return i

tmp = []
n = 0
num = input("input num: ")
while (n < num):
    tmp.append(cal(num, tmp))
    print tmp
    n = n + 1
print tmp
