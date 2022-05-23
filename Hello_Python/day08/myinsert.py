import pymysql

conn = pymysql.connect(
    host='localhost', 
    user='root', 
    password='python', 
    db='python',
    port=3305,
    charset='utf8'
)
# json 형태로 받아오기. 파이썬에서 json형식을 dictionary라 함
cur = conn.cursor()

e_id = 4
e_name = 4
sex = 4
age = 4
sql = f"""insert into emp(e_id, e_name, sex, age)
         values('{e_id}','{e_name}','{sex}','{age}')"""
cnt = cur.execute(sql)
if cnt > 0:
    print("추가 성공!")
else:
    print("추가 실패!")
conn.commit()


conn.close()
cur.close()