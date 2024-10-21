from django.http import HttpResponse
import os
import psutil
from datetime import datetime
import pytz

def htop(request):
    name = "Your Full Name"  # Replace with your actual name
    username = os.getenv("USER") or os.getenv("USERNAME") or "codespace"
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f')
    
    uptime = datetime.now() - datetime.fromtimestamp(psutil.boot_time())
    load_avg = psutil.getloadavg()
    cpu_count = psutil.cpu_count()
    memory = psutil.virtual_memory()

    process_list = []
    for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_percent']):
        try:
            process_list.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    response = f"""
    <pre>
Name: {name}
user: {username}
Server Time (IST): {server_time}
TOP output:

top - {datetime.now().strftime('%H:%M:%S')} up {uptime.days} days, {uptime.seconds // 3600} hours, {(uptime.seconds % 3600) // 60} min
Tasks: {len(process_list)} total
%Cpu(s): {psutil.cpu_percent(interval=1)}% used
MiB Mem : {memory.total / (1024 * 1024):.1f} total, {memory.available / (1024 * 1024):.1f} free, {memory.used / (1024 * 1024):.1f} used

  PID USER      %CPU %MEM    TIME+ COMMAND
"""
    for proc in sorted(process_list, key=lambda x: x['cpu_percent'], reverse=True)[:20]:
        response += f"{proc['pid']:5} {proc['username'][:8]:8} {proc['cpu_percent']:5.1f} {proc['memory_percent']:5.1f} 00:00:00 {proc['name'][:15]}\n"

    response += "</pre>"
    return HttpResponse(response)