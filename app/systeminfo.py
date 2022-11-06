import platform
import psutil

def get_platform_info():
    uname = platform.uname()

    platform_info = {
        'os_name': platform.platform().split('-')[0],
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
        time_remaining = str(round(psutil.sensors_battery().secsleft / 3600, 2)) + 'hrs '

    power_info = {
        'percent': power_data.percent,
        'time_remaining': time_remaining,
        'power_source': 'AC Power' if power_data.power_plugged  else 'Battery Power'
    }
    
    return power_info