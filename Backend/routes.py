from flask import Flask, request, jsonify
from main import create_user, get_user




app = Flask(__name__)


@app.route('/api/v1.0/create_user', methods=["POST"])
def create_user_route():
    if request.method == 'POST' or request.method == "OPTIONS":
        newuser = request.json
        user_status = create_user(newuser)
        if "Error" in user_status:
            return jsonify(user_status)
        else:
            message = {
                "Status" : "Success",
                "Message": "User successfully created",
                "UserID" : user_status
            }
            return jsonify(message)

@app.route('/api/v1.0/retrieve_user', methods=["POST"])
def retrive_user_route():
    if request.method == 'POST':
        user_to_get = request.json
        user = get_user(user_to_get)
        return jsonify(user)

@app.route("/", methods=["GET"])
def test():
    return("sucess")


if __name__ == '__main__':

    app.run(port=8080)