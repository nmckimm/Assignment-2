'''
Created on 22 Feb 2018

@author: neil
'''
import platform

def displayInfo():
    sysplat = 'System Platform : ', platform.platform() 
    macver = 'MacOS Version : ' , platform.mac_ver()
    winver ='Windows Version : ' , platform.win32_ver()
    linver = 'Linux Distribution : ' , platform.linux_distribution()
    proc = 'Processor Architecture: ' , platform.processor()

    systemInformation = sysplat + proc + macver + winver + linver
    return systemInformation



if __name__ == '__main__':
    displayInfo()


