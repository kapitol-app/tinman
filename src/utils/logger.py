from config import Config
import os
from datetime import datetime


class LogType:
    def __init__(self):
        self.ERROR = 'error'
        self.NORMAL = 'normal'
        self.WARNING = 'warning'


class Logger:
    def __init__(self):
        self.HEADER = '\033[95m'
        self.BLUE = '\033[94m'
        self.GREEN = '\033[92m'
        self.YELLOW = '\033[93m'
        self.RED = '\033[91m'
        self.ENDC = '\033[0m'
        self.BOLD = '\033[1m'
        self.UNDERLINE = '\033[4m'
        self.log_type = LogType()

    def color(self, log_type):
        if log_type == self.log_type.ERROR:
            color = self.RED
        elif log_type == self.log_type.WARNING:
            color = self.YELLOW
        else:
            color = self.GREEN
        return color

    def log(self, log_type, *args):
        message = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S') + ' :: '
        counter = 0
        for arg in args:
            if isinstance(arg, str):
                message += arg
            else:
                message += str(arg)
            if counter != len(args) - 1:
                message += ' '
        print(self.color(log_type) + message)
        log_path = Config().log_path
        if os.path.exists(log_path):
            with open(log_path, 'a') as log_file:
                log_file.write(message + '\n')
            log_file.close()
        else:
            with open(log_path, 'w+') as log_file:
                log_file.write(message + '\n')
            log_file.close()


log_types = LogType()
logger = Logger()


def log(*args):
    logger.log(log_types.NORMAL, args)

        
def error(*args):
    logger.log(log_types.ERROR, args)


def warn(*args):
    logger.log(log_types.WARNING, args)
