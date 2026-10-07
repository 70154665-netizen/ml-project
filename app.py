from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    return jsonify({'status': 'Merged logic for Student 1 & 2'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
