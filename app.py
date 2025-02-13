from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/references')
def references():
    return render_template('references.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/rants')
def rants():
    return render_template('rants.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/links')
def links():
    return render_template('links.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
