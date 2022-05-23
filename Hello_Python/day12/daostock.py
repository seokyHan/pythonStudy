import pymysql

class DaoStock:
    def __init__(self):

        self.conn = pymysql.connect(
            host='localhost', 
            user='root', 
            password='python', 
            db='python',
            port=3305,
            charset='utf8'
        )
        
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
        
    
    def myinsert(self, s_code, s_name, price, ymd_hm):
        sql = f"""insert 
                    into stock(s_code, s_name, price, ymd_hm)
                  values ('{s_code}','{s_name}','{price}','{ymd_hm}')"""
        cnt = self.curs.execute(sql)
        self.conn.commit()
        
        return cnt
        
        
    def __del__(self):
        self.conn.close()
        self.curs.close()
        
if __name__ == '__main__':
    de = DaoStock()
    
