import platform

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