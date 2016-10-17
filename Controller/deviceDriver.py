import os

import sys

import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

from Libs.AppiumManager import AppiumManager
from Libs.DevicesConfiguration import DeviceConfiguration

__author__ = 'kzhu'


class BaseDriver(object):

    def __init__(self):
        self.appium = AppiumManager()
        self.dc = DeviceConfiguration()
        self.driver = self.set_up()

    def set_up(self):
        port = self.appium.start_appium()
        device = self.dc.get_android_devices()
        app = os.path.join(os.path.dirname(__file__),
                           '../apps/[20161007]CoupangAndroid-v4.3.9-79bd89b2-release.apk')
        app = os.path.abspath(app)
        if not bool(device):
            print "No device get connected!\nPlease connect a device to get tested!"
            sys.exit(0)
        else:
            desired_cap = {}
            desired_cap['platformName'] = 'Android'
            desired_cap['browserName'] = ''
            # desired_cap['platformVersion'] = device.get("osVersion")
            desired_cap['deviceName'] = device.get("deviceName")
            desired_cap['udid'] = device.get("deviceID")
            desired_cap['app'] = app
            this_driver = webdriver.Remote('http://127.0.0.1:'+str(port)+'/wd/hub', desired_cap)
        print "driver has been generated as" + str(this_driver)
        return this_driver


    def tear_down(self):
        try:
            self.driver.close()
        except Exception:
            self.driver.quit()

    def get_session_id(self):
        try:
            return self.driver.session_id
        except Exception:
            raise

    def take_screenshot(self,name,save_location):
        # Make sure the path exists.
        path = os.path.abspath(save_location)
        if not os.path.exists(path):
            os.makedirs(path)
        full_path = '%s/%s' % (path, name)
        self.driver.get_screenshot_as_file(full_path)
        return full_path