import os
import logging
from flask import Flask, render_template, request
# from logging import Formatter, FileHandler
# from forms import *
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#
load_dotenv()
username = os.getenv("USER_ROOT_MONGODB")
password = os.getenv("PASS_ROOT_MONGODB")
uri = f"mongodb+srv://{username}:{password}@cluster0.qqwrckh.mongodb.net/?retryWrites=true&w=majority"

print(f'This is the username {username}')
print(f'This is the password {password}')
app = Flask(__name__)
# app.config.from_object('config')

# Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))
client = MongoClient(uri)

try:
    print(f'Is it trying to ping the deployment')
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Automatically tear down mongodb.
# @app.teardown_request
# def shutdown_session(exception=None):
#     client.close()


# Login required decorator.
'''
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap
'''
#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#
@app.route('/')
def home():
    return render_template('pages/placeholder.home.html')


# have a controller for sending a picture 
# have a controller for trying to scrape an item from walmart
@app.route('/about')
def about():
    return render_template('pages/placeholder.about.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    # Get the base64 encoded image from the request payload
    data = request.get_json()
    base64_image = data.get('image_data')

    # Your processing code for the base64 image can go here
    # For example, you can decode the base64 image and save it to a file
    # or perform image processing operations on it

    # For this example, let's just return the received image data
    return base64_image
# @app.route('/login')
# def login():
#     form = LoginForm(request.form)
#     return render_template('forms/login.html', form=form)


# @app.route('/register')
# def register():
#     form = RegisterForm(request.form)
#     return render_template('forms/register.html', form=form)


# @app.route('/forgot')
# def forgot():
#     form = ForgotForm(request.form)
#     return render_template('forms/forgot.html', form=form)

# Error handlers.


# @app.errorhandler(500)
# def internal_error(error):
#     #db_session.rollback()
#     return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

# if not app.debug:
#     file_handler = FileHandler('error.log')
#     file_handler.setFormatter(
#         Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
#     )
#     app.logger.setLevel(logging.INFO)
#     file_handler.setLevel(logging.INFO)
#     app.logger.addHandler(file_handler)
#     app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''