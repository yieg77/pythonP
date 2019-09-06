import random, time, pickle

prompt = """
1. 문제 바꾸기 (영어)
2. 문제 바꾸기 (한글)
3. 문제 추가하기
4. 피클로 문제 저장하기
5. 피클에서 문제 읽어오기
6. 타자게임
7. 등수 리스트
0. 종료

Enter number: """

word_list=['start', 'python', 'artificial', 'bigdata', 'computer']

def get_list(gubn):
    if gubn=='1':
        f = open("./basic/quiz_9_typing_game.txt", 'r') #영어문제
    else:
        f = open("./basic/quiz_9_typing_game2.txt", 'r', encoding='utf-8') #한글문제

    """
    new_list = f.readlines()
    for i in range (len(new_list)):
        new_list[i] = new_list[i].replace('\n', '')
    """
    new_list = f.read()
    new_list = new_list.split('\n')
    #print('new_list', new_list)

    random_nums = random.sample(range(0,len(new_list)), 7)
    #print('ramdom_nums', random_nums)

    new_quiz = []
    for i in random_nums:
        new_quiz.append(new_list[i])

    f.close()
    
    return new_quiz

def game(rank) :
    name=input('이름을 입력하세요 : ')
    input('엔터키를 누르면 게임이 시작됩니다! (종료 0)')
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
            if user_input==quiz : break

    time_end=time.time()
    time_record=time_end-time_start
    rank[name]=time_record

    #순위 저장
    #print(rank)
    ranklist=sorted(rank.items(), key=(lambda x:x[1]))
    for i in range(len(ranklist)):
        if ranklist[i][0] == name:
            record=i+1
    #print(rank)

    print('<<게임 끝>> - [{}] 소요시간:{:.2f}초, 순위:{}위'.format(name, time_record, record))

    #등수기록 파일에 저장
    with open ("./basic/quiz_9_typing_game_record.pkl", 'wb') as f:
        pickle.dump(rank, f)

    return ranklist

def saveAsPickle(data):
    """
    f = open("./basic/quiz_9_typing_game_pickle.pkl", 'wb')
    pickle.dump(word_list, f)
    f.close()
    """
    with open ("./basic/quiz_9_typing_game_pickle.pkl", 'wb') as f:
        pickle.dump(data, f)

def getPickle():
    """
    f = open("./basic/quiz_9_typing_game_pickle.pkl", 'rb')
    word_list = pickle.load(f)
    f.close()
    """
    with open ("./basic/quiz_9_typing_game_pickle.pkl", 'rb') as f:
        data = pickle.load(f)

    #print(data)
    return data



# main

#rank={'aaa':100, 'bbb':25, 'ccc':11} #아이디와 등수를 저장할 딕셔너리
with open ("./basic/quiz_9_typing_game_record.pkl", 'rb') as f:
    rank = pickle.load(f)

number = 0
ranklist=[]
while number != 3:
    print('\n\n문제 : ', word_list)
    print(prompt)
    number = input()

    if (number=='1') or (number=='2') :
        word_list = get_list(number)
    elif number=='3':
        new_word = '1'
        while new_word:
            new_word = input('추가할 단어를 입력하세요(종료 0) : ')
            if new_word == '0' : break            
            word_list.append(new_word)
    elif number=='4': saveAsPickle(word_list)
    elif number=='5': word_list = getPickle()
    elif number=='6': ranklist = game(rank)
    elif number=='7':
        #print(rank)
        ranklist = sorted(rank.items(), key=(lambda x: x[1]))

        cnt=1
        for k, v in ranklist:
            print(cnt, '위 : {}, {:.2f}초\n'.format(k, v), end='')
            cnt+=1
        
        #lst_rank = list(rank)
        #print(rank)
#        for i in range(len(rank)):
            #print(i+1, '등 : ', rank[i][0], ' - ', rank[i][1], '초')
 #           print(i+1, '위 : {}, {:.2f}초\n'.format( rank[i][0], rank[i][1]))
    elif number=='0': break
