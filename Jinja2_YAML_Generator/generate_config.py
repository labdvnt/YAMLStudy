import yaml
from jinja2 import Template

# Template YAML Read
with open("devices1.yaml") as f:
    data = yaml.safe_load(f)

# Template Jinja2 Read
with open("config_template.j2") as f:
    template = Template(f.read())

# Process data into template
output = template.render(devices=data["devices"])

# Print Result
print(output)

# If You Write to File:
with open("output_config.txt", "w") as f:
    f.write(output)

#TESTTEST
#TESTTEST
#TESTTEST
#TESTTEST
