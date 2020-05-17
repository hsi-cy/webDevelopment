from flask import Flask
app = Flask(__name__)
# double underscore name is a name of the module. if we run the script with python directly then double underscore name can be equal to double underscore main

# the root page "/"
@app.route("/")
@app.route("/home")
def home():
    return "<h1>Hello World!</h1>"

@app.route("/about")
def about():
    return "<h1>About Page</h1>"


# this part allows us to run the python script directly without run through export FLASK_DEBUG=1 flask run
if __name__ == '__main__':
    app.run(debug=True)
