from flask import Flask,request, render_template
from day10 import daoemp
from flask.json import jsonify

app = Flask(__name__,
            static_url_path='',
            static_folder='static')

@app.route('/emplist', methods=['GET'])
def myselect():
    myselect = daoemp.DaoEmp()
    rst = myselect.myselect()
    
    return render_template('emplist.html', rst=rst)

@app.route('/myinsert', methods=['POST'])
def myinsert():
    data = request.get_json()
    e_name = data['e_name']
    sex = data['sex']
    age = data['age']
    
    de = daoemp.DaoEmp()
    cnt = de.myinsert(e_name, sex, age)
    
    result = "fail"
    if cnt == 1:
        result = "success"
    
    return jsonify(result = result)

@app.route('/myupdate', methods=['POST'])
def myupdate():
    data = request.get_json()
    e_id = data['e_id']
    e_name = data['e_name']
    sex = data['sex']
    age = data['age']
    
    de = daoemp.DaoEmp()
    cnt = de.myupdate(e_id, e_name, sex, age)
    
    result = "fail"
    if cnt == 1:
        result = "success"
    
    return jsonify(result = result)

@app.route('/mydelete', methods=['POST'])
def mydelete():
    data = request.get_json()
    e_id = data['e_id']
    
    de = daoemp.DaoEmp()
    cnt = de.mydelete(e_id)
    
    result = "fail"
    if cnt == 1:
        result = "success"
    
    return jsonify(result = result)

if __name__ == '__main__':
    app.run(port=80)