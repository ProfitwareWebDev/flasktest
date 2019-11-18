from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    username = request.args.get('username')
    return render_template('index.html.jinja2', username=username)

@app.route('/about', methods=['GET', 'POST'])
def about():
    counter = int(request.form.get('counter', -1)) + 1
    return render_template('about.html.jinja2', counter=counter)

@app.route('/counter', methods=['GET', 'POST'])
def counter():
    counter = int(request.values.get('counter', -1)) + 1
    return jsonify({"counter": counter})
