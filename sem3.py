#задача 1
n = int(import())
def f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return f(n - 1) + f(n - 2)
print(f(n))



#задача 2

def f(n):
   a = 2
   s = []
   while a * a <= n:
       while n % a == 0:
           n = n // a
           s.append(a)
       a += 1
   if n > 1:
       s.append(n)
   return s
n = int(input())
print(f(n))


#задача 4
s00 = list(map(str, input().split()))
r = int(s00[0])
s = s00[1]
def f(i, r, s):
    if i > r:
        return
    if i <= int(r // 2) + 1:
        print(s * i)
    else:
        print(s * (r + 1 - i))
    return f(i + 1, r, s)
f(1, r, s)

