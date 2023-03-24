from __future__ import print_function

import logging

import grpc
import mist_messaging_pb2
import mist_messaging_pb2_grpc

import mist_web_messaging_pb2
import mist_web_messaging_pb2_grpc



def main():
    with grpc.insecure_channel('mist_server_service:50051') as channel:  
        stub = mist_messaging_pb2_grpc.MistMessagingStub(channel)  
        response = stub.SayHello(mist_messaging_pb2.HelloRequest(name='your saod'))
        print("Greeter client received: " + response.message)


    with grpc.insecure_channel('mist_web_service:50055') as channel1:  
        stub1 = mist_web_messaging_pb2_grpc.MistWebMessagingStub(channel1)
        response1 = stub1.SayHello(mist_web_messaging_pb2.HelloRequest(name='Saurabh'))
        print("Greeter client received: " + response1.message)


if __name__ == '__main__':
    logging.basicConfig()
    main()
