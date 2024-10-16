import grpc
from concurrent import futures
import showtime_pb2
import showtime_pb2_grpc
import json

class ShowtimeServicer(showtime_pb2_grpc.ShowtimeServicer):

    def __init__(self):
        with open('{}/data/times.json'.format("."), "r") as jsf:
            self.db = json.load(jsf)["schedule"]

    #return the schedule of all the movies (see showtime.proto)
    def GetSchedule(self, request, context):
        schedule_entries = []
    
        for entry in self.db:
            schedule_entries.append(
                showtime_pb2.Schedule(
                    date=entry['date'], 
                    movies=entry['movies']
                )
            )

        return showtime_pb2.AllSchedule(schedule=schedule_entries)

    #return the movies schedules at this date(see showtime.proto)
    def GetScheduleByDate(self, request, context):
        for d in self.db:
            if d['date'] == request.date:
                print('Date found')
                return showtime_pb2.Schedule(date=d['date'], movies=d['movies'])
        return showtime_pb2.Schedule(date="Not found", movies="No movie at this date")

    #return the dates where the movie is scheduled (see showtime.proto)
    def GetMovieSchedule(self, request, context):
        dates = []
        for d in self.db:
            for id in d["movies"]:
                if id == request.id:
                    dates.append(d['date'])
        if dates == []:
            return showtime_pb2.MovieSchedule(movie="Movie not scheduled", dates=dates)
        return showtime_pb2.MovieSchedule(movie=request.id, dates=dates)    
        

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    showtime_pb2_grpc.add_ShowtimeServicer_to_server(ShowtimeServicer(), server)
    server.add_insecure_port('[::]:3002')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
