class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(2))
print(cal1.add(5))

print(cal2.add(2))
print(cal2.add(7))


class Cookie:
    pass

a = Cookie()
b = Cookie()

print(id(a), type(a))
print(id(b), type(b))


class FourCal:
    def __init__(self):
        self.first = 0
        self.second = 0    

    def setData(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return self.first+self.second

    def mul(self):
        return self.first*self.second

    def sub(self):
        return self.first-self.second

    def div(self):
        return self.first//self.second


a = FourCal()
a.setData(4, 2)

print('+ : ', a.add())
print('* : ', a.mul())
print('- : ', a.sub())
print('// : ', a.div())