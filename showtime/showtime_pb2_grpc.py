# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import showtime_pb2 as showtime__pb2

GRPC_GENERATED_VERSION = '1.66.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in showtime_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class ShowtimeStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetSchedule = channel.unary_unary(
                '/Showtime/GetSchedule',
                request_serializer=showtime__pb2.Empty.SerializeToString,
                response_deserializer=showtime__pb2.AllSchedule.FromString,
                _registered_method=True)
        self.GetScheduleByDate = channel.unary_unary(
                '/Showtime/GetScheduleByDate',
                request_serializer=showtime__pb2.Date.SerializeToString,
                response_deserializer=showtime__pb2.Schedule.FromString,
                _registered_method=True)
        self.GetMovieSchedule = channel.unary_unary(
                '/Showtime/GetMovieSchedule',
                request_serializer=showtime__pb2.MovieID.SerializeToString,
                response_deserializer=showtime__pb2.MovieSchedule.FromString,
                _registered_method=True)


class ShowtimeServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetSchedule(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetScheduleByDate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMovieSchedule(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ShowtimeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetSchedule': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSchedule,
                    request_deserializer=showtime__pb2.Empty.FromString,
                    response_serializer=showtime__pb2.AllSchedule.SerializeToString,
            ),
            'GetScheduleByDate': grpc.unary_unary_rpc_method_handler(
                    servicer.GetScheduleByDate,
                    request_deserializer=showtime__pb2.Date.FromString,
                    response_serializer=showtime__pb2.Schedule.SerializeToString,
            ),
            'GetMovieSchedule': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMovieSchedule,
                    request_deserializer=showtime__pb2.MovieID.FromString,
                    response_serializer=showtime__pb2.MovieSchedule.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Showtime', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('Showtime', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Showtime(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetSchedule(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/Showtime/GetSchedule',
            showtime__pb2.Empty.SerializeToString,
            showtime__pb2.AllSchedule.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetScheduleByDate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/Showtime/GetScheduleByDate',
            showtime__pb2.Date.SerializeToString,
            showtime__pb2.Schedule.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetMovieSchedule(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/Showtime/GetMovieSchedule',
            showtime__pb2.MovieID.SerializeToString,
            showtime__pb2.MovieSchedule.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
