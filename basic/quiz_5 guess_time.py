import time

input()
start = time.time()
input()
end = time.time()
et = end-start

print('실제 시간 : {:.0f}초'.format(et))
print('차이 : {:.0f}초'.format(abs(et-20)))

