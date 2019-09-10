a = input('합을 구할 숫자들을 입력하세요.(,로 구분) : ')
a=a.split(',')

print(a)
sum=0
for i in range(len(a)):
    sum+=int(a[i])

print(sum)
