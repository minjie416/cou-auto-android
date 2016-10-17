import ConfigParser
import os
import sys

import time

from Controller import runnerController
import unittest
from Libs.Log import logger
from TestSuite import __init__
from Controller.apiController import CAPI

__author__ = 'kzhu'

class SearchTests(__init__):
    log = logger()
    CAPI = CAPI()
    ini_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'View','productId.ini')
    try:
        config = ConfigParser.ConfigParser()
        config.read(ini_path)
    except ConfigParser.MissingSectionHeaderError, e:
        raise str(e)

    @classmethod
    def setUpClass(cls):
        try:
            class_name = cls.__name__
            cls.log.log('<-----------Running in class ' + class_name + '-------------->' )
            super(SearchTests, cls).setUpClass()
        except Exception:
            cls.log.log('[+] Trying to start a webdriver but not the first one')
            cls.DRIVER = runnerController.Runner()

    @classmethod
    def tearDownClass(cls):
        class_name = cls.__name__
        cls.log.log('<-----------End running class ' + class_name + '-------------->' )

    def setUp(self):
        self.BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.case_name = self.id().split('.')[-1]
        self.today = time.strftime("%Y%m%d")



    def tearDown(self):
        if sys.exc_info()[0]:
            file = os.path.realpath(__file__)
            file_names = file.rsplit("/",1)
            file_name = file_names[1].strip()
            index = file_name.index(".")
            file_name = file_name[:index]
            directory = self.BASE_DIR +'/Results/' + file_name
            if not os.path.exists(directory):
                os.makedirs(directory)
            self.DRIVER.take_screenshot(self.case_name +'_'+self.today +'.png',directory)
        pass


    def test_sdp_add_srp(self):
        self.DRIVER.initialize_pages()
        self.DRIVER.select_home_tab()
        self.DRIVER.select_search_product("BSN")
        self.DRIVER.select_sdp_item_srp()
        title = self.DRIVER.get_product_title()
        self.assertIn("BSN",title)
        price = self.DRIVER.get_product_price()
        title = self.DRIVER.get_product_title()
        id = self.DRIVER.get_Ids()
        product_details = self.CAPI.get_product_details(id['productID'],id['itemID'])
        product_info = self.CAPI.get_product_info(id['productID'],id['itemID'])
        buyable_quantity = product_details['buyableQuantity']
        productName = product_details['productName']
        fee = product_details['fee']
        remainAmount = product_info['remainAmount']
        salePrice = product_info['salePrice']
        self.assertEqual(salePrice,price)
        self.assertEqual(title,productName)
        self.DRIVER.add_to_purchase()
        minus_btn_status_before = self.DRIVER.get_minus_btn_status()
        self.assertFalse(minus_btn_status_before)
        add_btn_status_before = self.DRIVER.get_add_btn_status()
        self.assertTrue(add_btn_status_before)
        price_before = self.DRIVER.get_original_price()
        ship_fee_before = self.DRIVER.get_ship_fee()
        self.assertIn(ship_fee_before,fee)
        max_buy = self.DRIVER.add_products(2,buyable_quantity,remainAmount)
        minus_enabled_after = self.DRIVER.get_minus_btn_status()
        self.assertTrue(minus_enabled_after)
        total = self.DRIVER.get_original_price()
        self.assertEqual(price_before*max_buy,total)
        quantity_after = self.DRIVER.get_quantity()
        self.assertEqual(max_buy,quantity_after)
        ship_fee_after = self.DRIVER.get_ship_fee()
        self.DRIVER.hidden_purchase()
        self.DRIVER.back_to_home()


    def test_ddp_srp(self):
        self.DRIVER.initialize_pages()
        self.DRIVER.select_home_tab()
        self.DRIVER.select_search_product("diaper")
        info = self.DRIVER.get_clp_srp()
        self.assertNotEqual(info,"")

    def test_case_multiple_options(self):
        products = self.config.get('NO_OPTION','productId')
        productIds = products.split(",")
        for productId in productIds:
            productId = productId.strip()
            self.DRIVER.initialize_pages()
            self.DRIVER.select_home_tab()
            self.DRIVER.select_search_product(productId)
            self.DRIVER.get_searched_results()








if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SearchTests)
    unittest.TextTestRunner(verbosity=2).run(suite)