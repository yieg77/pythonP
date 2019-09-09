def add(a, b):
    return a+b

print(add(3,5))

print(add(b=5, a=3))

def add_many(*args):
    result = 0
    for i in args:
        result += i

    return result

print(add_many(1, 2, 3, 4, 5, 5))


#매개변수 초깃값 설정
def say_myself(name, old, woman=True):
    print('나의 이름은 %s입니다.' %name)
    print('나의 나이는 %d살입니다.' %old)
    if woman: print('여자입니다.')
    else: print('남자입니다.')

say_myself('yeg', 10)
