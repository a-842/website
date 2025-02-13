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
    #List all blog posts (Markdown & HTML)#
    try:
        blog_posts = [
            f.rsplit(".", 1)[0] for f in os.listdir(BLOGS_DIR) if f.endswith(('.html', '.md'))
        ]
    except FileNotFoundError:
        blog_posts = []
    return render_template('blogs.html', blogs=blog_posts)

@app.route('/blog/<post>')
def blog_post(post):
    #Render a specific blog post (Markdown or HTML
    md_path = os.path.join(BLOGS_DIR, f"{post}.md")
    html_path = os.path.join(BLOGS_DIR, f"{post}.html")

    if os.path.exists(html_path):  # If HTML file exists, load it
        with open(html_path, "r", encoding="utf-8") as file:
            content = file.read()
        return render_template('blog_post.html', title=post.replace("_", " ").title(), content=content)

    elif os.path.exists(md_path):  # If Markdown file exists, convert it
        with open(md_path, "r", encoding="utf-8") as file:
            md_content = file.read()
            html_content = markdown.markdown(md_content)  # Convert to HTML
        return render_template('blog_post.html', title=post.replace("_", " ").title(), content=html_content)

    else:
        abort(404)  # If neither exists, return 404


@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/links')
def links():
    return render_template('links.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
