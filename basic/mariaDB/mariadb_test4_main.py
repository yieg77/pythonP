import mariadb_test4_func as fn

prompt="""
1. 테이블 생성
2. 데이터 입력하기
3. 추천수 데이터 수정하기
4. 데이터 삭제하기
5. 전체 데이터 불러오기
6. 부분 데이터 불러오기
0. 종료하기
"""


# === main =================================================================

number = 0
while 1:
    print(prompt)
    number = input('Enter number: ')

    if number=='1' : fn.create_table()
    elif number=='2': 
        new_data=[input('제목을 입력하세요: ')]
        new_data.append(input('출판일자를 입력하세요(YYYY-MM-DD): '))
        new_data.append(input('출판사를 입력하세요: '))
        new_data.append(int(input('페이지수를 입력하세요: ')))
        new_data.append(int(input('추천수를 입력하세요: ')))
        fn.insert_record(new_data)
    elif number=='3': fn.update_book()
    elif number=='4': fn.delete_book()
    elif number=='5': fn.show_all_books()
    elif number=='6': fn.show_some_books()
    elif number=='0': break
