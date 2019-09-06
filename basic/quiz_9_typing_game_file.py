import random, time

prompt = """
1. 새 문제 불러오기
2. 타자게임
3. 종료

Enter number: """

word_list=['start', 'python', 'artificial', 'bigdata', 'computer']

def get_list():
    f = open("./basic/quiz_9_typing_game.txt", 'r')
    new_list=[]
    while 1:
        new_word = f.readline()
        print(new_word)
        if not new_word: break
        new_list.append(new_word)

    f.close()
    return new_list

def game() :
    input('엔터키를 누르면 게임이 시작됩니다!')
    print('<<게임 시작>>')
    time_start=time.time()

    for i in range(0, 5):
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

number = 0
while number != 3:
    print(prompt)
    number = input()

    if number=='1':
        word_list = get_list()
        print('단어 바꾸기')
        print(word_list)
    elif number=='2': game()
    elif number=='3': break

