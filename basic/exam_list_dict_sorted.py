score = [23, 45, 67, 34, 100, 98]
names= {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245, 'Michale':27115, 'Bob':5887, 'Kelly':7855}

score.sort()
print(score)

def f1(x):
    return x[0]

def f2(x):
    return x[1]

res = sorted(names.items(), key=f1, reverse = True)
print(res)

res = sorted(names.items(), key=f2)
print(res)

res = sorted(names.items(), key=(lambda x:x[1]), reverse = True)
print(res)

