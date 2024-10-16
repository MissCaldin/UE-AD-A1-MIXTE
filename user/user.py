# REST API
from flask import Flask, render_template, request, jsonify, make_response
import requests
import json
from werkzeug.exceptions import NotFound

# CALLING gRPC requests
import grpc
from concurrent import futures
import booking_pb2
import booking_pb2_grpc

from google.protobuf.json_format import MessageToJson

# CALLING GraphQL requests
# todo to complete

app = Flask(__name__)

PORT = 3004
HOST = '0.0.0.0'

with open('{}/data/users.json'.format("."), "r") as jsf:
   users = json.load(jsf)["users"]

#Home page of the service
@app.route("/", methods=['GET'])
def home():
   return "<h1 style='color:blue'>Welcome to the User service!</h1>"

#Display all the movies and their data
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

#Display data about movie
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

  #Home page of the user 
@app.route("/<string:id>", methods=["GET"])
def home_user(id):
   user = next((user for user in users if user['id'] == id), None)
   if user==None:
      return jsonify({"error": "User not found"}), 404
   return make_response(jsonify(user['name']))

"""@app.route("/test", methods=["GET"])
def test2():
   with grpc.insecure_channel('localhost:3003') as channel:
      stub = booking_pb2_grpc.BookingStub(channel)

      print("-------------- GetAllBookings --------------")
      response = json.loads(MessageToJson(getAllBookings(stub)))
      print(response)
   return make_response(jsonify(response))"""

#Display the bookings of the user
@app.route("/<userid>/bookings", methods=['GET'])
def userBookings(userid):
   with grpc.insecure_channel('localhost:3003') as channel:
      stub = booking_pb2_grpc.BookingStub(channel)
      response = json.loads(MessageToJson(getUserBooking(stub, userid)))
   return make_response(jsonify(response))

#Add a booking for the user
@app.route("/<userid>/addBooking", methods=['GET'])
def addBooking(stub, user_id, date, movie_id):
   with grpc.insecure_channel('localhost:3003') as channel:
      stub = booking_pb2_grpc.BookingStub(channel)
      response = json.loads(MessageToJson(addBookingOfUser(stub, userid)))
   return make_response(jsonify(response))


# FUNCTIONS TO TEST THE SERVICE BOOKINGS

def getAllBookings(stub):
   response = stub.GetAllBookings(booking_pb2.BookingEmpty())
   print('Printing all the bookings')
   for b in response.bookings:
      print(f"user: {b.user} ; date: {b.date} ; movie: {b.movie}")
   return response

def getUserBooking(stub, id):
   response = stub.GetUserBookings(booking_pb2.UserId(id=id))
   print("Printing the user's bookings")
   print(len(response.bookings))
   for b in response.bookings:
      print(f"user: {b.user} ; date: {b.date} ; movie: {b.movie}")
   return response

def addBookingOfUser(stub, user_id, date, movie_id):
   response =  stub.AddBookingOfUser(booking_pb2.BookingItem(
      user = user_id, date=date, movie = movie_id
   ))
   print(response.body)
   return response

def getMovieSchedule(stub, movie_id):
   response = stub.GetMovieScheduleB(booking_pb2.BMovieID(id=movie_id))
   for d in response.dates:
      print(d)

def getScheduleByDate(stub, date):
   response = stub.GetScheduleByDateB(booking_pb2.BDate(date=date))
   for m in response.movies:
      print(m)



def test():
   with grpc.insecure_channel('localhost:3003') as channel:
      stub = booking_pb2_grpc.BookingStub(channel)

      print("-------------- GetAllBookings --------------")
      getAllBookings(stub)
      print("-------------- GetUserBooking --------------")
      getUserBooking(stub, "dwight_schrute" )
      print("-------------- AddBookingOfUser --------------")
      addBookingOfUser(stub, "dwight_schrute", "20151203", "720d006c-3a57-4b6a-b18f-9b713b073f3c" )
      addBookingOfUser(stub, "dwight_schrute", "20201203", "720d006c-3a57-4b6a-b18f-9b713b073f3c" )
      print("-------------- GetMovieSchedule --------------")
      getMovieSchedule(stub, "96798c08-d19b-4986-a05d-7da856efb697")
      print("-------------- GetScheduleByDate --------------")
      getScheduleByDate(stub, "20151203")
  
   channel.close()

#END OF TEST FUNCTIONS

if __name__ == "__main__":
   #Decomment line 156 to test the service booking
   #Warning: booking and user have to be running
   #test()
   print("Server running in port %s"%(PORT))
   app.run(host=HOST, port=PORT)
