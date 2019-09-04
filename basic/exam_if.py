pocket = ['paper', 'cellphone', 'money']
card = True
if 'monesy' in pocket:
    pass
elif card: 
    print("택시를 타고가라")
else:
    print("카드를 꺼내라")


score = int(input('점수를 입력하세요!\n'))
message = "success" if score >= 60 else "failure"
print(message)
