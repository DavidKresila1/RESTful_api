import json
import urllib.request
from urllib import response
import requests
from flask import Flask
from flask_restful import Api, Resource, abort

app = Flask(__name__)
api = Api(app)





class searchById(Resource):
    def get(self, id):
        url = (f"https://jsonplaceholder.typicode.com/users/{id}")
        response = urllib.request.urlopen(url)
        data = response.read()
        dict = json.loads(data)
        return {"data": dict}



class searchByUserid(Resource):
    def get(self, userId):
        url = f"https://jsonplaceholder.typicode.com/users/{userId}"
        response = urllib.request.urlopen(url)
        data = response.read()
        dict = json.loads(data)
        return {"data": dict}


class searchPostByID(Resource):
    def get(self, id):
        url = f"https://jsonplaceholder.typicode.com/posts/{id}"
        response = urllib.request.urlopen(url)
        data = response.read()
        dict = json.loads(data)
        return {"data": dict}


class searchPostByUserId(Resource):
    def get(self, userId):
        url = f"https://jsonplaceholder.typicode.com/posts/?userId={userId}"
        response = urllib.request.urlopen(url)
        data = response.read()
        dict = json.loads(data)
        return {"data": dict}

class addToJson(Resource):
    def put(self, userId, title, body):
        return {"userId": userId,
                "title": title,
                "body" : body,}


class delId(Resource):
    def delete(self, id):
        url = f"https://jsonplaceholder.typicode.com/posts/?userId={id}"
        response = urllib.request.urlopen(url)
        del response[id]
        return "", 204


class updateData(Resource):
    def patch(self, id, userId, title, body):
        url = f"https://jsonplaceholder.typicode.com/posts/{id}"
        response = urllib.request.urlopen(url)
        return requests.patch(response, data = {
            "userId": userId,
            "title": title,
            "body": body
        })


api.add_resource(searchById, "/idSearch/<int:id>")
api.add_resource(searchByUserid, "/userIdSearch/<int:userId>")
api.add_resource(searchPostByID, "/searchPostById/<int:id>")
api.add_resource(searchPostByUserId, "/searchPostByUserId/<int:userId>")
api.add_resource(addToJson, "/addToJson/<int:userId>/<string:title>/<string:body>")
api.add_resource(delId, "/delete/<int:id>")
api.add_resource(updateData, "/update/<int:id>/<int:userId>/<string:title>/<string:body>")


if __name__ == "__main__":
    app.run(debug=True)
