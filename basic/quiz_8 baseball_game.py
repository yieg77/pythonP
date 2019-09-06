import random, time

ans = random.sample(range(1,10),3)
print('ans',ans)

cnt_try = 0
cnt_strike = 0
time_start=time.time()
while cnt_strike<3 :
    user_try=list(input('숫자를 맞춰보세요!\n'))
    cnt_try+=1
    print(user_try)

    cnt_strike = 0
    cnt_ball = 0
    cnt_out = 0
    for i in range(3):
        for j in range(3):
            if int(user_try[i]) == ans[j]:
                if i==j:
                    cnt_strike+=1
                else:
                    cnt_ball+=1

        if int(user_try[i]) not in ans:  
            cnt_out+=1
    
    print(str(cnt_try)+'번째 시도', end=' : ')
    print(str(cnt_strike)+'S '+str(cnt_ball)+'B '+str(cnt_out)+'O')

    if cnt_strike==3:
        time_end = time.time()
        print('[정답] - 소요시간 : {:.0f}초'.format(time_end-time_start))
