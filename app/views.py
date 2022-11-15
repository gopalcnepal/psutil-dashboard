from app import app
from flask import render_template, url_for
from .systeminfo import *
from .processinfo import get_process_list, get_process_details

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

@app.route('/processes')
def processes():
    context = {
        'platform_info': get_platform_info(),
        'process_list': get_process_list(),
    }
    return render_template("processes.html", context=context)

@app.route('/processes/<int:process_id>')
def process_details(process_id=None):
    if process_id != None:
        context = {
        'platform_info': get_platform_info(),
        'process_data': get_process_details(process_id),

        }
        return render_template("process_details.html", context=context) 
    else:
        return "<h1> Error with Process ID </h1>"