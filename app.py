from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the main website!"

@app.route('/assassin')
def redirect_to_assassin():
    return redirect("http://127.0.0.1:5000")

if __name__ == '__main__':
    app.run(port=5001)
