import json

from flask import Flask
from flask_socketio import SocketIO, emit

from database.MongoClient import MongoClient


class WsServer:
    """
    Simple websocket server.
    """
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['SECRET_KEY'] = 'secret!'
        self.socketIO = SocketIO(self.app)
        self.mongoClient = MongoClient()

        self.socketIO.on_event('broadcast', self.handleBroadcast)
        self.socketIO.on_event('getUsers', self.getUsers)

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

    def getUsers(self):
        """
        Returns all users.
        """
        users = self.mongoClient.getUsers()
        data = json.dumps(users)
        print(data)
        emit('getUsers', data)



if __name__ == '__main__':
    WsServer().run()
