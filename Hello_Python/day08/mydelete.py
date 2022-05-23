import pymysql

conn = pymysql.connect(
    host='localhost', 
    user='root', 
    password='python', 
    db='python',
    port=3305,
    charset='utf8'
)
cur = conn.cursor()

sql = """delete 
           from emp
          where e_id = '6'""" 
cnt = cur.execute(sql)

if cnt > 0:
    print("삭제 성공")
else:
    print("삭제 실패")
conn.commit()

conn.close()
cur.close()