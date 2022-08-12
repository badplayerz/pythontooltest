import grequests
import json
import subprocess

url = "www.baidu.com"



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    res = subprocess.Popen(['ping', 'www.cnblogs.com'], stdout=subprocess.PIPE).communicate()[0]
    print('123')
    print(res)


if __name__ == '__main__':
    print_hi('PyCharm')