from app import app
from flask import render_template, url_for
from .systeminfo import get_platform_info

@app.route('/')
def index():
    context = {
        'platform_info': get_platform_info(),
    }

    return render_template("index.html", context=context)