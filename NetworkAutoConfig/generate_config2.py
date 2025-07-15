import yaml
from jinja2 import Environment, FileSystemLoader

# YAML'dan veriyi al
with open("devices3.yaml") as f:
    data = yaml.safe_load(f)

# Jinja2 ortamı (template klasörünü göster)
env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("base_config.j2")

# Şablonla çıktıyı üret
output = template.render(devices=data["devices"])
print(output)

# Dosyaya yazmak istersen:
with open("output_config.txt", "w") as f:
    f.write(output)