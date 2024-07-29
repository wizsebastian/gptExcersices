from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/test", methods=["GET"])
def its_good():
    test = "suprice motherfucker"
    return jsonify({"data": test})


if (__name__) == "__main__":
    app.run()
