import pickle
import quiz_9_class as cm

prompt = """
1. 문제 바꾸기 (영어)
2. 문제 바꾸기 (한글)
3. 문제 추가하기
4. 파일로 문제 저장하기
5. 피클로 문제 저장하기
6. 피클에서 문제 읽어오기
7. 타자게임
8. 등수 리스트
0. 종료

Enter number: """

# === main =================================================================

word_list=['start', 'python', 'artificial', 'bigdata', 'computer']

#rank={'aaa':100, 'bbb':25, 'ccc':11} #아이디와 등수를 저장할 딕셔너리
with open ("./basic/quiz_9_typing_game_record.pkl", 'rb') as f:
    rank = pickle.load(f)

ranklist=[]
number = 0
while 1:
    print('\n\n문제 : ', word_list)
    print(prompt)
    number = input()

    if (number=='1') or (number=='2') : word_list = fm.get_list(number)
    elif number=='3': fm.add_word(word_list)
    elif number=='4': fm.saveAsTxtFile(word_list)
    elif number=='5': fm.saveAsPickle(word_list)
    elif number=='6': word_list = fm.getPickle()
    elif number=='7': ranklist = fm.game(word_list, rank)
    elif number=='8': fm.showList(rank)
    elif number=='0': break
