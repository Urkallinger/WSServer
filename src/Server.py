from flask import Flask
from flask_socketio import SocketIO, send


class Server:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['SECRET_KEY'] = 'secret!'
        self.socketio = SocketIO(self.app)

        self.registerEvents()

    def run(self):
        self.socketio.run(self.app)

    def registerEvents(self):
        self.socketio.on_event('message', Server.handleMessage)

    @staticmethod
    def handleMessage(msg):
        print('Message: {}'.format(msg))
        send(msg, broadcast=True)


if __name__ == '__main__':
    Server().run()
