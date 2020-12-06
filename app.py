from flask import Flask, render_template, redirect, request
import sqlite3

"""
         создания таблицы
    sqlite> CREATE TABLE posts
    (id int primary key, title varchar(200), 
    description varchar(200), date text(100));
    """

app = Flask(__name__)


@app.route('/')
def list():
    conn = sqlite3.connect('posts')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM posts")
    list_all = cursor.fetchall()
    conn.close()
    return render_template('index.html', list_all=list_all)


@app.route('/add')
def add():
    #127.0.0.1:5000/add?id=3&title=newone&desc=Uaaauu&date=old

    conn = sqlite3.connect('posts')
    
    
    post_id = request.args.get('id')
    post_title = request.args.get('title')
    post_description = request.args.get('desc')
    post_date = request.args.get('date')
    
    values = (post_id, post_title, post_description, post_date)
    print(values)
    print(values)
    print('1231231321')
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO posts Values ({},'{}','{}','{}');".format(*values))
    # conn.commit()
    cursor.execute("SELECT * FROM posts")
    list_all = cursor.fetchall()
    conn.close()
    return render_template('index.html', list_all=list_all)

@app.route('/edit')
def edit():
    conn = sqlite3.connect('posts')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM posts")
    list_all = cursor.fetchall()
    conn.close()
    return redirect('index.html', list_all=list_all)

@app.route('/remove')
def remove():
    conn = sqlite3.connect('posts')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM posts")
    list_all = cursor.fetchall()
    conn.close()
    return redirect('index.html', list_all=list_all)


if __name__ == '__main__':     
    app.run(debug=True)