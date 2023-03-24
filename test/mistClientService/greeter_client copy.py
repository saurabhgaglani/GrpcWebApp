from __future__ import print_function

import logging

import grpc
import mist_messaging_pb2
import mist_messaging_pb2_grpc



channel = grpc.insecure_channel('mist_server_service:50051') 
stub = mist_messaging_pb2_grpc.MistMessagingStub(channel)

channel1 = grpc.insecure_channel('mist_web_service:50052')
stub1 = mist_messaging_pb2_grpc.MistMessagingStub(channel1)



def main():
        
    response = stub.SayHello(mist_messaging_pb2.HelloRequest(name='your saod'))
    print("Greeter client received: " + response.message)

    response1 = stub1.SayHello(mist_messaging_pb2.HelloRequest(name='yajssa'))
    print("Greeter client received: " + response1.message)


if __name__ == '__main__':
    logging.basicConfig()
    main()
