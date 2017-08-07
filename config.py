import os
from src.errors.errors import ConfigVarMissing


required_env_vars = [
    'TINMAN_PORT',
    'TINMAN_MODE',
    'TINMAN_DB_URL'
]

optional_env_vars = [
    'TINMAN_LOG_PATH'
]


class Config:
    def __init__(self):
        self._check_envs()
        self.port = os.environ['TINMAN_PORT']
        self.mode = os.environ['TINMAN_MODE']
        self.log_path = os.environ['TINMAN_LOG_PATH']
        self.db_url = os.environ['TINMAN_DB_URL']

    def _check_envs(self):
        for var in required_env_vars:
            if not os.environ[var]:
                raise ConfigVarMissing('Missing App Config Variable ' + var)
        for var in optional_env_vars:
            if not os.environ[var]:
                print('WARNING:', var, 'is not set in your environment')
        return None
