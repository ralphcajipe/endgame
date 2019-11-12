from flask import Flask,render_template,request,redirect,url_for
import sqlite3 as sql
app=Flask(__name__)

@app.route('/')
def index():
    title="Log in"
    return render_template('index.html', title=title)

@app.route('/signup')
def signup():
    title="Sign up"
    return render_template('registration.html',title=title)

@app.route('/success')
def success():
    return("Login Successful")


@app.route('/register',methods=['POST','GET'])
def register():
    title="Result"
    if request.method=='POST':
        try:
            uname=request.form['username']
            em=request.form['email']
            pword=request.form['password']
            with sql.connect('database.db') as con:
                cur=con.cursor()
                cur.execute("INSERT INTO account (username, email, password) VALUES (?,?,?)", (uname,em,pword))
                con.commit()
                msg="Record successfully added!"

        except Exception as e:
            con.rollback()
            msg="Error in insert operation!"
        finally:
            return msg
            con.close()


    #return 'Register'

@app.route('/result')
def list():
    title="List of Users"
    con=sql.connect('database.db')
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("Select * from account")
    rows=cur.fetchall()
    return render_template('result.html', rows=rows, title=title)

@app.route('/delete/<int:id>')
def delete(id):
    #ilagay ang cur.execute for delete
    return "Deleted {}".format(id)

@app.route('/update')
def update():
    return render_template('update.html')
if __name__=='__main__':
    app.run()
