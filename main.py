from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

from flask import Flask
from flask_socketio import SocketIO, emit
from config import Config
import src.utils.logger as logger
from run import run


app = Flask(__name__)
app.configuration = Config()
#app.config['SECRET_KEY'] = app.configuration.secret_key
socket_io = SocketIO(app)


def message_received():
    logger.log('message was received!')

def run_socket_io():
    if app.configuration.mode == 'dev':
        socket_io.run(app, port=app.configuration.port, debug=True)
    else:
        socket_io.run(app, port=app.configuration.port)

@socket_io.on('sample_event')
def sample_event(json):
    logger.log('received sample event: ', json)
    socket_io.emit('sample_response', json, callback=message_received)

if __name__ == '__main__':
    run()
