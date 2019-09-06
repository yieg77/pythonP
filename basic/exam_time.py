import time

day = ('일요일', '월요일', '화요일', '수요일', '목요일', '금요일', '토요일')

print(time.time()) #1970.1.1 0:0:0을 기준으로 지난 시간을 초 단위로 돌려줌
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
print(time.ctime()) #항상 현재시간만 돌려줌

print(time.strftime('%Y-%m-%d', time.localtime(time.time())), end=' ')
print(day[int(time.strftime('%w', time.localtime(time.time())))], end=' ')
print(time.strftime('%X', time.localtime(time.time())))

print(time.strftime('%x %X', time.localtime(time.time())))


for i in range(10):
    print(i, '초', sep='')
    time.sleep(1)
