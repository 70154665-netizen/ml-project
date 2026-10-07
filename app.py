from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['GET', 'POST'])
def get_prediction():
    return jsonify({'status': 'Student 2 logic'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
