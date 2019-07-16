from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Why so easy</h1>'

@app.route('/another')
def show():
    return '<h2>Yo!</h2>'

if __name__ == "__main__":
    app.run()