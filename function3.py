# function3.py
# 가변인자
def union(*ar):
    #지역변수(리스트)
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

# 호출
print(union("HAM","SPAM"))
print(union("HAM","SPAM","EGG"))

