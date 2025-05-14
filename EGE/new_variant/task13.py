from ipaddress import ip_network 



net = ip_network('98.81.154.195/255.252.0.0', False)


for ip in net.hosts():
    print(ip)


#98.83.255.254