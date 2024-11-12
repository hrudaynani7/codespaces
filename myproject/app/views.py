import os
from django.http import HttpResponse
from datetime import datetime
import subprocess

def htop_view(request):
    name = "Your Full Name"
    username = os.getenv("USER")
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S IST')
    top_output = subprocess.getoutput("top -b -n 1")
    content = f"<h1>Name: {name}</h1><h2>Username: {username}</h2><h3>Server Time: {time}</h3><pre>{top_output}</pre>"
    return HttpResponse(content)

