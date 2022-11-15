import psutil
from psutil._common import bytes2human
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

def get_process_details(pid):
    if psutil.pid_exists(pid):
        process_info = psutil.Process(pid).as_dict()
        process_data = {
            "create_time": datetime.fromtimestamp(process_info['create_time']),
            "status": process_info['status'],
            "cpu_percent": process_info['cpu_percent'],
            "name": process_info['name'],
            "memory_rss": bytes2human(process_info['memory_info'][0]),
            "memory_vms": bytes2human(process_info['memory_info'][1]),
            "exe": process_info['exe'],
            "username": process_info['username'],
            "num_threads": process_info['num_threads'],
            "memory_percent": process_info['memory_percent'],
            "pid": process_info['pid'],
            "cpu_times": process_info['cpu_times'],
        }
        return process_data
    else:
        return None