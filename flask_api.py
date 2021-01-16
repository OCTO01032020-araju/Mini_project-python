from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
courses = [
    {
        'courseID': 1,
        'courseName': 'Python course'
    },
    {
        'courseID': 2,
        'courseName': 'js course'
    },
    {
        'courseID': 3,
        'courseName': 'web Dev course'
    }
]

@app.route('/hello')
def appli_try():
    return render_template('index.html')


if __name__ == '__main__':
   app.run()


app.add_url_rule(‘/’, ‘hello’, appli_try)