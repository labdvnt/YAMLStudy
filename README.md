# YAML + Jinja2 Tabanlı Network Konfigürasyon Otomasyonu

Bu repoda **Python + YAML + Jinja2** kullanarak ağ cihazları için dinamik konfigürasyon üretimi yapılmıştır. Her klasör, farklı bir seviyeyi hedefleyen uygulamalı örnekler içerir.

---

## Proje Yapısı

```
YAMLSTUDY/
├── Jinja2_YAML_Generator/
├── Jinja2_YAML_Hostname_Control/
├── NetworkAutoConfig/
```

---

## 1. Jinja2_YAML_Generator

**Amaç:**
YAML dosyasından hostname, loopback, IP gibi temel bilgileri okuyup Jinja2 ile konfigürasyon üretmek.

 İçerik:

- `devices1.yaml`: Cihaz bilgileri
- `config_template.j2`: Basit şablon
- `generate_config.py`: Python script
- `output_config.txt`: Oluşturulan çıktı

---

## 2. Jinja2_YAML_Hostname_Control

**Amaç:**
Hostname’e göre farklı yapıların üretilmesi (örneğin router1 için BGP, router2 için ACL)

İçerik:

- `devices2.yaml`: Her cihaz için `features` listesi içerir
- `config_template2.j2`: Jinja2 if/elif blokları içerir
- `generate_config2.py`: Üretici script
- `output_config.txt`: Sonuç dosyası

---

## 3. NetworkAutoConfig

**Amaç:**
Modüler `.j2` blokları kullanarak VLAN, BGP, OSPF, ACL gibi servis yapılarını üretmek

 İçerik:

- `devices.yaml`: Özellik listeli YAML verisi
- `generate_config2.py`: Ana üretici script
- `output_config.txt`: Çıktı dosyası
- `read_yaml.py`: YAML okuma örneği
- `templates/`: Modüler Jinja2 şablonları
  - `base_config.j2`, `bgp_block.j2`, `ospf_block.j2`, `acl_block.j2`, `vlan_block.j2`

---

## Öğrenilen Konular

| Konu                                     | Açıklama                          |
| ---------------------------------------- | ----------------------------------- |
| YAML temelleri                           | Liste, sözlük, iç içe yapılar  |
| Jinja2 `{{ }}`                         | Değişken yerleştirme             |
| `if`, `for`, `include` kullanımı | Koşul, döngü, şablon çağırma |
| Python + YAML                            | `yaml.safe_load()` ile YAML okuma |
| Template render                          | `.render()` ile çıktı üretme  |

---

---

# YAML + Jinja2 Based Network Configuration Automation

This repository includes practical examples using **Python + YAML + Jinja2** to dynamically generate network device configurations. Each folder targets a more advanced level.

---

## Project Structure

```
YAMLSTUDY/
├── Jinja2_YAML_Generator/
├── Jinja2_YAML_Hostname_Control/
├── NetworkAutoConfig/
```

## 1. Jinja2_YAML_Generator

 **Goal:**
Generate config using basic YAML data like hostname, loopback, and IP with Jinja2 templates.

Includes:

- `devices1.yaml`: Device data
- `config_template.j2`: Basic template
- `generate_config.py`: Python script
- `output_config.txt`: Output config

---

## 2. Jinja2_YAML_Hostname_Control

**Goal:**
Generate different config blocks per hostname (e.g., BGP for router1, ACL for router2)

Includes:

- `devices2.yaml`: Devices with `features` list
- `config_template2.j2`: Contains if/elif logic
- `generate_config2.py`: Generator script
- `output_config.txt`: Final output

---

## 3. NetworkAutoConfig

**Goal:**
Generate VLAN, BGP, OSPF, ACL using modular `.j2` files and dynamic includes.

Includes:

- `devices.yaml`: YAML with feature list
- `generate_config2.py`: Main script
- `output_config.txt`: Final config output
- `read_yaml.py`: YAML test reader
- `templates/`: Modular templates:
  - `base_config.j2`, `bgp_block.j2`, `ospf_block.j2`, `acl_block.j2`, `vlan_block.j2`

---

## Topics Learned

| Topic                        | Description                            |
| ---------------------------- | -------------------------------------- |
| YAML basics                  | Lists, dictionaries, nested structures |
| Jinja2 `{{ }}`             | Variable rendering                     |
| `if`, `for`, `include` | Conditions, loops, modular templates   |
| Python + YAML                | `yaml.safe_load()` reading           |
| Template render              | `.render()` with device data         |

---

---
