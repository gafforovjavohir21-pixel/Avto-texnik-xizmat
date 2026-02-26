from flask import Flask, render_template

app = Flask(__name__)

# 1. Bosh sahifa (Hero va xizmatlar)
@app.route('/')
def index():
    return render_template('index.html')

# 2. Avtosalon sahifasi (Mashinalar ro'yxati)
@app.route('/buy')
def buy():
    return render_template('buy.html')

# 3. Texnik xizmat sahifasi (24/7 yordam)
@app.route('/service')
def service():
    return render_template('service.html')

if __name__ == '__main__':
    # debug=True xatoni brauzerda ko'rsatadi va kod o'zgarsa serverni yangilaydi
    # app.run(debug=True)
