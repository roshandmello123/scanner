from flask import Flask,render_template,request
#from flask_mysqldb import MySQL
import mysql.connector
app = Flask(__name__)
try:
    conn = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="user_db"
    )
    if (conn.is_connected()):
        print("connection done")

except:
    print("unable to connect")
# cur=conn.cursor()
# cur.execute('select uname from user')
# result=cur.fetchall()
# print(result)
# cur.close()
# conn.close()

@app.route('/register' ,methods=['POST','GET'])
def hello_world():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        cur=conn.cursor()
        print("here")
        cur.execute("select uname from user where uid=101")
        result=cur.fetchone()
        dbname = result[0]
        print(dbname)

        if name== dbname :
            return render_template("index.html",msg= dbname)
        #conn.commit()
        cur.close()
        conn.close()
    return render_template("register.html", msg="hi")




if __name__ == '__main__':
    app.run(debug=True)