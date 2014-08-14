from flask import request
from app import app
from datetime import datetime
from app.utils import get_ip

from app import db
from app.models import ProvServer


@app.route('/')
def verify():
    ip = get_ip(request)
    servers = ProvServer.query.all()
    for server in servers:
        ips = server.ips.split(',')
        if ip in ips:
            server.test_passed = True
            server.date_of_test = datetime.now()
            db.session.add(server)
    db.session.commit()
    return ip
