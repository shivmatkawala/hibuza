#!/bin/bash
cd /home/ec2-user/flask-app
nohup python3 app.py --host=0.0.0.0 --port=5000 --no-debugger --no-reload > flask.log 2>&1 &
