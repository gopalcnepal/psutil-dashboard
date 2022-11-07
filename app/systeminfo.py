import platform
import psutil
from datetime import datetime
from psutil._common import bytes2human

def get_platform_info():
    uname = platform.uname()
    if psutil.MACOS:
        os_name = 'apple'
    elif psutil.WINDOWS:
        os_name = 'windows'
    elif psutil.LINUX:
        os_name = 'linux'
    else:
        os_name = 'Unknown'

    platform_info = {
        'os_name': os_name,
        'node_name': uname.node.split('.')[0],
        'system_name': uname.system,
        'release_version': uname.release,
        'architecture': platform.architecture()[0],
        'processor_type': platform.processor()

    }

    return platform_info

def get_power_info():
    power_data = psutil.sensors_battery()

    if power_data.secsleft in (psutil.POWER_TIME_UNKNOWN, psutil.POWER_TIME_UNLIMITED):
        time_remaining = 'Calculating'
    else:
        time_remaining = str(round(psutil.sensors_battery().secsleft / 3600, 2)) + ' hrs'

    power_info = {
        'percent': int(power_data.percent),
        'time_remaining': time_remaining,
        'power_source': 'AC Power' if power_data.power_plugged  else 'Battery Power'
    }
    
    return power_info

def get_user_info():
    user_data = psutil.users()
    user_info = {}

    for count,user in enumerate(user_data):
        user_info[count] = {
            'name': user.name, 
            'terminal': user.terminal, 
            'host': user.host, 
            'started': datetime.fromtimestamp(user.started),
            'pid':user.pid,
        }

    return user_info

def get_memory_info():
    vmemory_data = psutil.virtual_memory()
    smemory_data = psutil.swap_memory()

    memory_data = {
        'svmem_total': bytes2human(vmemory_data.total),
        'svem_percent': vmemory_data.percent,
        'smem_total': bytes2human(smemory_data.total),
        'smem_percent': smemory_data.percent
    }
    
    return memory_data