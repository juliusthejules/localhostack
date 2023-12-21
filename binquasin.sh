#!/bin/bash
chmod +x ./binquasin.sh

# Device identification
# Hide device IP address
ip route add default via 127.0.0.1
# Hide device MAC address
macchanger -r wlan0
# Hide device Bluetooth addresses
bluetoothctl power off
# Hide IP address hostname
hostnamectl set-hostname "127.0.0.1"
