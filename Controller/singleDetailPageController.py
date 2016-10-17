# coding=utf-8
import re
import time
from selenium.webdriver.common.keys import Keys
from Controller.deviceDriver import BaseDriver
from Libs.Log import logger
from Libs.ObjectRepo import Element


__author__ = 'kzhu'

class SingleDetailPage(BaseDriver):
    def __init__(self):
        super(SingleDetailPage,self).__init__()

    def get_product_title(self):
        log = logger()
        driver = self.driver
        title = ""
        try:
            time.sleep(1)
            if Element(driver,"SDP","title").is_exist() and \
                    Element(driver,"SDP","title").get().is_displayed() :
                title = Element(driver,"SDP","title").get().text
                title = filter(lambda x: not re.match(r'^\s*$', x), title)
                title = title.replace(" ","")
            else:
                count = 0
                for count in range(0,5):
                    driver.swipe(470, 800, 470, 600,400)
                    if Element(driver,"SDP","title").is_exist() and \
                        Element(driver,"SDP","title").get().is_displayed() :
                        break
                if count == 4:
                    raise Exception("Could not find title element after swipe 5 times!")
                title = Element(driver,"SDP","title").get().text
                title = filter(lambda x: not re.match(r'^\s*$', x), title)
                title = title.replace(" ","")
            return title.encode("utf-8")
        except Exception as e:
            log.log('[-] Error occur @get_product_title')
            log.log('[-] Error is '+str(e))
            return title
    def get_product_price(self):
        log = logger()
        driver = self.driver
        price = ""
        try:
            time.sleep(1)
            if Element(driver,"SDP","salePrice").is_exist() and \
                    Element(driver,"SDP","salePrice").get().is_displayed() :
                price = Element(driver,"SDP","salePrice").get().text
                price = filter(lambda x: not re.match(r'^\s*$', x), price)
                price = price.replace(" ","")
                price = self.__get_num(price)
            else:
                i = 0
                for i in range(0,5):
                    driver.swipe(470, 800, 470, 600,400)
                    if Element(driver,"SDP","salePrice").is_exist() and \
                        Element(driver,"SDP","salePrice").get().is_displayed() :
                        break
                if i == 4:
                    raise Exception("Could not find price element after swipe 5 times!")
                price = Element(driver,"SDP","salePrice").get().text
                price = filter(lambda x: not re.match(r'^\s*$', x), price)
                price = price.replace(" ","")
                price = self.__get_num(price)
            return price
        except Exception as e:
            log.log('[-] Error occur @get_product_price')
            log.log('[-] Error is '+str(e))
            return price
    def get_ship_fee(self):
        log = logger()
        driver = self.driver
        shipFee = ""
        try:
            time.sleep(1)
            if Element(driver,"SDP","shipFee").is_exist() and \
                    Element(driver,"SDP","shipFee").get().is_displayed() :
                shipFee = Element(driver,"SDP","shipFee").get().text
                shipFee = filter(lambda x: not re.match(r'^\s*$', x), shipFee)
                shipFee = shipFee.replace(" ","")
            else:
                i = 0
                for i in range(0,5):
                    driver.swipe(470, 800, 470, 600,400)
                    if Element(driver,"SDP","shipFee").is_exist() and \
                        Element(driver,"SDP","shipFee").get().is_displayed() :
                        break
                if i == 4:
                    raise Exception("Could not find shipFee element after swipe 5 times!")
                shipFee = Element(driver,"SDP","shipFee").get().text
                shipFee = filter(lambda x: not re.match(r'^\s*$', x), shipFee)
                shipFee = shipFee.replace(" ","")
            return shipFee.encode("utf-8")
        except Exception as e:
            log.log('[-] Error occur @get_ship_fee')
            log.log('[-] Error is '+str(e))
            return shipFee
    def get_Ids(self):
        log = logger()
        driver = self.driver
        IDs = {}
        try:
            string = ""
            if (not Element(driver,"SDP","IDsParentView").is_exist()) or \
                    (not Element(driver,"SDP","IDsParentView").get().is_displayed()):
                i = 0
                for i in range(0,5):
                    driver.swipe(470, 800, 470, 550,400)
                    flag = Element(driver,"SDP","IDsParentView").is_exist() and Element(driver,"SDP","IDsParentView").get().is_displayed()
                    if flag:
                        break
                if i == 4:
                    raise Exception("Could not find IDs element after swipe 5 times!")
                bounds = Element(driver,"SDP","IDsParentView").gets(0).size
                height = bounds["height"]
                endY = abs(800 -height)
                driver.swipe(470,800,470,endY,400)
                elems = Element(driver,"SDP","IDsParentView").get_child_elements(0,"SDP","IDs")
                for elem in elems:
                    desc = elem.get_attribute("name")
                    desc = desc.encode("utf-8")
                    string = string + desc
                li = re.findall(r'\d+',string)
                IDs.update({'productID':li[-2],'itemID':li[-1]})
            else:
                bounds = Element(driver,"SDP","IDsParentView").gets(0).size
                height = bounds["height"]
                endY = abs(800 -height)
                driver.swipe(470,800,470,endY,400)
                elems = Element(driver,"SDP","IDsParentView").get_child_elements(0,"SDP","IDs")
                for elem in elems:
                    desc = elem.get_attribute("name")
                    desc = desc.encode("utf-8")
                    string = string + desc
                li = re.findall(r'\d+',string)
                IDs.update({'productID':li[-2],'itemID':li[-1]})
            return IDs
        except Exception as e:
            log.log('[-] Error occur @get_Ids')
            log.log('[-] Error is '+str(e))
            return IDs
    def get_promise_delivery_data(self):
        log = logger()
        driver = self.driver
        pdd = ""
        try:
            time.sleep(1)
            if Element(driver,"SDP","deliveryDesc").is_exist() and \
                    Element(driver,"SDP","deliveryDesc").get().is_displayed() :
                pdd = Element(driver,"SDP","deliveryDesc").get().text
                pdd = filter(lambda x: not re.match(r'^\s*$', x), pdd)
                pdd = pdd.replace(" ","")
            else:
                i = 0
                for i in range(0,5):
                    driver.swipe(470, 800, 470, 600,400)
                    if Element(driver,"SDP","deliveryDesc").is_exist() and \
                        Element(driver,"SDP","deliveryDesc").get().is_displayed() :
                        break
                if i == 4:
                    raise Exception("Could not find promise date element after swipe 5 times!")
                pdd = Element(driver,"SDP","deliveryDesc").get().text
                pdd = filter(lambda x: not re.match(r'^\s*$', x), pdd)
                pdd = pdd.replace(" ","")
            return pdd.encode("utf-8")
        except Exception as e:
            log.log('[-] Error occur @get_ship_fee')
            log.log('[-] Error is '+str(e))
            return pdd
    def select_an_option(self,index):
        log = logger()
        driver = self.driver
        option_info = ""
        try:
            time.sleep(1)
            if Element(driver,"SDP","optionSelector").is_exist() and \
                    Element(driver,"SDP","optionSelector").get().is_displayed() :
                Element(driver,"SDP","optionSelector").click()
            else:
                i = 0
                for i in range(0,5):
                    driver.swipe(470, 800, 470, 600,400)
                    if Element(driver,"SDP","optionSelector").is_exist() and \
                        Element(driver,"SDP","optionSelector").get().is_displayed() :
                        break
                if i == 4:
                    raise Exception("Could not find options button element after swipe 5 times!")
                Element(driver,"SDP","optionSelector").click()
            options = Element(driver,"SDP","options").get_element_list()
            index = index % len(options)
            option_info = Element(driver,"SDP","options").get_child_element(index,"SDP","optionPrice").text
            options[index].click()
            option_info = filter(lambda x: not re.match(r'^\s*$', x), option_info)
            option_info = option_info.replace(" ","")
            option_info = option_info.encode("utf-8")
            if "(" in option_info:
                option_info = option_info.split("(")[0]
            option_price = self.__get_num(option_info)
            return option_price
        except Exception as e:
            log.log('[-] Error occur @select_an_option')
            log.log('[-] Error is '+str(e))
            return option_info
    def back_to_home(self):
        log = logger()
        driver = self.driver
        try:
            time.sleep(1)
            Element(driver,"SDP","backToHome").click()
            time.sleep(1)
        except Exception as e:
            log.log('[-] Error occur @back_to_home')
            log.log('[-] Error is '+str(e))
    def minus_products(self,quantity=0):
        log = logger()
        driver = self.driver
        try:
            if quantity == 0:
                return
            else:
                for i in range(0,quantity):
                    time.sleep(1)
                    Element(driver,"SDP","minus").click()
                    time.sleep(1)
        except Exception as e:
            log.log('[-] Error occur @minus_products')
            log.log('[-] Error is '+str(e))
    def add_to_purchase(self):
        log = logger()
        driver = self.driver
        try:
            time.sleep(1)
            Element(driver,"SDP","purchase").click()
            time.sleep(1)
        except Exception as e:
            log.log('[-] Error occur @add_to_purchase')
            log.log('[-] Error is '+str(e))
    def hidden_purchase(self):
        log = logger()
        driver = self.driver
        try:
            time.sleep(1)
            Element(driver,"SDP","hiddenBtn").click()
            time.sleep(1)
        except Exception as e:
            log.log('[-] Error occur @hidden_purchase')
            log.log('[-] Error is '+str(e))
    def add_products(self,quantity=1,limitation=1,total=1):
        log = logger()
        driver = self.driver
        max_buy = 1
        try:
            if quantity == 0:
                return int(max_buy)
            elif limitation > total:
                raise Exception("Buyable quantity is greater than remain amount!")
            else:
                max_buy = quantity if quantity < limitation else limitation
                for i in range(0,max_buy-1):
                    time.sleep(1)
                    Element(driver,"SDP","add").click()
                    time.sleep(1)
                return max_buy
        except Exception as e:
            log.log('[-] Error occur @add_products')
            log.log('[-] Error is '+str(e))
    def get_total_ship_fee(self):
        log = logger()
        driver = self.driver
        try:
            time.sleep(1)
            total_price = Element(driver,"SDP","originalShipFee").get().text
            return total_price
        except Exception as e:
            log.log('[-] Error occur @get_total_ship_fee')
            log.log('[-] Error is '+str(e))
    def get_elem_location(self,elem):
        log = logger()
        try:
            time.sleep(1)
            location = elem.location
            start_x = location['x']
            start_y = location['y']
            size = elem.size
            width = size['width']
            height = size['height']
            return (start_x,start_y),(width,height)
        except Exception as e:
            log.log('[-] Error occur @get_elem_location')
            log.log('[-] Error is '+str(e))
    def get_quantity(self):
        log = logger()
        driver = self.driver
        try:
            time.sleep(1)
            quantity = Element(driver,"SDP","quantity").get().text
            return int(quantity)
        except Exception as e:
            log.log('[-] Error occur @get_quantity')
            log.log('[-] Error is '+str(e))
    def get_add_btn_status(self):
        log = logger()
        driver = self.driver
        flag = False
        try:
            time.sleep(1)
            flag = Element(driver,"SDP","add").get().is_enabled()
            return flag
        except Exception as e:
            log.log('[-] Error occur @get_add_btn_status')
            log.log('[-] Error is '+str(e))
            return flag
    def get_minus_btn_status(self):
        log = logger()
        driver = self.driver
        flag = False
        try:
            time.sleep(1)
            flag = Element(driver,"SDP","minus").get().is_enabled()
            return flag
        except Exception as e:
            log.log('[-] Error occur @get_minus_btn_status')
            log.log('[-] Error is '+str(e))
            return flag
    def get_share_item(self):
        log = logger()
        driver = self.driver
        share_item_list=[]
        try:
            time.sleep(1)
            Element(driver,"SDP","share").click()
            share_options = Element(driver,"SDP","shareOptions").get_element_list()
            for share_option in share_options:
                share_item = share_option.text
                share_item = filter(lambda x: not re.match(r'^\s*$', x), share_item)
                share_item = share_item.replace(" ","")
                share_item_list.append(share_item.encode("utf-8"))
            Element(driver,"SDP","cancelShareBtn").click()
            return share_item_list
        except Exception as e:
            log.log('[-] Error occur @get_share_item')
            log.log('[-] Error is '+str(e))
    def get_rate(self):
        log = logger()
        driver = self.driver
        try:
            time.sleep(1)
            Element(driver,"SDP","share").click()
            share_options = Element(driver,"SDP","shareOptions").get_element_list()
            Element(driver,"SDP","cancelShareBtn").click()
            return len(share_options)
        except Exception as e:
            log.log('[-] Error occur @get_share_item')
            log.log('[-] Error is '+str(e))
    def check_minus_enabled(self):
        log = logger()
        driver = self.driver
        flag = False
        try:
            time.sleep(1)
            flag = Element(driver,"SDP","minus").get().is_enabled()
            return flag
        except Exception as e:
            log.log('[-] Error occur @check_minus_enabled')
            log.log('[-] Error is '+str(e))
            return flag
    def get_original_price(self):
        log = logger()
        driver = self.driver
        try:
            time.sleep(1)
            original_price = Element(driver,"SDP","selectedLayout").get_children_element("SDP","originalPrice").text
            original_price = filter(lambda x: not re.match(r'^\s*$', x), original_price)
            original_price = original_price.replace(",","")
            original_price = original_price.encode("utf-8")
            original_price = self.__get_num(original_price)
            return original_price
        except Exception as e:
            log.log('[-] Error occur @get_original_price')
            log.log('[-] Error is '+str(e))
    def __get_num(self,x):
        try:
            if x is None or x == '':
                return 0
            num = str(''.join(ele for ele in x if ele.isdigit() or ele == ',')).replace(",","")
            return int(num)
        except Exception:
            return 0
    def get_product_maple_price(self):
        log = logger()
        driver = self.driver
        price = ""
        try:
            time.sleep(1)
            if Element(driver,"SDP","mapleSalePrice").is_exist() and \
                    Element(driver,"SDP","mapleSalePrice").get().is_displayed() :
                price = Element(driver,"SDP","mapleSalePrice").get().text
                price = filter(lambda x: not re.match(r'^\s*$', x), price)
                price = price.replace(" ","")
                price = self.__get_num(price)
            else:
                i = 0
                for i in range(0,5):
                    driver.swipe(470, 800, 470, 600,400)
                    if Element(driver,"SDP","mapleSalePrice").is_exist() and \
                        Element(driver,"SDP","mapleSalePrice").get().is_displayed() :
                        break
                if i == 4:
                    raise Exception("Could not find price element after swipe 5 times!")
                price = Element(driver,"SDP","mapleSalePrice").get().text
                price = filter(lambda x: not re.match(r'^\s*$', x), price)
                price = price.replace(" ","")
                price = self.__get_num(price)
            return price
        except Exception as e:
            log.log('[-] Error occur @get_product_maple_price')
            log.log('[-] Error is '+str(e))
            return price
    def get_product_maple_unit_price(self):
        log = logger()
        driver = self.driver
        price = ""
        try:
            time.sleep(1)
            if Element(driver,"SDP","mapleProductUnitPrice").is_exist() and \
                    Element(driver,"SDP","mapleProductUnitPrice").get().is_displayed() :
                price = Element(driver,"SDP","mapleProductUnitPrice").get().text
                price = filter(lambda x: not re.match(r'^\s*$', x), price)
                price = price.replace(" ","")
            else:
                i = 0
                for i in range(0,5):
                    driver.swipe(470, 800, 470, 600,400)
                    if Element(driver,"SDP","mapleProductUnitPrice").is_exist() and \
                        Element(driver,"SDP","mapleProductUnitPrice").get().is_displayed() :
                        break
                if i == 4:
                    raise Exception("Could not find price element after swipe 5 times!")
                price = Element(driver,"SDP","mapleProductUnitPrice").get().text
                price = filter(lambda x: not re.match(r'^\s*$', x), price)
                price = price.replace(" ","")
            return price.encode("utf-8")
        except Exception as e:
            log.log('[-] Error occur @get_product_maple_unit_price')
            log.log('[-] Error is '+str(e))
            return price
    def add_maple_purchase(self):
        log = logger()
        driver = self.driver
        try:
            time.sleep(1)
            Element(driver,"SDP","maplePurchase").click()
            time.sleep(1)
        except Exception as e:
            log.log('[-] Error occur @add_maple_purchase')
            log.log('[-] Error is '+str(e))
    def get_maple_delivery_desc(self):
        log = logger()
        driver = self.driver
        price = ""
        try:
            time.sleep(1)
            if Element(driver,"SDP","mapleDeliveryDesc").is_exist() and \
                    Element(driver,"SDP","mapleDeliveryDesc").get().is_displayed() :
                price = Element(driver,"SDP","mapleDeliveryDesc").get().text
                price = filter(lambda x: not re.match(r'^\s*$', x), price)
                price = price.replace(" ","")
            else:
                i = 0
                for i in range(0,5):
                    driver.swipe(470, 800, 470, 600,400)
                    if Element(driver,"SDP","mapleDeliveryDesc").is_exist() and \
                        Element(driver,"SDP","mapleDeliveryDesc").get().is_displayed() :
                        break
                if i == 4:
                    raise Exception("Could not find price element after swipe 5 times!")
                price = Element(driver,"SDP","mapleDeliveryDesc").get().text
                price = filter(lambda x: not re.match(r'^\s*$', x), price)
                price = price.replace(" ","")
            return price.encode("utf-8")
        except Exception as e:
            log.log('[-] Error occur @get_maple_delivery_desc')
            log.log('[-] Error is '+str(e))
            return price
    def get_maple_quantity(self):
        log = logger()
        driver = self.driver
        try:
            time.sleep(1)
            quantity = Element(driver,"SDP","mapleQuantity").get().text
            return int(quantity)
        except Exception as e:
            log.log('[-] Error occur @get_maple_quantity')
            log.log('[-] Error is '+str(e))
    def add_maple_product(self,quantity=1,limitation=2,total=2):
        log = logger()
        driver = self.driver
        max_buy =1
        try:
            if quantity == 0:
                return int(max_buy)
            else:
                result = quantity if quantity < limitation else limitation
                max_buy = result if result < total else total
                for i in range(0,max_buy):
                    time.sleep(1)
                    Element(driver,"SDP","mapleAdd").click()
                    time.sleep(1)
                return max_buy
        except Exception as e:
            log.log('[-] Error occur @add_maple_product')
            log.log('[-] Error is '+str(e))
    def minus_maple_products(self,quantity=0):
        log = logger()
        driver = self.driver
        try:
            if quantity == 0:
                return
            else:
                for i in range(0,quantity):
                    time.sleep(1)
                    Element(driver,"SDP","mapleMinus").click()
                    time.sleep(1)
        except Exception as e:
            log.log('[-] Error occur @minus_maple_products')
            log.log('[-] Error is '+str(e))
    def get_maple_add_btn_status(self):
        log = logger()
        driver = self.driver
        flag = False
        try:
            time.sleep(1)
            flag = Element(driver,"SDP","mapleAdd").get().is_enabled()
            return flag
        except Exception as e:
            log.log('[-] Error occur @get_maple_add_btn_status')
            log.log('[-] Error is '+str(e))
            return flag
    def get_maple_minus_btn_status(self):
        log = logger()
        driver = self.driver
        flag = False
        try:
            time.sleep(1)
            flag = Element(driver,"SDP","mapleMinus").get().is_enabled()
            return flag
        except Exception as e:
            log.log('[-] Error occur @get_maple_minus_btn_status')
            log.log('[-] Error is '+str(e))
            return flag
    def get_original_unit_price(self):
        log = logger()
        driver = self.driver
        try:
            time.sleep(1)
            price = Element(driver,"SDP","mapleOriginalUnitPrice").get().text
            price = filter(lambda x: not re.match(r'^\s*$', x), price)
            price = price.replace(" ","")
            return price.encode("utf-8")
        except Exception as e:
            log.log('[-] Error occur @get_original_unit_price')
            log.log('[-] Error is '+str(e))
    def get_original_maple_price(self):
        log = logger()
        driver = self.driver
        try:
            time.sleep(1)
            price = Element(driver,"SDP","mapleOriginalSalePrice").get().text
            price = filter(lambda x: not re.match(r'^\s*$', x), price)
            original_price = price.encode("utf-8")
            original_price = self.__get_num(original_price)
            return original_price
        except Exception as e:
            log.log('[-] Error occur @get_original_unit_price')
            log.log('[-] Error is '+str(e))
    def get_tooltip_content(self,index):
        log = logger()
        driver = self.driver
        content = "No tooltip pop up!"
        try:
            time.sleep(1)
            elems = Element(driver,"SDP","mapleOption").get_element_list()
            leng = len(elems)
            index = index % leng
            elems[index].click()
            if Element(driver,"SDP","mapleTooltip").is_exist() and \
                Element(driver,"SDP","mapleTooltip").get().is_displayed():
                content = Element(driver,"SDP","tooltipContent").get().text
            content = filter(lambda x: not re.match(r'^\s*$', x), content)
            content = content.replace(" ","")
            return content.encode("utf-8"),leng
        except Exception as e:
            log.log('[-] Error occur @get_tooltip_content')
            log.log('[-] Error is '+str(e))
            return content,0
    def get_pinch_zoom_area(self):
        log = logger()
        driver = self.driver
        size_1 = []
        size_2 = []
        try:
            time.sleep(1)
            if (not Element(driver,"SDP","IDsParentView").is_exist()) or \
                    (not Element(driver,"SDP","IDsParentView").get().is_displayed()):
                i = 0
                for i in range(0,5):
                    driver.swipe(470, 800, 470, 400,400)
                    time.sleep(1)
                    flag = Element(driver,"SDP","IDsParentView").is_exist() and Element(driver,"SDP","IDsParentView").get().is_displayed()
                    if flag:
                        break
                if i == 4:
                    raise Exception("Could not find IDs element after swipe 5 times!")
                time.sleep(3)
                driver.switch_to.context("WEBVIEW")
                bound = Element(driver,"SDP","pinchZoomPic").get().size
                x0 = bound["width"]
                y0 = bound["height"]
                size_1.append(x0)
                size_1.append(y0)
                driver.switch_to.context("NATIVE_APP")
                time.sleep(3)
                driver.swipe(470,800,470,200,400)
                time.sleep(3)
                driver.switch_to.context("WEBVIEW")
                bound = Element(driver,"SDP","pinchZoomPic").get().size
                x1 = bound["width"]
                y1 = bound["height"]
                driver.switch_to.context("NATIVE_APP")
                time.sleep(1)
                size_2.append(x1)
                size_2.append(y1)
            else:
                time.sleep(3)
                driver.switch_to.context("WEBVIEW")
                bound = Element(driver,"SDP","pinchZoomPic").get().size
                x0 = bound["width"]
                y0 = bound["height"]
                size_1.append(x0)
                size_1.append(y0)
                driver.switch_to.context("NATIVE_APP")
                time.sleep(3)
                driver.swipe(470,800,470,200,400)
                time.sleep(3)
                driver.switch_to.context("WEBVIEW")
                bound = Element(driver,"SDP","pinchZoomPic").get().size
                x1 = bound["width"]
                y1 = bound["height"]
                driver.switch_to.context("NATIVE_APP")
                time.sleep(1)
                size_2.append(x1)
                size_2.append(y1)
            return size_1,size_2
        except Exception as e:
            log.log('[-] Error occur @get_pinch_zoom_area')
            log.log('[-] Error is '+str(e))
