# from flask import Flask

# # WSGI application
# app =Flask(__name__)

# @app.route('/') # decorator
# def index():
#     return "Hello, World! hiii"

# @app.route('/members') # decorator
# def members():
#     return "Hello, members"


# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, redirect, url_for
app= Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to my website"

@app.route('/passs/<int:score>') # variable route
def passs(score):
    return "Congratulations, you scored {0}!".format(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "Congratulations, you fail {0}!".format(score)

@app.route('/result/<int:marks>')
def result(marks):
    result = ''
    if marks >= 50:
        result = 'passs'
    else:
        result = 'fail'
    return redirect(url_for(result,score=marks))



if __name__ == '__main__':
    app.run(debug=True)