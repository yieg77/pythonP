test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

print('===============')

a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)

print('===============')

sum = 0
for i in range(1, 101):
    if i%2==0 :
        sum = sum + i

print(sum)
