# coding=utf-8
import time
from Controller.deviceDriver import BaseDriver
from Libs.Log import logger
from Libs.ObjectRepo import Element

__author__ = 'kzhu'

class MenuBar(BaseDriver):
    def __init__(self):
        super(MenuBar,self).__init__()

    def select_home_tab(self):
        log = logger()
        driver = self.driver
        try:
            time.sleep(1)
            elems = Element(driver,"MenuBar","tabContainer").get_children_elements("MenuBar","menuTab")
            elems[0].click()
        except Exception as e:
            log.log('[-] Error occur @select_home_tab')
            log.log('[-] Error is '+str(e))

    def select_category_tab(self):
        log = logger()
        driver = self.driver
        try:
            time.sleep(1)
            elems = Element(driver,"MenuBar","tabContainer").get_children_elements("MenuBar","menuTab")
            elems[1].click()
        except Exception as e:
            log.log('[-] Error occur @select_category_tab')
            log.log('[-] Error is '+str(e))

    def select_to_mycoupang_tab(self):
        log = logger()
        driver = self.driver
        try:
            time.sleep(1)
            elems = Element(driver,"MenuBar","tabContainer").get_children_elements("MenuBar","menuTab")
            elems[2].click()
        except Exception as e:
            log.log('[-] Error occur @select_to_mycoupang_tab')
            log.log('[-] Error is '+str(e))






