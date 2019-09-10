from mod1 import *
import sys, os

print(add(2,5))
print(sub(2,5))

print(os.getcwd()) # 이 프로젝트의 루트 경로

print(sys.path)
sys.path.append('D:/ai/pythonP/test01/MyMod') #일시적
print(sys.path)

from MyMod.mod2 import *

from MyMod.img.image import img

