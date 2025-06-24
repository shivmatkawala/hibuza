from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to My Flask App</h1><p>This is the homepage.</p>"

@app.route('/greet', methods=['POST'])
def greet():
    data = request.get_json()
    name = data.get('name', 'Guest')
    return jsonify(message=f"Hello, {name}! Welcome aboard.")

if __name__ == '__main__':
    app.run(debug=True)
