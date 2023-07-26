# DemoRE.py
import re

# 숫자가 0에서 N번th
result = re.search("[0-9]*th", "  35th")
print(result)
print(result.group())

# 선택 블록: ctrl + /
# result = re.match("[0-9]*th", "  35th")     #정확하게 text가 맞아야함
# print(result)
# print(result.group())

result = re.search("apple", "빅테크에서 apple의 위상")
print(result.group())
result = re.search("\d{4}", "올해는 2023년")
print(result.group())
result = re.search("\d{5}", "우리 동네는 42300")
print(result.group())

print("---대소문자---")
data = "Apple is big company and aple is very delicious"
c = re.compile("apple", re.IGNORECASE)
print(c.findall(data))

print("---다중라인검색---")
data2 = """파이썬을
배워서

누구나 사용"""
c = re.compile("^.+",re.MULTILINE)  # ^ 시작하는 패턴에 / . 글자가 / + 하나라도 있으면 / 읽기
print(c.findall(data2))