import random

cnt_o = 0
a=['+','-','*','/']
#print(random.random())
#print(random.randint(1, 10))
#print(random.choice(a))  # 중복허용
#print(random.sample)  # 중복X
#random.shuffle(a)
#print(a)

for i in range(1,6):
    quiz = str(random.randint(1,100)) + random.choice(a) +str(random.randint(1,100))
    print(quiz+' = ', end='')
    ans = int(eval(quiz))

    print(ans)
    user_ans = input()

    if str(ans) == user_ans:
        print('정답')
        cnt_o += 1
    else:
        print('오답')

print(str(cnt_o)+'개 맞음')
