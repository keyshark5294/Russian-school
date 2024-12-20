from ipaddress import *


'''
Если маска подсети 255.255.255.192 и IP-⁠адрес компьютера в сети 10.18.134.220, 
то номер компьютера в сети равен
'''
i = 0

for m in range(33):
    print(m)
    net = ip_network(f'98.162.71.123/{m}', False)
    print(net.netmask)
    print(net)
    print()
    # print()
    # for ip in net:
    #     if '98.162.71.96' in str(net):
    #         print(net.netmask)
    