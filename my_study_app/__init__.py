from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome Home!'

@app.route('/books/')
def view_students():
    return 'Book Library'

@app.route('/courses/')
def view_courses():
    return 'Courses Library'

@app.route('/certifications/')
def view_certifications():
    return 'Certifications Library'

if __name__ == '__main__':
    app.run(debug=True)