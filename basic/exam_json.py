import json

customer={
    'id':152352,
    'name':'강진수',
    'history':[
        {'data':'2015-03-11','item':'iPhone'},
        {'data':'2016-02-23','item':'Monitor'}
    ]
}

print(type(customer))

toJSON1 = json.dumps(customer)

print(type(toJSON1))
print(toJSON1)

with open ("./basic/test.JSON", 'wt') as f:  #텍스트로 쓰기 모드
    json.dump(customer, f,indent=4)


cu = json.loads(toJSON1)
print('cu', type(cu), cu)

with open ("./basic/test.JSON", 'rt') as f:  #텍스트로 읽기 모드
    cu2=json.load(f)

print('cu2', type(cu2), cu2)
