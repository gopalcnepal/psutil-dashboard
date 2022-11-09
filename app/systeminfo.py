import platform
import psutil
from datetime import datetime
from psutil._common import bytes2human

def get_platform_info():
    uname = platform.uname()
    boot_time = psutil.boot_time()
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
        'processor_type': platform.processor(),
        'boot_time': datetime.now() - datetime.fromtimestamp(boot_time),

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

def get_disks_info():
    disk_data = {}
    disk_partitions = psutil.disk_partitions(all=False)
    for counter,partition in enumerate(disk_partitions):
        usage_data = psutil.disk_usage(partition.mountpoint)
        disk_data[counter] = {
            'device': partition.device,
            'mounted': partition.mountpoint,
            'total': bytes2human(usage_data.total),
            'used':bytes2human(usage_data.used),
            'free':bytes2human(usage_data.free),
        }
    return disk_data

def get_network_info():
    network_data = {}
    if_addrs = psutil.net_if_addrs()
    io_counter = psutil.net_io_counters(pernic=True)

    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            if int(address.family) == 2:
                if interface_name in io_counter:
                    io = io_counter[interface_name]
                    network_data[interface_name] = {
                        'name': interface_name,
                        'ip_address': address.address,
                        'sent_bytes': bytes2human(io.bytes_sent),
                        'received_bytes': bytes2human(io.bytes_recv),
                    }

    return network_data