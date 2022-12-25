import os
import ftplib
import ipaddress
from qrshare.ClientInterface import ClientInterface
        
class FTPClient(object):
    """
    The base class for client interfaces.
    """
    def __init__(self, ip, port, user="", password="", remote_folder=""):
        self._ip = ip
        self._port = port
        self._user = user
        self._password = password
        self._remote_folder = remote_folder

    def upload(self, local_file_path):
        with open(local_file_path, 'rb') as f: 
            ftp = ftplib.FTP()
            ftp.connect(host=self._ip, port=self._port)
            ftp.login(user=self._user, passwd=self._password)
            ftp.cwd(self._remote_folder)
            ftp.storbinary(f'STOR a {os.path.basename(local_file_path)}', f)  
            ftp.close()

        full_remote_path = os.path.join(self._remote_folder, os.path.basename(local_file_path))
        
        return f"ftp://{self._user}:{self._password}@{self._ip}/{full_remote_path}"
        
    @staticmethod
    def validate_init_params(**params):
        if 'ip' not in params:
            raise ValueError("\'ip\' expected but not given")

        ipaddress.ip_address(params['ip'])
        
        if 'port' not in params:
            raise ValueError("\'port\' expected but not given")
        
        if not isinstance(params['port'], int):
            raise ValueError('param \'port\' has to be an int')
        
        if params['port'] < 1 or params['port'] > 65535:
            raise ValueError('param \'port\' is invalid')
        
        if 'user' in params.keys():
            if not isinstance(params['user'], str):
                raise ValueError('param \'user\' has to be an str')
        
        if 'password' in params.keys():
            if not isinstance(params['password'], str):
                raise ValueError('param \'password\' has to be an str')
            
        if 'remote_folder' in params.keys():
            if not isinstance(params['remote_folder'], str):
                raise ValueError('param \'remote_folder\' has to be an str')
