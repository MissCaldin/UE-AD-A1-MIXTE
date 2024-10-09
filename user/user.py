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
#import movie_pb2
#import movie_pb2_grpc

# CALLING GraphQL requests
# todo to complete

app = Flask(__name__)

PORT = 3004
HOST = '0.0.0.0'

with open('{}/data/users.json'.format("."), "r") as jsf:
   users = json.load(jsf)["users"]

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


def test():
   with grpc.insecure_channel('localhost:3001') as channel:
      stub = booking_pb2_grpc.BookingStub(channel)

      print("-------------- GetAllBookings --------------")
      getAllBookings(stub)
      print("-------------- GetUserBooking --------------")
      getUserBooking(stub, "dwight_schrute" )
      print("-------------- AddBookingOfUser --------------")
      addBookingOfUser(stub, "dwight_schrute", "20151203", "720d006c-3a57-4b6a-b18f-9b713b073f3c" )
      addBookingOfUser(stub, "dwight_schrute", "20201203", "720d006c-3a57-4b6a-b18f-9b713b073f3c" )

      
   channel.close()

if __name__ == "__main__":
   test()
   print("Server running in port %s"%(PORT))
   app.run(host=HOST, port=PORT)
