coffee={'아메리카노':2500, '카페라떼':3000, '카푸치노':3500}

number = 0
while number != 3:
    number = int(input('커피종류는 1, 커피 가격은 2, 종료는 3 : '))

    if number == 1:
        for k in coffee.keys():
            print(k, end= ' ')
        print('\n')
    elif number == 2:
        cf_name = input('커피를 선택하세요.\n')
        print(coffee[cf_name])
        print('\n')

