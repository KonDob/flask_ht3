from flask import Flask, render_template, redirect, request
import sqlite3

"""
         создания таблицы
    sqlite> CREATE TABLE posts
    (id integer primary key autoincrement, title varchar(200), 
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
    cursor = conn.cursor()

    # post_id = request.args.get('id')
    post_title = request.args.get('title')
    post_description = request.args.get('desc')
    
    values =(post_title, post_description)
    cursor.execute("INSERT INTO posts(title, description, date) Values ('{}','{}', datetime('now'));".format(*values))
    conn.commit()
    
    conn.close()
    return redirect('/')

@app.route('/edit')
def edit():
    conn = sqlite3.connect('posts')
    cursor = conn.cursor()
    
    post_id = request.args.get('id')
    post_title = request.args.get('title')
    post_description = request.args.get('desc')
    values = (post_title, post_description, post_id)
    
    cursor.execute("UPDATE posts SET title = '{}',description = '{}' WHERE id = {};".format(*values))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/remove')
def remove():
    post_id = int(request.args.get('id'))
    
    conn = sqlite3.connect('posts')
    cursor = conn.cursor()
    cursor.execute("Delete from posts where id = (?);", (post_id, ))
    conn.commit()

    conn.close()
    return redirect('/')


if __name__ == '__main__':     
    app.run(debug=True)