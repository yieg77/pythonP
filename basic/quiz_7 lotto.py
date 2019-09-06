import random

print('=====v1=====')

for i in range(1,6):
    lst = []

    for j in range(1,7):
        while 1:
            a=random.randint(1,45)
            if a not in lst:
                lst.append(a)
                break

    lst.sort()
    print(lst)
    #print(sorted(lst))

print('=====v2=====')

for i in range(5):
    lotto = [0,0,0,0,0,0]
    for x in range(6):
        num=0
        while(num in lotto):
            num = random.randint(1,45)
        lotto[x]=num

    print(sorted(lotto))

print('=====v3=====')

for i in range(1,6):
    print(sorted(random.sample(range(1,46),6)))
