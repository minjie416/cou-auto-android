# coding=utf-8
import re
import time

from Controller.deviceDriver import BaseDriver
from Libs.Log import logger
from Libs.ObjectRepo import Element
from Controller.singleDetailPageController import SingleDetailPage
__author__ = 'kzhu'

class IndexPage(BaseDriver):
    def __init__(self):
        super(IndexPage,self).__init__()

    def initialize_pages(self):
        log = logger()
        driver = self.driver
        try:
            time.sleep(2)
            if Element(driver,"Guide","confirm").is_exist():
                Element(driver,"Guide","confirm").click()
            if Element(driver,"MenuBar","tabContainer").is_exist() and \
                Element(driver,"MenuBar","tabContainer").get().is_displayed():
                elems = Element(driver,"MenuBar","tabContainer").get_children_elements("MenuBar","menuTab")
                elems[0].click()
                time.sleep(1)
                Element(driver,"IndexPage","topdown").click()
                return
            elif Element(driver,"SDP","backToHome").is_exist() and \
                    Element(driver,"SDP","backToHome").get().is_displayed():
                Element(driver,"SDP","backToHome").click()
                time.sleep(1)
                Element(driver,"IndexPage","topdown").click()
                return
            elif Element(driver,"SDP","backHome").is_exist() and \
                    Element(driver,"SDP","backHome").get().is_displayed():
                Element(driver,"SDP","backHome").click()
                time.sleep(1)
                Element(driver,"IndexPage","topdown").click()
                return
            else:
                # self.click_native_back()
                self.initialize_pages()
            return
        except Exception as e:
            log.log('[-] Error occur @initialize_pages')
            log.log('[-] Error is '+str(e))
    def accept_alert(self):
        log = logger()
        try:
            time.sleep(1)
            alert = self.driver.switch_to_alert()
            alert.accept()
        except Exception as e:
            log.log('[-] Error occur @accept_alert')
            log.log('[-] Error is '+str(e))
            return
    def select_search_product(self,search_product):
        log = logger()
        driver = self.driver
        try:
            time.sleep(1)
            Element(driver,"IndexPage","search").click()
            time.sleep(1)
            Element(driver,"IndexPage","searchText").get().send_keys(search_product)
            Element(driver,"IndexPage","searchBtn").click()
        except Exception as e:
            log.log('[-] Error occur @select_search_product')
            log.log('[-] Error is '+str(e))
    def select_global_product_category(self):
        log = logger()
        driver =self.driver
        try:
            time.sleep(1)
            items = Element(driver,"CategoryList","rootLayouts").get_lists(0)
            items[1].click()
        except Exception as e:
            log.log('[-] Error occur @select_global_product_category')
            log.log('[-] Error is '+str(e))
    def select_rocket_product_category(self):
        log = logger()
        driver =self.driver
        try:
            time.sleep(1)
            items = Element(driver,"CategoryList","rootLayouts").get_lists(0)
            items[0].click()
        except Exception as e:
            log.log('[-] Error occur @select_rocket_product_category')
            log.log('[-] Error is '+str(e))
    def select_maple_product_category(self):
        log = logger()
        driver =self.driver
        try:
            time.sleep(1)
            items = Element(driver,"CategoryList","rootLayouts").get_lists(0)
            items[2].click()
        except Exception as e:
            log.log('[-] Error occur @select_maple_product_category')
            log.log('[-] Error is '+str(e))
    def select_sdp_item(self):
        log = logger()
        driver = self.driver
        try:
            if (not Element(driver,"SDPCollections","productLists").is_exist()) or \
                    (not Element(driver,"SDPCollections","productLists").get().is_displayed()):
                i = 0
                for i in range(0,15):
                    driver.swipe(470, 800, 470, 500,400)
                    time.sleep(1)
                    flag = Element(driver,"SDPCollections","productLists").is_exist() and \
                           Element(driver,"SDPCollections","productLists").get().is_displayed()
                    if flag:
                        break
                if i == 14:
                    raise Exception("Could not find IDs element after swipe 15 times!")
            sdps = Element(driver,"SDPCollections","productLists").get_element_list()
            for sdp in sdps:
                sdp.click()
                time.sleep(2)
                if Element(driver,"Guide","close").is_exist() and Element(driver,"Guide","close").is_displayed():
                    time.sleep(2)
                    Element(driver,"Guide","close").click()
                if Element(driver,"SDP","favorite").is_exist() and \
                    Element(driver,"SDP","favorite").is_displayed():
                    return
                else:
                    Element(driver,"SDP","back").click()
                    driver.swipe(470, 800, 470, 600,400)
        except Exception as e:
            log.log('[-] Error occur @select_sdp_item')
            log.log('[-] Error is '+str(e))
    def select_sdp_item_with_options(self):
        log = logger()
        driver = self.driver
        try:
            if (not Element(driver,"SDPCollections","productLists").is_exist()) or \
                    (not Element(driver,"SDPCollections","productLists").get().is_displayed()):
                i = 0
                for i in range(0,15):
                    driver.swipe(470, 800, 470, 500,400)
                    time.sleep(1)
                    flag = Element(driver,"SDPCollections","productLists").is_exist() and \
                           Element(driver,"SDPCollections","productLists").get().is_displayed()
                    if flag:
                        break
                if i == 14:
                    raise Exception("Could not find IDs element after swipe 15 times!")
            sdps = Element(driver,"SDPCollections","productLists").get_element_list()
            for sdp in sdps:
                sdp.click()
                time.sleep(2)
                if Element(driver,"Guide","close").is_exist() and \
                    Element(driver,"Guide","close").get().is_displayed():
                    Element(driver,"Guide","close").click()
                if Element(driver,"SDP","favorite").is_exist() and \
                    Element(driver,"SDP","favorite").is_displayed():
                    if Element(driver,"SDP","optionSelector").is_exist():
                        return
                    else:
                        Element(driver,"SDP","back").click()
                        driver.swipe(470, 800, 470, 100, 400)
                        scroll_sdps = Element(driver,"SDPCollections","productLists").get_element_list()
                        for scroll_sdp in scroll_sdps:
                            if scroll_sdp == sdp:
                                continue
                            else:
                                scroll_sdp.click()
                                if Element(driver,"Guide","close").is_exist() and \
                                   Element(driver,"Guide","close").get().is_displayed():
                                    Element(driver,"Guide","close").click()
                                if Element(driver,"SDP","favorite").is_exist() and \
                                    Element(driver,"SDP","favorite").is_displayed():
                                    if Element(driver,"SDP","optionSelector").is_exist():
                                        return
                                    else:
                                        Element(driver,"SDP","back").click()
                                        driver.swipe(470, 800, 470, 100, 400)
                                else:
                                    Element(driver,"SDP","back").click()
                                    driver.swipe(470, 800, 470, 200,400)
                        self.select_sdp_item_with_options()
                else:
                    Element(driver,"SDP","back").click()
                    driver.swipe(470, 800, 470, 200,400)
        except Exception as e:
            log.log('[-] Error occur @select_sdp_item')
            log.log('[-] Error is '+str(e))
    def select_sdp_item_srp(self):
        log = logger()
        driver = self.driver
        try:
            if (not Element(driver,"SDPCollections","searchLists").is_exist()) or \
                    (not Element(driver,"SDPCollections","searchLists").gets(0).is_displayed()):
                i = 0
                for i in range(0,8):
                    driver.swipe(470, 800, 470, 550,400)
                    flag = Element(driver,"SDPCollections","searchLists").is_exist() and \
                           Element(driver,"SDPCollections","searchLists").gets(0).is_displayed()
                    if flag:
                        break
                if i == 7:
                    raise Exception("Could not find IDs element after swipe 8 times!")
            sdps = Element(driver,"SDPCollections","searchLists").get_element_list()
            for sdp in sdps:
                sdp.click()
                time.sleep(2)
                if Element(driver,"Guide","close").is_exist() and \
                        Element(driver,"Guide","close").get().is_displayed():
                    Element(driver,"Guide","close").click()
                if Element(driver,"SDP","favorite").is_exist():
                    return
                else:
                    Element(driver,"SDP","back").click()
                    driver.swipe(470, 800, 470, 600,400)
        except Exception as e:
            log.log('[-] Error occur @select_sdp_item_srp')
            log.log('[-] Error is '+str(e))
    def get_searched_results(self):
        log = logger()
        driver = self.driver
        try:
            if Element(driver,"SDPCollections","noSearchResults").is_exist() and \
                    Element(driver,"SDPCollections","noSearchResults").get().is_displayed():
                raise Exception("No Such Product Found")
            elif Element(driver,"SDPCollections","searchLists").is_exist() and \
                    Element(driver,"SDPCollections","searchLists").gets(0).is_displayed():
                sdps  = Element(driver,"SDPCollections","searchLists").get_element_list()
            elif Element(driver,"SDPCollections","searchResults").is_exist() and \
                    Element(driver,"SDPCollections","searchResults").gets(0).is_displayed():
                sdps = Element(driver,"SDPCollections","searchResults").get_element_list()
            elif Element(driver,"SDPCollections","productLists").is_exist() and \
                    Element(driver,"SDPCollections","productLists").gets(0).is_displayed():
                sdps = Element(driver,"SDPCollections","productLists").get_element_list()
            for sdp in sdps:
                sdp.click()
                time.sleep(2)
                if Element(driver,"Guide","close").is_exist() and \
                        Element(driver,"Guide","close").get().is_displayed():
                    Element(driver,"Guide","close").click()
                if Element(driver,"SDP","favorite").is_exist():
                    return
                else:
                    Element(driver,"SDP","back").click()
        except Exception as e:
            log.log('[-] Error occur @get_search_results')
            log.log('[-] Error is '+str(e))
    def get_clp_srp(self):
        log = logger()
        driver = self.driver
        clp_info = ""
        try:
            if (not Element(driver,"SDPCollections","CLP").is_exist()) or \
                    (not Element(driver,"SDPCollections","CLP").gets(0).is_displayed()):
                i = 0
                for i in range(0,15):
                    driver.swipe(470, 800, 470, 550,400)
                    flag = Element(driver,"SDPCollections","CLP").is_exist() and \
                           Element(driver,"SDPCollections","CLP").gets(0).is_displayed()
                    if flag:
                        break
                if i == 14:
                    raise Exception("Could not find collection pages after swipe 14 times!")
            clps = Element(driver,"SDPCollections","CLP").get_element_list()
            if len(clps) == 1:
                location = Element(driver,"SDPCollections","CLP").get().size
                height = location["height"]
                end_y = abs(800-height)
                driver.swipe(470, 800, 470, end_y,400)
                clp_info = Element(driver,"SDPCollections","CLP").get_children_element("SDPCollections","CLPText").text
            else:
                location = Element(driver,"SDPCollections","CLP").gets(0).size
                height = location["height"]
                end_y = abs(800-height)
                driver.swipe(470, 800, 470, end_y,400)
                clp_info = Element(driver,"SDPCollections","CLP").get_child_element(0,"SDPCollections","CLPText").text
            clp_info = filter(lambda x: not re.match(r'^\s*$', x), clp_info)
            clp_info = clp_info.replace(" ","")
            return clp_info.encode("utf-8")
        except Exception as e:
            log.log('[-] Error occur @get_clp_srp')
            log.log('[-] Error is '+str(e))
            return clp_info
    def click_native_back(self):
        self.driver.press_keycode('4')


if __name__ == '__main__':
    instance  = IndexPage()
