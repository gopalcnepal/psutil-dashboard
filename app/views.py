from app import app
from flask import render_template, url_for
from .systeminfo import *

@app.route('/')
def index():
    context = {
        'platform_info': get_platform_info(),
        'power_info': get_power_info(),
        'user_info': get_user_info(),
        'memory_info': get_memory_info(),
        'disk_info': get_disks_info(),
        'network_info': get_network_info(),
    }

    return render_template("index.html", context=context)