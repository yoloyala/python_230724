# db1.py
import sqlite3
#con = sqlite3.connect("c:\\work\\test.db")
# 연결객체 생성(일단은 메모리에서 연습)
con = sqlite3.connect(":memory:")
# 커서 객체
cur = con.cursor()
#테이블 구조 생성
cur.execute("create table if not exists PhoneBook" +
            " (id integer primary key autoincrement" +
            " name text, phoneNum text);")
# 1건 입력
cur.execute("insert into PhoneBook (name, phoneNum) values " +
            " ('홍길동', '010-111');")

# 검색구문
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)