import grpc
from concurrent import futures
import showtime_pb2
import showtime_pb2_grpc
import json

""""
class BookingServicer(booking_pb2_grpc.BookingServicer):

    def __init__(self):
        with open('{}/data/bookings.json'.format("."), "r") as jsf:
            self.db = json.load(jsf)["schedule"]
"""

def getSchedule(stub):
    response = stub.GetSchedule(showtime_pb2.Empty())
    print('hello')
    schedule_list = response.schedule
    print("Printing schedule:")
    for entry in schedule_list:
        print(f"Date: {entry.date}")
        print("Movies:")
        for movie_id in entry.movies:
            print(f"  - {movie_id}")

def getScheduleByDate(stub, date):
    response = stub.GetScheduleByDate(showtime_pb2.Date(date=date))
    print("Printing schedule:")
    if response.movies:
        for movie_id in response.movies:
            print(f"  - {movie_id}")
    else:
        print("No movies found for this date.")

def getMovieSchedule(stub, movie_id):
    response = stub.GetMovieSchedule(showtime_pb2.MovieID(id=movie_id))
    print("Printing Schedule:")
    if response.dates:
        for date in response.dates:
            print(f"  - {date}")
    else:
        print("No dates found for this movie.")
    






def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:3002') as channel:
        stub = showtime_pb2_grpc.ShowtimeStub(channel)

        print("-------------- GetSchedule --------------")
        getSchedule(stub)
        print("-------------- GetScheduleByDate --------------")
        getScheduleByDate(stub, str(20151201))
        print("-------------- GetMovieSchedule --------------")
        getMovieSchedule(stub, "39ab85e5-5e8e-4dc5-afea-65dc368bd7ab")

    channel.close()


""" def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    booking_pb2_grpc.add_BookingServicer_to_server(BookingServicer(), server)
    server.add_insecure_port('[::]:3002')
    server.start()
    server.wait_for_termination() """


if __name__ == '__main__':
    run()
    #serve()
