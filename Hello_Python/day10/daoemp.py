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
        sql = """select e_id,
                        e_name,
                        sex,
                        age
                   from emp"""
        self.curs.execute(sql)        
        mylist = self.curs.fetchall()
        return mylist
    
    def myinsert(self, e_name, sex, age):
        sql = f"""insert 
                    into emp(e_name, sex, age)
                  values ('{e_name}','{sex}','{age}')"""
        cnt = self.curs.execute(sql)
        self.conn.commit()
        
        return cnt
    
    def myupdate(self, e_id, e_name, sex, age):
        sql = f"""update emp
                     set e_name='{e_name}', 
                         sex='{sex}', 
                         age='{age}'
                   where e_id = '{e_id}' """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        
        return cnt
    
    def mydelete(self, e_id):
        sql = f""" delete 
                     from emp
                    where e_id = '{e_id}'"""
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
