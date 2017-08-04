import os


class Config:
    def __init__(self):
        self.port = os.environ['TINMAN_PORT']
        self.mode = os.environ['TINMAN_MODE']
        self.log_path = os.environ['TINMAN_LOG_PATH']
