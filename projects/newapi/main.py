from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self, name):
        return {"data": "Hello World"}
    # def post(self):
        # return{"data": "new value"}
    
api.add_resource(HelloWorld,"/helloworld/<string:name>/<int:test>")

# @app.route("/get-user/<user_id>")
# def get_user(user_id):
#     user_data = {
#         "user_id": user_id,
#         "name": "John Doe",
#         "email": "john.doe@example.com"
#     }
#     extra = request.args.get("extra")
#     if extra:
#         user_data["extra"] = extra

#     return jsonify(user_data), 200

# @app.route("/create-user", methods=["POST"])
# def create_user():
#     if request.method =="POST":
#         data = request.get_json()
#         return jsonify(data), 201


# @app.route("/")
# def home():
#     return "Home"



if __name__ == '__main__':
    app.run(debug=True)

