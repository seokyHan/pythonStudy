from flask import Flask,request, render_template
from day13 import daostock

app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/jqplot')
def jqplot(): 
    a=[]
    b=[]
    
    de = daostock.DaoStock()
    mylist = de.mys_name()
    for n in mylist:
        s_name = n['s_name']
        prices = de.myprices(s_name)
        a.append(s_name)
        b.append(prices)
    return render_template('jqplot.html' ,a=a, b=b)

if __name__ == '__main__':
    app.run(port=80)