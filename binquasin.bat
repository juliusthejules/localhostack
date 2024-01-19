@ECHO OFF
REM Device identification
REM Hide device IP address
ROUTE ADD DEFAULT GATEWAY 127.0.0.1
REM Hide device MAC address
MACCHANGER -R wlan0
REM Hide device Bluetooth addresses
BLUETOOTHCTL POWER OFF
REM Hide IP address hostname
NETDOM RENAME %COMPUTERNAME% 127.0.0.1
