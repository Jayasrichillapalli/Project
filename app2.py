from flask import Flask, request, jsonify

app = Flask(__name__)

users = {
    "user1": {"password": "pass123"},
    "user2": {"password": "abc456"}
}

@app.route('/signin', methods=['POST'])
def signin():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'message': 'Please provide both username and password'}), 400
    if username not in users or password != users[username]['password']:
        return jsonify({'message': 'Invalid credentials'}), 401
    return jsonify({'message': 'Successfully signed in'})

if __name__ == '__main__':
    app.run(debug=True)
