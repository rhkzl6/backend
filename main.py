from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={"r/*": {"origins": "*"}})

@app.route("/hello")
def hello():
    code = 200
    message = "hello flask"
    # result = {"code" : 200, "message" : "hello flask"}
    return code, message

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

    #dafafsafaaaad