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
def list_all():
    """
    Main page that return HTML page with list of all row in posts table

    Returns:
        html page with all data from table
    """
    conn = sqlite3.connect('posts')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM posts")
    list_all = cursor.fetchall()
    conn.close()
    return render_template('index.html', list_all=list_all)


@app.route('/add')
def add():
    """
        Adding new row to posts table
        Require : title and description in url. 

    Returns:
        redirect to list of all row in posts table
    """

    conn = sqlite3.connect('posts')
    cursor = conn.cursor()

    post_title = request.args.get('title')
    post_description = request.args.get('desc')
    
    values = (post_title, post_description)
    cursor.execute("INSERT INTO posts(title, description, date) Values ('{}','{}', datetime('now'));".format(*values))
    conn.commit()
    
    conn.close()
    return redirect('/')

@app.route('/edit')
def edit():
    """
        Edit existing row in posts table
        Require : id, title and description in url.

    Returns:
        redirect to list of all row in posts table
    """
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
    """
        Remove row from table
        Require : id of row in url.

    Returns:
        redirect to list of all row in posts table
    """
    post_id = int(request.args.get('id'))
    
    conn = sqlite3.connect('posts')
    cursor = conn.cursor()
    cursor.execute("Delete from posts where id = (?);", (post_id, ))
    conn.commit()

    conn.close()
    return redirect('/')


if __name__ == '__main__':     
    app.run(debug=True)