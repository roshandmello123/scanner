from flask import Flask,render_template,request
app = Flask(__name__)
@app.route('/')
def hello_world():
    return "Hello Roshan Bhai"

@app.route('/main')
def main():
    return render_template("main.html")

@app.route('/index')
def index():
    return render_template("index.html")

# @app.route('/register',methods=['POST','GET'])
# def register():
#     if request.method=='POST':
#         name=request.form['name']
#         password = request.form['password']
#         if name=="roshan" and password=="bhai22":
#             log_msg = 'Welcome to pdf scanner !'
#             return render_template('index.html', msg=log_msg)
#         else:
#             msg = 'Incorrect credentials!'
#             return render_template('register.html', msg=msg)
#     return render_template("register.html")

if __name__ == '__main__':
    app.run(debug=True)