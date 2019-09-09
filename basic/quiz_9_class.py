import random, time, pickle

class TypingGame:
    def __init__(self):
        self.word_list = ['start', 'python', 'artificial', 'bigdata', 'computer']
        self.rank = {}  

    # 1, 2 문제 바꾸기
    def get_list(self, gubn):
        if gubn=='1':
            f = open("./basic/quiz_9_typing_game.txt", 'r') #영어문제
        else:
            f = open("./basic/quiz_9_typing_game2.txt", 'r', encoding='utf-8') #한글문제

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

    #3. 문제 추가하기
    def add_word(self):
        new_word = '1'
        while new_word:
            new_word = input('추가할 단어를 입력하세요(종료 0) : ')
            if new_word == '0' : break            
            self.word_list.append(new_word)

    #4. 파일로 문제 저장하기
    def saveAsTxtFile(self):
        #print(data)
        with open ("./basic/quiz_9_quizList.txt", 'w') as f:
            for i in self.word_list:
                f.write(i)
                f.write(' ')

    #5. 피클로 문제 저장하기
    def saveAsPickle(self):
        with open ("./basic/quiz_9_typing_game_pickle.pkl", 'wb') as f:
            pickle.dump(self.word_list, f)

    #6. 피클에서 문제 읽어오기
    def getPickle(self):
        with open ("./basic/quiz_9_typing_game_pickle.pkl", 'rb') as f:
            data = pickle.load(f)

        #print(data)
        return data

    # 7. 게임하기
    def game(self):
        name=input('이름을 입력하세요 : ')
        input('엔터키를 누르면 게임이 시작됩니다! (종료 0)')
        print('<<게임 시작>>')
        time_start=time.time()

        for i in range(0, 5):
            print(str(i+1)+'번째 문제 : ', end = '')
            #quiz=word_list[random.randint(0, 4)]\

            quiz = random.choice(self.word_list)
            print(quiz)

            while 1 :
                print('>> ', end='')
                user_input = input()
                if user_input==quiz : break

        time_end=time.time()
        time_record=time_end-time_start
        self.rank[name]=time_record

        #순위 저장
        #print(rank)
        ranklist=sorted(self.rank.items(), key=(lambda x:x[1]))
        for i in range(len(ranklist)):
            if ranklist[i][0] == name:
                record=i+1
        #print(rank)

        print('<<게임 끝>> - [{}] 소요시간:{:.2f}초, 순위:{}위'.format(name, time_record, record))

        #등수기록 파일에 저장
        with open ("./basic/quiz_9_typing_game_record.pkl", 'wb') as f:
            pickle.dump(self.rank, f)

        return ranklist

    #8. 등수 리스트
    def showList(self):
        #print(rank)
        ranklist = sorted(self.rank.items(), key=(lambda x: x[1]))

        cnt=1
        for k, v in ranklist:
            print(cnt, '위 : {}, {:.2f}초\n'.format(k, v), end='')
            cnt+=1
        