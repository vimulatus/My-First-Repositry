import math


min,max = input().strip().split(' ')
min,max = [int(min),int(max)]
# your code goes here

def mindiff(n, d):
    diff1 = math.pi - n/d
    diff2 = (n+1)/d - math.pi
    if (diff1 - diff2) > 0:
        return diff2, n+1, d
    else:
        return diff1, n, d

n = math.floor(math.pi*min)
diff, a, b = mindiff(n, min)

for d in range(min + 1, max + 1):
    n = math.floor(math.pi*d)
    i, j, k = mindiff(n, d)
    if (diff - i) > 0:
        diff = i
        a = j
        b = k
print("{}/{}".format(a, b))
