from flask import Flask
from flask_socketio import SocketIO, emit
from config import Config


app = Flask(__name__)
app.configuration = Config()
app.config['SECRET_KEY'] = app.configuration.secret_key
socket_io = SocketIO(app)


def message_received():
    print('message was received!')


@socket_io.on('sample_event')
def sample_event(json):
    print('received sample event: ' + str(json))
    socket_io.emit('sample_response', json, callback=message_received)

if __name__ == '__main__':
    if app.configuration.mode == 'development':
        socket_io.run(app, port=app.configuration.port, debug=True)
    else:
        socket_io.run(app, port=app.configuration.port)
