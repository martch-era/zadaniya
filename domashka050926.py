#задание 2
a = int(input())
print(a%10)

#задание 4
f = open('input.txt')
g = open('output.txt', 'w')
sp = []
for l in f:
    sp.append(l)
a = list(map(int, sp[0][:-1].split()))
if sp[1] == '+':
    su = 0
    for i in a:
        su += i
    g.write(su)
elif sp[1] == '-':
    res = a[0]
    for i in range(1, len(a)):
        res -= a[i]
    g.write(res)
elif sp[1] == '*':
    mul = 1
    for i in a:
        mul*=i
    g.write(mul)
f.close()
g.close()

#задание 6
f = open('input.txt')
g = open('output.txt', 'w')
sp = []
for l in f:
    sp.append(l)
a = list(map(str, sp[0][:-1].split()))
b = int(sp[2])
aa =[]
for i in a:
    aa.append(int(i, b))
if sp[1][0] == '+':
    su = 0
    for i in aa:
        su += i
    x1 =''
    while su>0:
        x1 += str(su%b)
        su //= b
    x = x1[::-1]
    g.write(x)
elif sp[1][0] == '-':
    res = aa[0]
    for i in range(1, len(aa)):
        res -= aa[i]
    x1 =''
    r1 = abs(res)
    while r1>0:
        x1 += str(r1%b)
        r1 //= b
    x = '-'+x1[::-1]
    g.write(x)
elif sp[1][0] == '*':
    mul = 1
    for i in aa:
        mul*=i
    x1 =''
    while mul>0:
        x1 += str(mul%b)
        mul //= b
    x = x1[::-1]
    g.write(x)
f.close()
g.close()
