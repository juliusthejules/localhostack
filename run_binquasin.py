import subprocess

# Device identification
# Hide device IP address
subprocess.run(['ip', 'route', 'add', 'default', 'via', '192.168.1.1'])

# Hide device MAC address
subprocess.run(['macchanger', '-r', 'wlan0'])

# Hide device Bluetooth addresses
subprocess.run(['bluetoothctl', 'power', 'off'])

# Hide IP address hostname
subprocess.run(['hostnamectl', 'set-hostname', 'localhost'])

# Make binquasin.sh executable
subprocess.run(['chmod', '+x', './binquasin.sh'])

# Execute binquasin.sh
subprocess.run(['./binquasin.sh'])

# You can add more commands as needed

# Now you can call this Python script from your index.html page