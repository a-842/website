from flask import Flask, render_template
import os

app = Flask(__name__)
BLOGS_DIR="blogs"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/references')
def references():
    return render_template('references.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/blog')
def blogs():
    """List all blog posts"""
    try:
        blog_posts = [
            f[:-5] for f in os.listdir(BLOGS_DIR) if f.endswith('.html')
        ]
    except FileNotFoundError:
        blog_posts = []
    return render_template('blogs.html', blogs=blog_posts)

@app.route('/blog/<post>')
def blog_post(post):
    """Render a specific blog post"""
    blog_path = os.path.join(BLOGS_DIR, f"{post}.html")
    if not os.path.exists(blog_path):
        abort(404)
    
    with open(blog_path, "r", encoding="utf-8") as file:
        content = file.read()
    
    return render_template('blog_post.html', title=post.replace("_", " ").title(), content=content)


@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/links')
def links():
    return render_template('links.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
