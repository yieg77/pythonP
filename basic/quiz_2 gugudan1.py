"%10s"%("first")

"{:^10}".format("hi")



num = int(input('출력하고 싶은 구구단이 몇 단인가요?\n'))

print('--[', end= '')
print(str(num), end= '')
print('단]--\n')
for i in range(1, 10):
    "{0:^10}".format("hi")
    #"{0:^10}".format(str(num)+'*'+str(i)+'='+str(num*i))
    #print(str(num)+'*'+str(i)+'='+str(num*i)+'\n')

