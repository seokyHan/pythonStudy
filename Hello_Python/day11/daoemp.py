import pymysql

class DaoEmp:
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
        
              
    def myselect(self):
        sql = """select m_id,
                        m_name,
                        tel,
                        addr
                   from member"""
        self.curs.execute(sql)        
        mylist = self.curs.fetchall()
        return mylist
    
    def myinsert(self, m_name, tel, addr):
        sql = f"""insert 
                    into member(m_name, tel, addr)
                  values ('{m_name}','{tel}','{addr}')"""
        cnt = self.curs.execute(sql)
        self.conn.commit()
        
        return cnt
    
    def myupdate(self, m_id, m_name, tel, addr):
        sql = f"""update member
                     set m_name='{m_name}', 
                         tel='{tel}', 
                         addr='{addr}'
                   where m_id = '{m_id}' """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        
        return cnt
    
    def mydelete(self, m_id):
        sql = f""" delete 
                     from member
                    where m_id = '{m_id}'"""
        cnt = self.curs.execute(sql)
        self.conn.commit()
        
        return cnt
        
        
    def __del__(self):
        self.conn.close()
        self.curs.close()
        
if __name__ == '__main__':
    de = DaoEmp()
    # icnt = de.myinsert('9', '9', '9')
    # ucnt = de.myupdate(8)
    dcnt = de.mydelete(8)
    mylist = de.myselect()
    print(mylist)
