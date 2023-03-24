from concurrent import futures
import logging

import grpc
import mist_messaging_pb2
import mist_messaging_pb2_grpc


class MistMessaging(mist_messaging_pb2_grpc.MistMessagingServicer):
    print("HEREEEEEEEEEE")

    def SayHello(self, request, context):
        return mist_messaging_pb2.HelloReply(message='Hello, %s!' % request.name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mist_messaging_pb2_grpc.add_MistMessagingServicer_to_server(MistMessaging(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
