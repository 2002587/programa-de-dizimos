#app.py

from flask import Flask, render_template, request, url_for, flash, redirect, send_file
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import abort
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
import os, datetime
import sqlite3

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "database.db"))

app = Flask('__name__')
app.config['SECRET_KEY'] = 'your secret key'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:////home/univesp/programa_dizimos/img.db
db = SQLAlchemy(app)
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'upload')


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(288), nullable=False)

class FileContents(db.Model)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))
    data = db.Column(db.LargeBinary)

@app.route('/')
def index():
    posts = Posts.query.all()
    return render_template('index.html', posts=posts)

def get_post(post_id):
    post = Posts.query.filter_by(id=post_id).first()
    if post is None:
        abort(404)
    return post

@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Título é obrigatório!!!')
        else:
            post = Posts(title=title, content=content)
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('index'))

    return render_template('create.html')


@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Nome é obrigatório!!')
        else:
            post.title = title
            post.content = content
            db.session.commit()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    db.session.delete(post)
    db.session.commit()
    flash('"{}" foi apagado com sucesso!!'.format(post.title))
    return redirect(url_for('index'))


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['imagem']
    savePath = os.path.join(UPLOAD_FOLDER, secure.filename(file.filename))
    file.save(savePath)
    return 'UPLOAD feito com sucesso'

@app.route('/get-file/<filename>')
def getFile(filename):
    file = os.path.join(UPLOAD_FOLDER + '.png')
    return send_file(file, mimetype="imagem/png")

@app.route('/upload', methods=['POST'])
def uploads():
    file = request.files['inputFile']

    newFile = FileContents(name=file.filename, data=file.read())
    db.session.add(newFile)
    db.session.commit()
    return 'Saved' + file.filename + 'to the database!'

if __name__ == '__main__':
    app.run(debug=True)
