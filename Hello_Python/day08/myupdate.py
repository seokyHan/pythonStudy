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

sql = """update emp 
            set e_name='7',
                sex = '7',
                age = '7' 
          where e_id = '6'""" 
cnt = cur.execute(sql)

if cnt > 0:
    print("수정 성공")
else:
    print("수정 실패")
conn.commit()

conn.close()
cur.close()