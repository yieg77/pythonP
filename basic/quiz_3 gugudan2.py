# 구구단 1
for i in range(1, 10):
    #print('--[', end= '')
    #print(str(i), end= '')
    #print('단]--')
    print("\n--[%d단]--"%i)
    for j in range(1, 10):
        #print(str(i)+'*'+str(j)+'='+str(i*j))
        print("%d X %d = %2d" %(i,j,i*j))
    print()


# 구구단 2
for j in range(1, 10):
    for i in range(2, 10):
        #print(str(i)+'*'+str(j)+'='+str(i*j), end='\t')
        #print("%d X %d = %2d" %(i,j,i*j), end = '  ')
        print("{} X {} = {:2}".format(i,j,i*j), end='  ')
    print()
