"""
 ______     _   _
|__  / |   | | | |
  / /| |   | |_| |
 / /_| |___|  _  |
/____|_____|_| |_|

"""""
import pyfiglet

def doArtCode(code):
    artCode = pyfiglet.figlet_format(code)
    print(artCode)


def printIpAddress(ip):
    spliteIP = ip.split(".")
    separator = "[.]"
    printIp = separator.join(spliteIP)
    print(printIp)

if __name__ == '__main__':

    # doArtCode("ZLH")
    printIpAddress(input("Enter your ip address: "))