import os
import sys

import time

from Controller import runnerController
import unittest

from Controller.apiController import CAPI
from Libs.Log import logger
from TestSuite import __init__


__author__ = 'kzhu'

class GlobalDeliveryTests(__init__):
    log = logger()
    CAPI = CAPI()

    @classmethod
    def setUpClass(cls):
        try:
            class_name = cls.__name__
            cls.log.log('<-----------Running in class ' + class_name + '-------------->' )
            super(GlobalDeliveryTests, cls).setUpClass()
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


    def test_sdp_add_product_limitation(self):
        self.DRIVER.initialize_pages()
        self.DRIVER.select_category_tab()
        self.DRIVER.select_global_product_category()
        self.DRIVER.select_sdp_item_with_options()
        option_price = self.DRIVER.select_an_option(1)
        price = self.DRIVER.get_product_price()
        title = self.DRIVER.get_product_title()
        id = self.DRIVER.get_Ids()
        product_details = self.CAPI.get_product_details(id['productID'],id['itemID'])
        product_info = self.CAPI.get_product_info(id['productID'],id['itemID'])
        buyable_quantity = product_details['buyableQuantity']
        productName = product_details['productName']
        fee = product_details['fee']
        feeValue = product_details['feeValue']
        remainAmount = product_info['remainAmount']
        salePrice = product_info['salePrice']
        self.assertEqual(title,productName)
        self.assertEqual(salePrice,option_price)
        self.assertEqual(price,option_price)
        self.DRIVER.add_to_purchase()
        minus_btn_status_before = self.DRIVER.get_minus_btn_status()
        self.assertFalse(minus_btn_status_before)
        add_btn_status_before = self.DRIVER.get_add_btn_status()
        self.assertTrue(add_btn_status_before)
        price_before = self.DRIVER.get_original_price()
        ship_fee_before = self.DRIVER.get_ship_fee()
        self.assertIn(ship_fee_before,fee)
        max_buy= self.DRIVER.add_products(7,buyable_quantity,remainAmount)
        add_btn_status = self.DRIVER.get_add_btn_status()
        minus_enabled_after = self.DRIVER.get_minus_btn_status()
        self.assertTrue(minus_enabled_after)
        self.assertTrue(add_btn_status)
        total = self.DRIVER.get_original_price()
        self.assertEqual(price_before*max_buy,total)
        quantity_after = self.DRIVER.get_quantity()
        self.assertEqual(max_buy,quantity_after)
        ship_fee_after = self.DRIVER.get_ship_fee()
        self.DRIVER.hidden_purchase()
        self.DRIVER.back_to_home()

    def test_sdp_add_product(self):
        self.DRIVER.initialize_pages()
        self.DRIVER.select_category_tab()
        self.DRIVER.select_global_product_category()
        self.DRIVER.select_sdp_item()
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

    def test_sdp_share(self):
        self.DRIVER.initialize_pages()
        self.DRIVER.select_category_tab()
        self.DRIVER.select_global_product_category()
        self.DRIVER.select_sdp_item()
        share_item_list = self.DRIVER.get_share_item()
        self.assertEqual(len(share_item_list),8)
        self.DRIVER.back_to_home()

    def test_sdp_option_selected(self):
        self.DRIVER.initialize_pages()
        self.DRIVER.select_category_tab()
        self.DRIVER.select_global_product_category()
        self.DRIVER.select_sdp_item_with_options()
        option_price = self.DRIVER.select_an_option(1)
        price = self.DRIVER.get_product_price()
        self.assertEqual(option_price,price)
        self.DRIVER.back_to_home()

    @unittest.skip("skip this case in for WEBVIEW")
    def test_sdp_pinch_zoom(self):
        self.DRIVER.initialize_pages()
        self.DRIVER.select_category_tab()
        self.DRIVER.select_global_product_category()
        self.DRIVER.select_sdp_item()
        location_before,location_after = self.DRIVER.get_pinch_zoom_area()
        self.assertListEqual(location_after,location_before)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(GlobalDeliveryTests)
    unittest.TextTestRunner(verbosity=2).run(suite)