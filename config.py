import os


class Config:
    def __init__(self):
        self.port = os.environ['KAPITOL_TINMAN_PORT']
        self.mode = os.environ['KAPITOL_TINMAN_MODE']
        self.secret_key = os.environ['KAPITOL_TINMAN_SECRET_KEY']
