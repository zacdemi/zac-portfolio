from flask import Flask, render_template, url_for
application = Flask(__name__)

@application.route('/')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    application.debug = True
    application.run()



