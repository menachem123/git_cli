

def load_csv_function (csv):
    external_ip = []
    with open (csv,"r",encoding="utf-8") as file :
        for line in file:
            external_ip.append(list(line.strip().split(",")))

    return external_ip


def external_ip(source_ip):
    list_external_ip = []
    for ip in source_ip:
        if not ip[1].startswith("192.168") and not ip[1].startswith("10"):
            list_external_ip.append(ip[1])

    return list_external_ip

def sensitive_port (prot):
    list_sensitive_port = []
    for ip in prot:
        if not ip[3] == "22" and not ip[3] == "23" and not ip[3] == " 3389" :
            list_sensitive_port.append(ip)

    return list_sensitive_port


def packet_large (size):
    list_packet_large = []
    for ip in size:
        if ip[5] > "5000" :
            list_packet_large.append(ip)

    return list_packet_large

def traffic_tagging (all_size):
    list_traffic_tagging = []
    large = "LARGE"
    normal = "NORMAL"
    for ip in all_size:
        if ip[5] > "5000":
            list_traffic_tagging.append(ip)
            ip.append(large)
        else:
            list_traffic_tagging.append(ip)
            ip.append(normal)
    return list_traffic_tagging

