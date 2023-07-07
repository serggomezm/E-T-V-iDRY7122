import requests
from netmiko import ConnectHandler
import json

cisco1 = { 
    "ip": "10.0.2.5",
    "device_type": "cisco_ios",
    "username": "cisco",
    "password": "cisco123!",
}

# Show command that we execute.
command = "show run"

with ConnectHandler(**cisco1) as net_connect:
    output = net_connect.send_command(command)
    # Automatically cleans-up the output so that only the show output is returned
    print("\n" + output + "\n")

