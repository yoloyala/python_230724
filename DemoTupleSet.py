# DemoTupleSet

# 중요 함수
# list()
# int()
# str()
# range()

# True
# False
# None

# 형식 변환 -> set 함수
a = {1,2,3,3}
b = {3,4,4,5}

print(a)
print(type(a))
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

print("---Tuple---")
tp=(10,20,30)
print(len(tp))
print(tp[0])
print("id:%s, name:%s" %("kim","김유신"))

# 함수 정의
def calc(a,b):
    return a+b, a*b

# 함수 호출
reValue = calc(5,6)
print(reValue)

print("---형식변환---")
a = set((1,2,3))
print(a)
b = list(a)
b.append(4)
print(b)
c = tuple(b)
print(c)

print("---dict---")
color = {"apple":"red", "banana":"yellow"}
print(len(color))
print(color["apple"])
color["cherry"] = "red"
print(color)