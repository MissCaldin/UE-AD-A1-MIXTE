import grpc
from concurrent import futures
import showtime_pb2
import showtime_pb2_grpc
import booking_pb2
import booking_pb2_grpc
import json


class BookingServicer(booking_pb2_grpc.BookingServicer):

    def __init__(self):
        with open('{}/data/bookings.json'.format("."), "r") as jsf:
            self.db = json.load(jsf)["bookings"]

    #Return all the bookings of the database (see booking.proto)
    def GetAllBookings(self, request, context):
        all =[]
        for user in self.db:
            user_id = user['userid']
            for d in user['dates']:
                all.append(booking_pb2.BookingItem(
                    user=user_id, date=d['date'], movie=d['movies'][0] 
                    )
                )
        return booking_pb2.Bookings(bookings=all)
    
    #Return all the bookings of the user of the database (see booking.proto)
    def GetUserBookings(self, request, context):
        user_booking = []
        for user in self.db:
            if user['userid'] == request.id :
                for d in user['dates']:
                    user_booking.append(booking_pb2.BookingItem(
                        user=request.id, date=d['date'], movie=d['movies'][0]
                        )
                    )
        return booking_pb2.Bookings(bookings=user_booking)
    
    #Add a booking for the user (see booking.proto)
    def AddBookingOfUser(self, request, context):
        #Verify booking exist
        with grpc.insecure_channel('localhost:3002') as channel:
            stub = showtime_pb2_grpc.ShowtimeStub(channel)
            movieSchedule = stub.GetMovieSchedule(showtime_pb2.MovieID(id=request.movie))
            for date in movieSchedule.dates:
                if date == request.date :
                    #addBooking
                    for booking in self.db:
                        if booking['userid'] == request.user:
                            booking['dates'].append({
                                "date": request.date,
                                "movies": [request.movie]
                            })
                    write({"bookings":self.db})
                    return booking_pb2.Message(body='Booking added')
            return booking_pb2.Message(body='Booking not added')

    #Return the movies scheduled at this date (see booking.proto)    
    def GetScheduleByDateB(self, request, context):
        with grpc.insecure_channel('localhost:3002') as channel:
            stub = showtime_pb2_grpc.ShowtimeStub(channel)
            schedule = stub.GetScheduleByDate(showtime_pb2.Date(date=request.date))
            return booking_pb2.BSchedule(date=schedule.date, movies=schedule.movies)

    #Return the dates when the movie is scheduled (see booking.proto)    
    def GetMovieScheduleB(self, request, context):
        with grpc.insecure_channel('localhost:3002') as channel:
            stub = showtime_pb2_grpc.ShowtimeStub(channel)
            schedule = stub.GetMovieSchedule(showtime_pb2.MovieID(id=request.id))
            return booking_pb2.BMovieSchedule(movie=schedule.movie, dates=schedule.dates) 



def write(something):
    with open('{}/data/bookings.json'.format("."), 'w') as f:
        json.dump(something, f, indent=4)


#FUNCTIONS TO TEST THE SERVICE SHOWTIMES

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

#END OF THE TEST FUNCTIONS

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    booking_pb2_grpc.add_BookingServicer_to_server(BookingServicer(), server)
    server.add_insecure_port('[::]:3003')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    #Decomment line 146 to test the service user
    #Warning: user have to be running
    #run()
    serve()
