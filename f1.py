

def load_csv_function (csv):
    External_list = []
    with open (csv,"r",encoding="utf-8") as file :
        for line in file:
            External_list.append(list(line.strip().split(",")))


    return External_list


def external_ip(all_ip):
    list_external_ip = []
    for ip in all_ip:
        if not ip[1].startswith("192.168") and not ip[1].startswith("10"):
            list_external_ip.append(ip)

    return list_external_ip

def sensitive_port (port):
    list_sensitive_port = []
    for ip in port:
        if not ip[4] == "SSH" and not ip[4] == "Telnet" and not ip[4] == "RDP" :
            list_sensitive_port.append(ip)

    return list_sensitive_port


