from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify, json
from flask_login import login_required, login_user, logout_user, current_user, LoginManager, UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///User.sqlite' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret_key'
app.config['SECURITY_PASSWORD_SALT'] = 'password salt'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

watchlist = []

class User(db.Model, UserMixin): #store User information into database table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __init__(self, name, email, password):
        self.name=name
        self.email = email
        self.password = password

resetdb = False
if resetdb:
    with app.app_context():
        db.drop_all()
        db.create_all()


# Route for the home page
@app.route('/')
def index():
    print(watchlist)
    return render_template('index.html')

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print(123)
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            db.session.commit()
            return redirect(url_for('index'))
        else:
            error_message = 'Invalid email or password'
            return render_template('login.html', error_message=error_message)
    else:
        print(345)
        return render_template('login.html')
# Route for the register page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        hashed_password = generate_password_hash(password, method='sha256',salt_length=16)

        if password != confirm_password: #renders error_message on html file as you have used wrong passwords
            error_message = 'Your passwords do not match'
            return render_template('register.html', error_message=error_message)
        elif user_exists(email): #renders error_message on html file as account already exists
            error_message = 'User with this email address already exists'
            return render_template('register.html', error_message=error_message)

        else: #creates an attendee account and sends confirmation email with OTP
            create_user(name, email, hashed_password)

            return redirect(url_for('login'))
    else:

        return render_template('register.html')

@app.route('/add_coin', methods=['POST'])
def add_coin():
    data = request.get_json()
    coin = data['coin']
    watchlist.append(coin)
    return jsonify({'message': 'Coin added to watchlist', 'watchlist': watchlist})

def create_user(name, email, hashed_password): #method to create a user
    user = User(name=name, email=email, password=hashed_password)
    db.session.add(user)
    db.session.commit()
    session['user_id'] = user.id

def validate_user(email, password): #method to make sure user password is right.
    user = User.query.filter_by(email=email).first()
    if user and user.password == password:
        return True
    else:
        return False

def user_exists(email): #method for if the user email already being used
    user = User.query.filter_by(email=email).first()
    if user:
        return True
    else:
        return False

@app.route('/dashboard')
def dashboard():
    # Get the watchlist data (replace this with your actual implementation)
    watchlist = get_watchlist_data()

    # Fetch coin data from the CoinGecko API (replace this with your actual implementation)
    coin_data = fetch_coin_data()

    return render_template('dashboard.html', watchlist=watchlist, coin_data=coin_data)
def get_watchlist_data():
    watchlist_data = []
    coin_data = fetch_coin_data()

    if coin_data:
        for coin in watchlist:
            selected_coin = next((item for item in coin_data if item['name'] == coin), None)
            if selected_coin:
                watchlist_data.append(selected_coin)

    return watchlist_data

@app.route('/coin/<coin_id>/chart')
def get_coin_chart(coin_id):
    chart_data = fetch_coin_chart(coin_id)
    return jsonify(chart_data)

def fetch_coin_data():
    # Replace this with your implementation to fetch the coin data from the CoinGecko API
    # You can use requests or any other library to make the API call
    response = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd')
    if response.status_code == 200:
        coin_data = response.json()
        return coin_data
    else:
        return None

@app.route('/coin/<coin_id>/chart')
def fetch_chart_data(coin_id):
    # Fetch the chart data from the CoinGecko API
    response = requests.get(f'https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart?vs_currency=usd&days=1')
    
    if response.status_code == 200:
        chart_data = response.json()
        return jsonify(chart_data)
    else:
        return jsonify({'error': 'Failed to fetch chart data'})

@login_manager.user_loader
def load_user(user_id):
    # Code to load the user object based on the user ID
    # For example, if you have a User model, you can use:
    user = User.query.get(int(user_id))
    return user

    # Replace the above code with your own implementation
    return None  # Return None if the user is not found
if __name__ == '__main__':
    app.run(debug=True)

