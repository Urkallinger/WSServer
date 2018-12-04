from flask import Flask
from flask_socketio import SocketIO, emit


class WsServer:
    """
    Simple websocket server.
    """
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['SECRET_KEY'] = 'secret!'
        self.socketIO = SocketIO(self.app)

        self.socketIO.on_event('broadcast', self.handleBroadcast)

    def run(self):
        """
        Starts the websocket server.
        """
        self.socketIO.run(self.app)

    def handleBroadcast(self, msg):
        """
        Sends the given message to all connected clients.
        """
        print('broadcast: {}'.format(msg))
        emit('broadcast', msg, broadcast=True)


if __name__ == '__main__':
    WsServer().run()
