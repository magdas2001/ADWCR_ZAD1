from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1.0/predict', methods=['GET'])
def predict():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))

    prediction = 1 if (a + b) > 5.8 else 0

    return jsonify({
        "features": {"a": a, "b": b},
        "prediction": prediction
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
