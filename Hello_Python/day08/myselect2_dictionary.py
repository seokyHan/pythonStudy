import pymysql

conn = pymysql.connect(
    host='localhost', 
    user='root', 
    password='python', 
    db='python',
    port=3305,
    charset='utf8'
)
cur = conn.cursor(pymysql.cursors.DictCursor)

sql = 'select * from emp'
cur.execute(sql)

rows = cur.fetchall()
print(rows)

conn.close()
cur.close()
