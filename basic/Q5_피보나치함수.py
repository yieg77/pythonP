n = input("n값을 입력하세요 : ")

a=[0, 1]

for i in range(int(n)-2):
    #a.append(int(a[i])+int(a[i+1]))
    a.append(a[i]+a[i+1])

print(a)
