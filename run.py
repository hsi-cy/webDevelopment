from flaskblog import app

# this part allows us to run the python script directly without run through export FLASK_DEBUG=1 flask run
if __name__ == '__main__':
    app.run(debug=True)
