from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add():
    # Get numbers from query parameters
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is None or b is None:
        return jsonify({'error': 'Missing parameters'}), 400
    result = a + b
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)