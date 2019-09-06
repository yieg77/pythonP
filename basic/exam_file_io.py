"""
f = open("./basic/test1.txt", 'w')
for i in range(1,11):
    #data = "%d번째 줄입니다.\n" %i
    data = "{}번째 줄입니다.\n".format(i)
    f.write(data)
f.close()
"""

"""
f = open("./basic/test1.txt", 'r')
while 1:
    line = f.readline()
    line = line.replace('\n', '')
    if not line: break
    print(line)
    #print(line, end='')
f.close()

print("==================")
"""

"""
f = open("./basic/test1.txt", 'r')

lines = f.readlines()
for i in lines:
    new_i = i.replace('\n', '')
    print(new_i)

f.close()

print("==================")
"""

"""
f = open("./basic/test1.txt", 'r')

data = f.read()
print(data)

f.close()

print("==================")
"""

"""
f = open("./basic/test2.txt", 'r', encoding='utf-8')

lines = f.readlines()
for i in lines:
    new_i = i.replace('\n', '')
    print(new_i)

f.close()
"""

# file close 안해도 되는 코드
with open("./basic/test2.txt", 'r', encoding='utf-8') as f:
    f.write("Life is too short, you need python")
