import random, time

input('엔터키를 누르면 게임이 시작됩니다!')
print('<<게임 시작>>')
time_start=time.time()

word_list=['start', 'python', 'artificial', 'bigdata', 'computer']

for i in range(5):
    print(str(i+1)+'번째 문제 : ', end = '')
    #quiz=word_list[random.randint(0, 4)]\
    quiz = random.choice(word_list)
    print(quiz)

    while 1 :
        print('>> ', end='')
        user_input = input()
        if user_input==quiz :
            break

time_end=time.time()

print('<<게임 끝>> - 소요시간 : {:.2f}초'.format(time_end-time_start))
