from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm #this is the forms we made earlier

# double underscore name is a name of the module. if we run the script with python directly then double underscore name can be equal to double underscore main
app = Flask(__name__)
# Create a secure cookie
app.config['SECRET_KEY'] = 'e3320a22f374154e50bb8750f68275c3'

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

# this part allows us to run the python script directly without run through export FLASK_DEBUG=1 flask run
if __name__ == '__main__':
    app.run(debug=True)