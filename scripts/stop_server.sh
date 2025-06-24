#!/bin/bash
echo "Stopping Flask server if running..."
pkill -f app.py || true
