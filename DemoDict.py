# DemoDict.py

device = {"아이폰":5, "갤럭시":10, "윈도우":30}
#검색
print(device["아이폰"])
#입력
device["맥북"] = 15
print(device)
#수정
device["아이폰"]=5
print(device)
#삭제
del device["아이폰"]
print(device)

for item in device.items():
    print(item)

for key in device.keys():
    print(key)

#이름 + 전화번호 매핑(딕셔너리)
phone = {"kim" : "1111", "lee": "2222", "park": "3333"}
print(phone.values())
print("kim" in phone)
print("kang" not in phone)
#파이썬은 항상 참조를 전달한다.
p = phone
print(p)
print(phone)
print(id(phone), id(p))

print("---논리식---")
isRight = True
print(type(isRight))
print(1<2)
print(1!=2)
print(1==2)
print( True and True and True)
print( True and True and False)
print( True or False or False)