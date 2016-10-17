import commands
import subprocess
import time,os

from Libs.AvailablePorts import AvailablePorts

__author__ = 'kzhu'
class AppiumManager():

    def __init__(self):
        self.ap = AvailablePorts()

    def start_appium(self):
        """start the appium server
        """
        port = self.ap.get_open_port()
        chrome_port = self.ap.get_open_port()
        bootstrap_port = self.ap.get_open_port()

        command = "appium --session-override -p"+" "+str(port)+" "+ \
                  "--chromedriver-port"+" "+str(chrome_port)+" "+"-bp"+" "+str(bootstrap_port)
        print command
        subprocess.Popen([command],shell=True)
        time.sleep(10)
        return port

    def release_appium(self):
        pid = commands.getoutput("ps -eaf|grep -i 'appium'|grep -v grep|awk '{print $2}'")
        if len(pid) != 0:
            os.system("kill -9 "+ pid)


    def release_appium2(self):
        """stop the appium server
        :return:
        """
        # kill myServer
        os.popen('pkill node')