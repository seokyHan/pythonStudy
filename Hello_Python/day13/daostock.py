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
    
    def myselect(self, s_name):
        sql = f"""select s_code, s_name, price, ymd_hm
                    from stock
                   where s_name='{s_name}'
                """
        self.curs.execute(sql)        
        mylist = self.curs.fetchall()
        return mylist
    
    def myprices(self, s_name):
        ret = []
        sql = f"""
                  select s_code, s_name, price, ymd_hm
                    from stock
                   where s_name='{s_name}'
                   order by ymd_hm
                """
        self.curs.execute(sql)        
        mylist = self.curs.fetchall()
        
        for p in mylist:
            ret.append(p['price'])
        return ret
    
    def mys_name(self):
        sql = f"""
                  select s_name
                    from stock
                   group by s_name
                   limit 20
                """
                
        self.curs.execute(sql)        
        mylist = self.curs.fetchall()
        return mylist
    
        
    def __del__(self):
        self.conn.close()
        self.curs.close()
        
if __name__ == '__main__':
    de = DaoStock()
   
       
    
