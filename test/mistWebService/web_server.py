from concurrent import futures
import logging

import grpc
import mist_web_messaging_pb2
import mist_web_messaging_pb2_grpc

from forms import RegistrationForm

from flask import Flask, render_template, request

result = {}
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

@app.route('/', methods = ['GET', 'POST']) 
def render_templ():
    form = RegistrationForm()
    if form.is_submitted():
        global result
        result = request.form
        return render_template('user.html', result=result)

    return render_template('index.html', form=form)


class MistMessaging(mist_web_messaging_pb2_grpc.MistWebMessagingServicer):

    print("Web server started!")

    def SayHello(self, request, context):
        return mist_web_messaging_pb2.HelloReply(message='Hello, %s!' % request.name)



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mist_web_messaging_pb2_grpc.add_MistWebMessagingServicer_to_server(MistMessaging(), server)
    server.add_insecure_port('[::]:50055')
    server.start()
    app.run(debug=True, host='0.0.0.0', port=8080)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
