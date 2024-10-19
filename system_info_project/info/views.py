from django.http import HttpResponse
import os
from datetime import datetime
import pytz

def htop(request):
    name = "Your Full Name"  # Replace with your actual name
    username = os.getenv("USER") or os.getenv("USERNAME") or "codespace"
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f')
    
    response = f"""
    <h1>System Information</h1>
    <p>Name: {name}</p>
    <p>Username: {username}</p>
    <p>Server Time (IST): {server_time}</p>
    """
    return HttpResponse(response)