#!/bin/bash
echo "Stopping any existing app..."
pkill -f app.py || true
rm -rf /home/ec2-user/flask-app
mkdir -p /home/ec2-user/flask-app
