import hashlib
from flask import Flask, jsonify, request

app = Flask(__name__)


password = "d5cf7b6903d35447d249573ec80ba86ab9537166d0b979c6a42adadc81a0072a26b63266797afff3dc70ac4fd27953dc2e3ca68ab941272228439c18982f1ea1"


@app.route("/password", methods=["POST"])
def getPassword():
    response = {"status": False}
    try:
        data: str = request.get_json()['password']
        if password == hashlib.sha512(data.encode('utf-8')).hexdigest():
            response['status'] = True
            return response
        response['reason'] = "Password does not match!"
    except KeyError:
        response['reason'] = "Missing 'password' parameter!"
    return response, 403


if __name__ == "__main__":
    app.run("0.0.0.0", "8080", True)