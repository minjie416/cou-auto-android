import unittest
import os
import csv
import time
import sys

from Libs import HTMLReport
from Libs.AppiumManager import AppiumManager

__author__ = 'kzhu'

def load_suite(modules_to_test):
    suite = unittest.TestSuite()
    for module in map(__import__,modules_to_test):
        suite.addTest(unittest.findTestCases(module))
    return suite

def load_tests(modules_to_test):
    suites = [unittest.defaultTestLoader.loadTestsFromName(module_name) for module_name in modules_to_test]
    testSuite = unittest.TestSuite(suites)
    return testSuite

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    appium = AppiumManager()
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    suites = []
    with open(BASE_DIR+'/config.csv') as configfile:
        reader = csv.DictReader(configfile)
        for row in reader:
            sign = row['ToBeExecuted'].lower()
            if sign == 'yes':
                suites.append(row['TestSuite'])
    suite = load_tests(suites)
    today = time.strftime("%Y%m%d")
    fp = file(BASE_DIR+'/Results/testing_report_'+today+'.html','wb')
    runner = HTMLReport.HTMLTestRunner(
        stream = fp,
        title ='Testing Report',
        description='This demonstrates the report output by HTMLTestRunner.'
    )
    runner.run(suite)
    appium.release_appium()


