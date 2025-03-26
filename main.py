from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Cristian Cardoso": "+525523457687", "Santiago Amezcua": "+525567879687", "Mario Centeno": "+5234543321", "Gerardo Cornejo": "+52455565465"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
