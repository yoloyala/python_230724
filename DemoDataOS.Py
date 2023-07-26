# DemoDataOS.Py
from datetime import *

d1 = date(2023,7, 20)
print(d1)
d2 = date.today()
print(d2)
d3 = timedelta(days=100)
print(f"100일을 더하면:{d2+d3}")
d4 = datetime.now()
print(d4)

print("----------------------------")

import random
print(random.random())
print(random.random())
print([random.randrange(20) for i in range(10)])
print([random.randrange(20) for i in range(10)])
print(random.sample(range(20), 5))  # sample은 이전에 나온것과 안겹치는 숫자로 출력
print(random.sample(range(20), 5))

from os.path import *
print(abspath("python.exe"))                    # 현재 작동하는 프로그램의 절대 경로(abspath)를 나타내줌
print(basename("c:\\python310\\python.exe"))    # 최종파일이름만 알고 싶을 때 사용
print(getsize("c:\\python310\\python.exe"))

if isfile("c:\\python310\\python.exe"):
    print("파일 있음")
else:
    print("파일 없음")

lotto = list(range(1,46))
random.shuffle(lotto)
print(lotto)

from os import *
print("운영체제이름:", name)
print("환경변수:", environ)
#print(system("notepad.exe"))

print("현재폴더:", getcwd())
chdir("..")
chdir("c:\\work")

import glob
result = glob.glob("*.py")
print(result)
for item in glob.iglob("*.*"):
    print(item)