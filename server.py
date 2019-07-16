from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<name>')
def index(name):
    hobbies = ['writing', 'reading', 'rowing', 'drawiing']
    signed_in=True
    name=name.upper()
    return render_template('index.html', name=name, hobbies = hobbies, signed_in = signed_in)

@app.route('/user/<username>')
def show(username):
    return f'Hi {username}'

if __name__ == "__main__":
    app.run(debug=True)