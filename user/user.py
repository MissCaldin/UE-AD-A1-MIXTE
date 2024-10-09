# REST API
from flask import Flask, render_template, request, jsonify, make_response
import requests
import json
from werkzeug.exceptions import NotFound

# CALLING gRPC requests
import grpc
from concurrent import futures
"""import booking_pb2
import booking_pb2_grpc
import movie_pb2
import movie_pb2_grpc"""

# CALLING GraphQL requests
# todo to complete

app = Flask(__name__)

PORT = 3004
HOST = '0.0.0.0'

with open('{}/data/users.json'.format("."), "r") as jsf:
   users = json.load(jsf)["users"]

@app.route("/", methods=['GET'])
def home():
   return "<h1 style='color:blue'>Welcome to the User service!</h1>"

@app.route("/movies", methods=['GET'])
def movies():
   url="http://127.0.0.1:3001/graphql"
   body= """
   {movies{
      title
      rating
      director
      id}
   }"""
   response = requests.post(url=url, json={"query":body})
   return make_response(jsonify(response.json()["data"]), 200)

@app.route("/movies/<movieid>", methods=['GET'])
def movie_by_id(movieid):
   url=f"http://127.0.0.1:3001/graphql"
   body="""
   {
      movie_with_id(_id: "%s") {
         id
         title
         rating
         director
      }
   }
   """ % movieid
   response1=requests.post(url, json={"query":body})
   return make_response(jsonify(response1.json()["data"]), 200)
   
@app.route("/<string:id>", methods=["GET"])
def home_user(id):
   user = next((user for user in users if user['id'] == id), None)
   return make_response(jsonify(user['name']))

if __name__ == "__main__":
   print("Server running in port %s"%(PORT))
   app.run(host=HOST, port=PORT)
