import psutil
from datetime import datetime
from .systeminfo import get_user_info
import os

def get_process_list():
    processes_list = {}
    # List of attribues we want to list
    process_attributes_list = ['pid', 'name', 'username', 'status', 'create_time', 'memory_percent', 'cpu_percent']

    for processes in psutil.process_iter(process_attributes_list):
        if processes.info['username'] == os.environ.get('USER', os.environ.get('USERNAME')):
            processes_list[processes.pid] = {
                'pid': processes.info['pid'],
                'name': processes.info['name'],
                'username': processes.info['username'], 
                'status': processes.info['status'], 
                'create_time': datetime.fromtimestamp(processes.info['create_time']), 
                'memory_percent': processes.info['memory_percent'], 
                'cpu_percent': processes.info['cpu_percent'],
                }
    return processes_list