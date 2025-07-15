import yaml
from jinja2 import Template

with open("devices2.yaml") as f:
    data = yaml.safe_load(f)

with open("config_template2.j2") as f:
    template = Template(f.read())

output = template.render(devices=data["devices"])
print(output)

with open("output_config.txt", "w") as f:
    f.write(output)