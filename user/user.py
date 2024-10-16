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

# TEST DU SERVICE BOOKINGS

def getAllBookings(stub):
   response = stub.GetAllBookings(booking_pb2.BookingEmpty())
   print('Printing all the bookings')
   for b in response.bookings:
      print(f"user: {b.user} ; date: {b.date} ; movie: {b.movie}")

def getUserBooking(stub, id):
   response = stub.GetUserBookings(booking_pb2.UserId(id=id))
   print("Printing the user's bookings")
   print(len(response.bookings))
   for b in response.bookings:
      print(f"user: {b.user} ; date: {b.date} ; movie: {b.movie}")

def addBookingOfUser(stub, user_id, date, movie_id):
   response =  stub.AddBookingOfUser(booking_pb2.BookingItem(
      user = user_id, date=date, movie = movie_id
   ))
   print(response.body)

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

if __name__ == "__main__":
   test()
   print("Server running in port %s"%(PORT))
   app.run(host=HOST, port=PORT)
