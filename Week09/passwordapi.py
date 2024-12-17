from flask import Flask, request, jsonify
import hashlib
import random
import string
import json


app = Flask(__name__)


def generate_password():
    password = "".join(
        random.choices(string.ascii_letters + string.digits, k=random.randint(8, 16))
    )
    return hashlib.md5(password.encode()).hexdigest()


@app.route("/get_password", methods=["GET"])
def get_password():
    password = generate_password()
    response = jsonify({"password": password})
    with open("password.json", "w") as f:
        json.dump({"password": password}, f)
    return response


@app.route("/check_password", methods=["POST"])
def check_password():
    data = request.get_json()
    password = data.get("password")
    password_hash = hashlib.md5(password.encode()).hexdigest()
    with open("password.json", "r") as f:
        stored_password = json.load(f).get("password")
    if password_hash == stored_password:
        return jsonify({"message": "Success"})
    else:
        return jsonify({"message": "Failed"})


if __name__ == "__main__":
    app.run()
