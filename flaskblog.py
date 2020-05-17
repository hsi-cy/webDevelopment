from flask import Flask, render_template
app = Flask(__name__)
# double underscore name is a name of the module. if we run the script with python directly then double underscore name can be equal to double underscore main
posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'May 17, 2020'
    },
    {
        'author': 'ChengYun Hsi',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'May 18, 2020'
    }
]

# the root page "/"
@app.route("/")
@app.route("/home", posts=posts)
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')


# this part allows us to run the python script directly without run through export FLASK_DEBUG=1 flask run
if __name__ == '__main__':
    app.run(debug=True)
