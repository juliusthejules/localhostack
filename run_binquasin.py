import subprocess 

# Device identification
# Hide device IP address
subprocess.run(['ip', 'route', 'add', 'default', 'via', '127.0.0.1'])

# Hide device MAC address
subprocess.run(['macchanger', '-r', 'wlan0'])

# Hide device Bluetooth addresses
subprocess.run(['bluetoothctl', 'power', 'off'])

# Hide IP address hostname
subprocess.run(['hostnamectl', 'set-hostname', '127.0.0.1'])

# Make binquasin.sh executable
subprocess.run(['chmod', '+x', './binquasin.sh'])

# Execute binquasin.sh
subprocess.run(['./binquasin.sh'])

# Execute binquasin.bat
subprocess.run(['./binquasin.bat'], shell=True)

# You can add more commands as needed

# Now you can call this Python script from your index.html page
