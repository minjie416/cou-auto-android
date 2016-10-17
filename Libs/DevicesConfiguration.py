import sys
import re
from Libs.CommandPrompt import CommandPrompt

__author__ = 'kzhu'

#
#   Device Configuration - this class contains method to config the device get connected.
#

class DeviceConfiguration():

    def __init__(self):
        self.cmd = CommandPrompt()
        self.devices = dict()


    def start_ADB(self):
        """start adb server
        """
        command = "adb start-server".split()
        output = self.cmd.run_command(command)
        lines = output.split('\n')
        if len(lines) == 1:
            print "adb service already started"
        elif "daemon started successfully" in  lines[1].lower():
            print "adb service started"
        elif "internal or external command" in lines[0].lower():
            print("adb path not set in system varibale")
            sys.exit(0)


    def stop_ADB(self):
        """stop adb server
        """
        command = "adb kill-server".split()
        self.cmd.run_command(command)


    def get_ios_devices(self):
        """get all iOS devices connected
           :return :
        """
        ios_devices = dict()
        command = "xcrun instruments -s devices".split(" ")
        output = self.cmd.run_command(command)
        lines = [line for line in output.split('\n') if line.strip() != '']
        length = len(lines)
        for i in range(2,length):
            if "Simulator" in lines[i]:
                continue
            else:
                ios_device_id = re.sub(r'.*\[(.*)\].*', r'\1',lines[i])
                ios_os_version = re.sub(r'.*\((.*)\).*', r'\1',lines[i])
                end = lines[i].find('(',1)
                ios_device_name = lines[i][0:end]
                ios_devices.update({'iosDeviceID':ios_device_id,'iosDeviceName':ios_device_name,'iosVersion':ios_os_version})
                print ("Following device is connected\n")
                print (ios_device_id+ " "+ios_device_name+" "+ios_os_version+"\n")
        if not bool(ios_devices):
            print ("No IOS Devices Connected\n")
        return ios_devices


    def get_android_devices(self):
        """get all android devices connected
           :return :
        """
        android_devices = dict()
        self.start_ADB()
        command = "adb devices".split()
        output = self.cmd.run_command(command)
        lines = [line for line in output.split('\n') if line.strip() != '']
        if len(lines)<=1:
            print ("No Android Devices Connected\n")
        else:
            length = len(lines)
            for i in range(1,length):
                line = lines[i].replace("\\s+","")
                line = line.replace("\t","")
                if "device" in line:
                    line_info = line.replace("device","")
                    device_id = line_info
                    model = self.cmd.run_command(("adb -s "+device_id+" shell getprop ro.product.model").split(" ")).replace("\r\n", "",-1)
                    brand = self.cmd.run_command(("adb -s "+device_id+" shell getprop ro.product.brand").split(" ")).replace("\r\n", "",-1)
                    os_version = self.cmd.run_command(("adb -s "+device_id+" shell getprop ro.build.version.release").split(" ")).replace("\r\n", "",-1)
                    device_name = model
                    android_devices.update({'deviceID':device_id,'deviceName':device_name,'osVersion':os_version})
                    print ("Following device is connected\n")
                    print (device_id+ " "+device_name+" "+os_version+"\n")
                elif "unauthorized" in line:
                    line_info = line.replace("unauthorized","")
                    device_id = line_info
                    print ("Following device is unauthorized\n")
                    print (device_id+"\n")
                elif "offline" in line:
                    line_info = line.replace("offline","")
                    device_id = line_info
                    print ("Following device is offline\n")
                    print (device_id+"\n")
        return android_devices

    def get_devices(self,ios_devices,android_devices):
        """get all iOS & android devices connected
           :return :
        """
        self.devices = android_devices.copy()
        self.devices.update(ios_devices)
        return self.devices

if __name__ == '__main__':
    dc = DeviceConfiguration()
    print dc.get_android_devices()



