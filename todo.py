from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sys

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@pg:5432/postgres'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://docker:docker@pg:5432/docker'
db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    bob = ListRow('bob', 'Im a bob')
    db.session.add(bob)
    db.session.commit()
    print(bob, file=sys.stderr)
    return 'Hello World!!'

@app.route('/create')
def create():
    db.create_all()
    return 'ok'

class ListRow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String())
    text = db.Column(db.UnicodeText())

    def __init__(self, author, text):
        self.author = author
        self.text = text

    def __repr__(self):
        return '<{}: {}>'.format(self.author, self.text)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
