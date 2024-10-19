from django.http import HttpResponse
import os
import platform
from datetime import datetime
import psutil
import pytz

def htop(request):
    name = "Your Full Name"  # Replace with your actual name
    username = os.getenv("USER") or os.getenv("USERNAME") or "codespace"
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f')
    
    # Safe system information
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    response = f"""
    <h1>System Information</h1>
    <p>Name: {name}</p>
    <p>User: {username}</p>
    <p>Server Time (IST): {server_time}</p>
    <h2>System Details:</h2>
    <ul>
        <li>System: {platform.system()}</li>
        <li>Release: {platform.release()}</li>
        <li>CPU Usage: {cpu_percent}%</li>
        <li>Memory: {memory.percent}% used</li>
        <li>Disk: {disk.percent}% used</li>
    </ul>
    """
    return HttpResponse(response)