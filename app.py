import psycopg2
from flask import Flask,render_template, request,redirect,url_for

app = Flask(__name__)

def db_conn():
    conn = psycopg2.connect(database="sampledb",host="localhost",user="postgres",password="1234",port="5432")
    return conn

@app.route('/')
def index():
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM members ORDER BY id ASC''')
    data = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html',data= data)


@app.route('/create',methods=['POST'])
def create():
    conn = db_conn()
    cur = conn.cursor()
    name = request.form['name']
    age = request.form['age']
    address = request.form['address']
    cur.execute('''INSERT INTO members (name,age,address) VALUES(%s,%s,%s)''',(name,age,address))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))


@app.route('/update',methods=['POST'])
def update():
    conn = db_conn()
    cur = conn.cursor()

    name = request.form['name']
    age = request.form['age']
    address = request.form['address']
    id = request.form['id']

    cur.execute('''UPDATE members SET name=%s,age=%s,address=%s WHERE id=%s''',(name,age,address,id))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))


@app.route('/delete',methods=['POST'])
def delete():
    conn = db_conn()
    cur = conn.cursor()

    id = request.form['id']

    cur.execute('''DELETE FROM members WHERE id=%s''',(id))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))