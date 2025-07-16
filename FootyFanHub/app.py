from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# --- App setup ---
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://kingsley:yourpassword@localhost/footyfanhub'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# --- Initialize database ---
db = SQLAlchemy(app)

# --- Define a model ---
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# --- Run create_all inside the app context ---
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("✅ Tables created.")

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)



