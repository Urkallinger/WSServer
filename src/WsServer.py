from flask import Flask
from flask_socketio import SocketIO, send, emit


class WsServer:
    """
    Simple websocket server.
    """
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['SECRET_KEY'] = 'secret!'
        self.socketio = SocketIO(self.app)

        self.socketio.on_event('broadcast', self.handleBroadcast)

    def run(self):
        """
        Starts the websocket server.
        """
        self.socketio.run(self.app)

    def handleBroadcast(self, msg):
        """
        Sends the given message to all connected clients.
        """
        send(msg, broadcast=True)


if __name__ == '__main__':
    WsServer().run()
