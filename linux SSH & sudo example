from netmiko import ConnectHandler

linux = {'device_type': 'linux',
         'ip': '1.1.1.1',
         'username': 'user',
         'password': 'pw'}

net_connect = ConnectHandler(**linux)

#only necessary if root elevation is required
#root pw is the same as ssh login pw in this example
def root_access():
    net_connect.send_command("sudo su", expect_string=r"$")
    net_connect.send_command(linux['password'])

#non-root command example
user_command = net_connect.send_command("ip route show")
print(user_command)

#root command example
root_access()
root_command = net_connect.send_command("apt-get update")
#print(root_command)

net_connect.disconnect()
