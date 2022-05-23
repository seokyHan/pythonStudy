from flask import Flask,request, render_template
from day11 import daoemp
from flask.json import jsonify

app = Flask(__name__,
            static_url_path='',
            static_folder='static')
de = daoemp.DaoEmp()

@app.route('/memberlist', methods=['GET'])
def myselect():
    myselect = daoemp.DaoEmp()
    rst = myselect.myselect()
    
    return render_template('memberlist.html', rst=rst)

@app.route('/myinsert', methods=['POST'])
def myinsert():
    data = request.get_json()
    m_name = data['m_name']
    tel = data['tel']
    addr = data['addr']
    
    cnt = de.myinsert(m_name, tel, addr)
    
    result = "fail"
    if cnt == 1:
        result = "success"
    
    return jsonify(result = result)

@app.route('/myupdate', methods=['POST'])
def myupdate():
    data = request.get_json()
    m_id = data['m_id']
    m_name = data['m_name']
    tel = data['tel']
    addr = data['addr']
    
    cnt = de.myupdate(m_id, m_name, tel, addr)
    
    result = "fail"
    if cnt == 1:
        result = "success"
    
    return jsonify(result = result)

@app.route('/mydelete', methods=['POST'])
def mydelete():
    data = request.get_json()
    m_id = data['m_id']
    
    cnt = de.mydelete(m_id)
    
    result = "fail"
    if cnt == 1:
        result = "success"
    
    return jsonify(result = result)

if __name__ == '__main__':
    app.run(port=80)