from flask import Flask, render_template

app = Flask(__name__,
            static_url_path='',
            static_folder='static')

@app.route('/janggi')
def janggi():
  
    return render_template('janggi4.html')

if __name__ == '__main__':
    app.run(port=80)