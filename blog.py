from flask import Flask,render_template, url_for

posts = [
    {
        'author': 'Akshay Satpaise',
        'title':'blog post 1',
        'content':'first post content',
        'date_posted':'Apr 20, 2019'
    },
    {
        'author': 'Siddharth',
        'title':'blog post 2',
        'content':'Second post content',
        'date_posted':'MAR 19, 2019'
    }
]

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title = 'about')

if __name__ == '__main__':
    app.run(debug=True)