from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail

app = Flask(__name__)

ENV = 'production'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:yourpassword@localhost/yourappname'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'Insert your database uri'

app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)

class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200))
    email = db.Column(db.String(200), unique=True)
    service = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())

    def __init__(self, customer, email, service, rating, comments):
        self.customer = customer
        self.email = email
        self.service = service
        self.rating = rating
        self.comments = comments

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        email = request.form['email']
        service = request.form['service']
        rating = request.form['rating']
        comments = request.form['comments']
        # print(customer, service, rating, comments)
        if db.session.query(Feedback).filter(Feedback.email == email).count() == 0:
            data = Feedback(customer, email, service, rating, comments)
            db.session.add(data)
            db.session.commit()
            send_mail(customer, email, service, rating, comments)
            return render_template('success.html')
        return render_template('index.html', message="You have already submitted feedback")


if __name__ == '__main__':
    app.debug = True
    app.run()