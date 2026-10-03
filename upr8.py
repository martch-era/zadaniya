#упражнение 8 с семинара 4
x = [1, 33, 27, 890, 65, 43, 43, 890, 97]
y = [2, 3, 33, 43, 28, 762, 2, 2, 33, 97]
print(*[i for i in x if x.count(i) == 1])
print(*[i for i in y if y.count(i) == 1])
print(*[i for i in x if i in y and x.count(i) == 1 and y.count(i) == 1])
print(set(x).union(set(y)))
