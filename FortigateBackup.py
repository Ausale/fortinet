from netmiko import ConnectHandler
import datetime
from sys import platform

#'host' is used to determine the .cfg file name
#'ip', 'username' and 'password' must be specified

my_fw = {'host': 'MyHost',
         'device_type': 'fortinet',
         'ip': '1.1.1.1',
         'username': 'MyUsername',
         'password': 'MyPassword'}

net_connect = ConnectHandler(**my_fw)

output = net_connect.send_command("show full-configuration", expect_string=r"#")

current_time = datetime.datetime.today().strftime('%Y_%b_%d')

#Enter the file path on your platform
#Only reason I included the if statement is because I used this script on different platforms

if platform == "win32":
    with open (f"C:\\Users\\..\\{my_fw['host']}_{current_time}.cfg", "w") as f:
        for line in output:
             f.write(line)

elif platform == "linux" or platform == "linux2":
    with open (f"Home/../{my_fw['host']}_{current_time}.cfg", "w") as f:
        for line in output:
             f.write(line)

elif platform == "darwin":
    with open (f"/Users/../{my_fw['host']}_{current_time}.cfg", "w") as f:
        for line in output:
            f.write(line)
else:
    print("Oops, this script currently only works for Windows, Linux & MacOS platforms")

