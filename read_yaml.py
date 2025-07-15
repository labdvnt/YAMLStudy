import yaml
import json
with open('devices.yaml', 'r') as f:
    data = yaml.safe_load(f)

print(json.dumps(data, indent=4))

for device in data['devices']:
    print(f"{device['hostname']} → {device['ip']} ")