from netmiko import ConnectHandler

device_data = []
with open("devices.csv") as dev:
    
    for line in dev:
        d = {}
        #print(line)
        line_list = line.strip().split(";")
        #print(line_list)
        if line_list[0] == "Hostname":
            continue
        d["device_type"] = line_list[1]
        d["ip"] = line_list[2]
        d["username"] = line_list[3]
        d["password"] = line_list[4]
        #print(d)
        device_data.append(d)


for dev in device_data:
    cmd = ["interface ethernet 1/6", "switchport mode trunk"]
    net_connect = ConnectHandler(**dev)
    host = dev["ip"]
    print(f"{host} ... connected")
    cmd = net_connect.send_config_set(cmd)
    print(cmd, type(cmd))
    cmd = net_connect.save_config()
    print(cmd, type(cmd))
    net_connect.disconnect()
