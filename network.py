import json
import os

def execute_config(config):
    for entry in config:
        if isinstance(entry, dict):
            for key, value in entry.items():
                if key == "dir":
                    os.chdir(value)
                elif key.startswith("set"):
                    set_property(key[3:], value)
                else:
                    print(f"Ignoring unsupported key: {key}")
        elif isinstance(entry, list):
            print("Ignoring array entry:", entry)
        else:
            print("Ignoring unsupported entry type:", entry)

def set_property(prop, value):
    if prop == "IP4Address":
        print(f"Setting IPv4 address to {value}")
        # Implement setting IPv4 address
    elif prop == "Hostname":
        print(f"Setting hostname to {value}")
        # Implement setting hostname
    elif prop == "PrimaryDNSServerAddress":
        print(f"Setting primary DNS server address to {value}")
        # Implement setting primary DNS server address
    elif prop == "SecondaryDNSServerAddress":
        print(f"Setting secondary DNS server address to {value}")
        # Implement setting secondary DNS server address
    elif prop == "closePings":
        if value:
            print("Closing pings")
            # Implement closing pings
        else:
            print("Ignoring open pings")
    elif prop == "locationEnabled":
        if not value:
            print("Disabling location")
            # Implement disabling location
        else:
            print("Ignoring location setting")
    elif prop == "cacheEnabled":
        if not value:
            print("Disabling cache")
            # Implement disabling cache
        else:
            print("Ignoring cache setting")
    elif prop == "clearAll":
        if value:
            print("Clearing all")
            # Implement clearing all
        else:
            print("Ignoring clear all")
    else:
        print(f"Ignoring unsupported property: {prop}")

config_file = "./configuration/.conf"

with open(config_file, "r") as f:
    lines = f.readlines()

config = []

for line in lines:
    line = line.strip()
    if line and not line.startswith("#"):
        config.append(json.loads(line.replace("'", '"')))

execute_config(config)
