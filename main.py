from flask import Flask, request, jsonify

app = Flask(__name__)

users = {
    "1": {
       "name": "John Doe",
       "email": "john.doe@example.com"
   },
   "2": {
       "name": "Jane Doe",
       "email": "jane.doe@example.com"
   }
}

@app.route("/")
def home():
   return "Home"

@app.route("/get-user/<user_id>", methods=["GET"])
def getUser(user_id):
   if user_id in users:
       return jsonify(users[user_id]), 200
   else:
       return jsonify({"error": "User not found"}), 404

@app.route("/create-user", methods=["POST"])
def create_user():
   data = request.get_json()
   user_id = data.get('user_id')
   if user_id in users:
       return jsonify({"error": "User already exists"}), 400
   else:
       users[user_id] = data
       return jsonify(users[user_id]), 201

@app.route("/update-user/<user_id>", methods=["PUT"])
def update_user(user_id):
   data = request.get_json()
   if user_id in users:
       users[user_id].update(data)
       return jsonify(users[user_id]), 200
   else:
       return jsonify({"error": "User not found"}), 404

@app.route("/delete-user/<user_id>", methods=["DELETE"])
def delete_user(user_id):
   if user_id in users:
       del users[user_id]
       return jsonify({"message": "User deleted successfully"}), 200
   else:
       return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
   app.run(debug=True)
