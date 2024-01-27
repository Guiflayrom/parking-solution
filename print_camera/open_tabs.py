from os import system as sy

ip_list= ['199.234.167.151','199.234.167.152','199.234.167.153','199.234.167.154','199.234.167.155']

for ip in ip_list:
    co = 'start {}'.format(ip);sy(co)