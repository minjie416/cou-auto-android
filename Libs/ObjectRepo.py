import os
from time import sleep
import xml.etree.ElementTree as elementTree
from pip import logger
from selenium.common.exceptions import NoSuchElementException


__author__ = 'kzhu'
activity = {}


def set_xml():
    """
    get the xml file's value
    :use:
    a = getXml(path)

    print(a.get(".module.GuideActivity").get("skip").get("type"))
    :param: xmlPath
    :return:activity
    """
    if len(activity) == 0:
        xml_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'View','element.xml')
        # open the xml file
        per = elementTree.parse(xml_path)
        all_element = per.findall('activity')

        for firstElement in all_element:
            activity_name = firstElement.get("name")

            element = {}

            for secondElement in firstElement.getchildren():
                element_name = secondElement.get("name")

                element_child = {}
                for thirdElement in secondElement.getchildren():

                    element_child[thirdElement.tag] = thirdElement.text

                element[element_name] = element_child
            activity[activity_name] = element

def get_el__dict(activity_name, element_name):
    """
    According to the activityName and elementName get element
    :param activity_name:
    :param element_name:
    :return:
    """
    set_xml()
    element_dict = activity.get(activity_name).get(element_name)
    return element_dict

class Element():

    def __init__(self, driver, activity_name, element_name):
        self.driver = driver
        self.activity_name = activity_name
        self.element_name = element_name
        element_dict = get_el__dict(self.activity_name, self.element_name)
        self.path_type = element_dict.get("pathtype")
        self.path_value = element_dict.get("pathvalue")

    def is_exist(self):
        """
        To determine whether an element is exits
        :return: TRUE or FALSE
        """
        try:
            if self.path_type == "ID":
                self.driver.find_element_by_id(self.path_value)
                return True
            if self.path_type == "CLASSNAME":
                self.driver.find_element_by_class_name(self.path_value)
                return True
            if self.path_type == "XPATH":
                self.driver.find_element_by_xpath(self.path_value)
                return True
            if self.path_type == "NAME":
                self.driver.find_element_by_name(self.path_value)
                return True
            if self.path_type == "LINKTEXT":
                self.driver.find_element_by_link_text(self.path_value)
                return True
            if self.path_type == "ACCESSIBILITY":
                self.driver.find_element_by_accessibility_id(self.path_value)
                return True
            return False
        except NoSuchElementException:
            return False

    def is_displayed(self):
        """
        To determine whether an element is exits
        :return: TRUE or FALSE
        """
        try:
            if self.path_type == "ID":
                return self.driver.find_element_by_id(self.path_value).is_displayed()

            if self.path_type == "CLASSNAME":
                return self.driver.find_element_by_class_name(self.path_value).is_displayed()
            if self.path_type == "XPATH":
                return self.driver.find_element_by_xpath(self.path_value).is_displayed()
            if self.path_type == "NAME":
                return self.driver.find_element_by_name(self.path_value).is_displayed()
            if self.path_type == "LINKTEXT":
                return self.driver.find_element_by_link_text(self.path_value).is_displayed()
            if self.path_type == "ACCESSIBILITY":
                return self.driver.find_element_by_accessibility_id(self.path_value).is_displayed()
            return False
        except NoSuchElementException:
            return False
    def does_exist(self):
        """
        To determine whether an element is exits
        :return:
        """
        i = 1
        while not self.is_exist():
            sleep(1)
            i += 1
            if i >= 10:
                return False
        else:
            return True

    def get(self):
        """
        get one element
        :return:
        """
        if self.does_exist():
            if self.path_type == "ID":
                element = self.driver.find_element_by_id(self.path_value)
                return element
            if self.path_type == "CLASSNAME":
                element = self.driver.find_element_by_class_name(self.path_value)
                return element
            if self.path_type == "XPATH":
                element = self.driver.find_element_by_xpath(self.path_value)
                return element
            if self.path_type == "NAME":
                element = self.driver.find_element_by_name(self.path_value)
                return element
            if self.path_type == "LINKTEXT":
                element = self.driver.find_element_by_link_text(self.path_value)
                return element
            if self.path_type == "ACCESSIBILITY":
                self.driver.find_element_by_accessibility_id(self.path_value)
            return None
        else:
            return None

    def gets(self, index):
        """
        get one element in elementList
        :param index
        :return:elements[index]
        """
        if self.does_exist():
            if self.path_type == "ID":
                elements = self.driver.find_elements_by_id(self.path_value)
                return elements[index]
            if self.path_type == "CLASSNAME":
                elements = self.driver.find_elements_by_class_name(self.path_value)
                return elements[index]
            if self.path_type == "XPATH":
                elements = self.driver.find_elements_by_xpath(self.path_value)
                return elements[index]
            if self.path_type == "NAME":
                elements = self.driver.find_elements_by_name(self.path_value)
                return elements[index]
            if self.path_type == "ACCESSIBILITY":
                elements = self.driver.find_elements_by_accessibility_id(self.path_value)
                return elements[index]
            return None
        else:
            return None
    def get_child_element(self,index,activity_name,element_name):
        """
        input the key
        :param values
        :return:
        """
        try:
            element_dict = get_el__dict(activity_name, element_name)
            path_type = element_dict.get("pathtype")
            path_value = element_dict.get("pathvalue")
            if self.path_type == "ID":
                if path_type == "ID":
                    element = self.driver.find_elements_by_id(self.path_value)
                    elem = element[index].find_element_by_id(path_value)
                    return elem
                if path_type == "CLASSNAME":
                    element = self.driver.find_elements_by_id(self.path_value)
                    elem = element[index].find_element_by_class_name(path_value)
                    return elem
                if path_type == "XPATH":
                    element = self.driver.find_elements_by_id(self.path_value)
                    elem = element.find_element_by_xpath(path_value)
                    return elem
                if path_type == "NAME":
                    element = self.driver.find_elements_by_id(self.path_value)
                    elem = element[index].find_element_by_name(path_value)
                    return elem
                if path_type == "ACCESSIBILITY":
                    element = self.driver.find_elements_by_id(self.path_value)
                    elem = element[index].find_element_by_accessibility_id(path_value)
                    return elem
            if self.path_type == "NAME":
                if path_type == "ID":
                    element = self.driver.find_elements_by_name(self.path_value)
                    elem = element[index].find_element_by_id(path_value)
                    return elem
                if path_type == "CLASSNAME":
                    element = self.driver.find_elements_by_name(self.path_value)
                    elem = element[index].find_element_by_class_name(path_value)
                    return elem
                if path_type == "XPATH":
                    element = self.driver.find_elements_by_name(self.path_value)
                    elem = element[index].find_element_by_xpath(path_value)
                    return elem
                if path_type == "NAME":
                    element = self.driver.find_elements_by_name(self.path_value)
                    elem = element[index].find_element_by_name(path_value)
                    return elem
                if path_type == "ACCESSIBILITY":
                    element = self.driver.find_elements_by_name(self.path_value)
                    elem = element[index].find_element_by_accessibility_id(path_value)
                    return elem
            if self.path_type == "CLASSNAME":
                if path_type == "ID":
                    element = self.driver.find_elements_by_class_name(self.path_value)
                    elem = element[index].find_element_by_id(path_value)
                    return elem
                if path_type == "CLASSNAME":
                    element = self.driver.find_elements_by_class_name(self.path_value)
                    elem = element[index].find_element_by_class_name(path_value)
                    return elem
                if path_type == "XPATH":
                    element = self.driver.find_elements_by_class_name(self.path_value)
                    elem = element[index].find_element_by_xpath(path_value)
                    return elem
                if path_type == "NAME":
                    element = self.driver.find_elements_by_class_name(self.path_value)
                    elem = element[index].find_element_by_name(path_value)
                    return elem
                if path_type == "ACCESSIBILITY":
                    element = self.driver.find_elements_by_class_name(self.path_value)
                    elem = element[index].find_element_by_accessibility_id(path_value)
                    return elem
            if self.path_type == "XPATH":
                if path_type == "ID":
                    element = self.driver.find_elements_by_xpath(self.path_value)
                    elem = element[index].find_element_by_id(path_value)
                    return elem
                if path_type == "CLASSNAME":
                    element = self.driver.find_elements_by_xpath(self.path_value)
                    elem = element[index].find_element_by_class_name(path_value)
                    return elem
                if path_type == "XPATH":
                    element = self.driver.find_elements_by_xpath(self.path_value)
                    elem = element[index].find_element_by_xpath(path_value)
                    return elem
                if path_type == "NAME":
                    element = self.driver.find_elements_by_xpath(self.path_value)
                    elem = element[index].find_element_by_name(path_value)
                    return elem
                if path_type == "ACCESSIBILITY":
                    element = self.driver.find_elements_by_xpath(self.path_value)
                    elem = element[index].find_element_by_accessibility_id(path_value)
                    return elem
        except AttributeError:
            raise
    def get_children_element(self,activity_name,element_name):
        """
        input the key
        :param values
        :return:
        """
        try:
            element_dict = get_el__dict(activity_name, element_name)
            path_type = element_dict.get("pathtype")
            path_value = element_dict.get("pathvalue")
            if self.path_type == "ID":
                if path_type == "ID":
                    element = self.driver.find_element_by_id(self.path_value)
                    elem = element.find_element_by_id(path_value)
                    return elem
                if path_type == "CLASSNAME":
                    element = self.driver.find_element_by_id(self.path_value)
                    elem = element.find_element_by_class_name(path_value)
                    return elem
                if path_type == "XPATH":
                    element = self.driver.find_element_by_id(self.path_value)
                    elem = element.find_element_by_xpath(path_value)
                    return elem
                if path_type == "NAME":
                    element = self.driver.find_element_by_id(self.path_value)
                    elem = element.find_element_by_name(path_value)
                    return elem
                if path_type == "ACCESSIBILITY":
                    element = self.driver.find_element_by_id(self.path_value)
                    elem = element.find_element_by_accessibility_id(path_value)
                    return elem
            if self.path_type == "NAME":
                if path_type == "ID":
                    element = self.driver.find_element_by_name(self.path_value)
                    elem = element.find_element_by_id(path_value)
                    return elem
                if path_type == "CLASSNAME":
                    element = self.driver.find_element_by_name(self.path_value)
                    elem = element.find_element_by_class_name(path_value)
                    return elem
                if path_type == "XPATH":
                    element = self.driver.find_element_by_name(self.path_value)
                    elem = element.find_element_by_xpath(path_value)
                    return elem
                if path_type == "NAME":
                    element = self.driver.find_element_by_name(self.path_value)
                    elem = element.find_element_by_name(path_value)
                    return elem
                if path_type == "ACCESSIBILITY":
                    element = self.driver.find_element_by_name(self.path_value)
                    elem = element.find_element_by_accessibility_id(path_value)
                    return elem
            if self.path_type == "CLASSNAME":
                if path_type == "ID":
                    element = self.driver.find_element_by_class_name(self.path_value)
                    elem = element.find_element_by_id(path_value)
                    return elem
                if path_type == "CLASSNAME":
                    element = self.driver.find_element_by_class_name(self.path_value)
                    elem = element.find_element_by_class_name(path_value)
                    return elem
                if path_type == "XPATH":
                    element = self.driver.find_element_by_class_name(self.path_value)
                    elem = element.find_element_by_xpath(path_value)
                    return elem
                if path_type == "NAME":
                    element = self.driver.find_element_by_class_name(self.path_value)
                    elem = element.find_element_by_name(path_value)
                    return elem
                if path_type == "ACCESSIBILITY":
                    element = self.driver.find_element_by_class_name(self.path_value)
                    elem = element.find_element_by_accessibility_id(path_value)
                    return elem
            if self.path_type == "XPATH":
                if path_type == "ID":
                    element = self.driver.find_element_by_xpath(self.path_value)
                    elem = element.find_element_by_id(path_value)
                    return elem
                if path_type == "CLASSNAME":
                    element = self.driver.find_element_by_xpath(self.path_value)
                    elem = element.find_element_by_class_name(path_value)
                    return elem
                if path_type == "XPATH":
                    element = self.driver.find_element_by_xpath(self.path_value)
                    elem = element.find_element_by_xpath(path_value)
                    return elem
                if path_type == "NAME":
                    element = self.driver.find_element_by_xpath(self.path_value)
                    elem = element.find_element_by_name(path_value)
                    return elem
                if path_type == "ACCESSIBILITY":
                    element = self.driver.find_element_by_xpath(self.path_value)
                    elem = element.find_element_by_accessibility_id(path_value)
                    return elem
        except AttributeError:
            raise
    def get_child_elements(self,index,activity_name,element_name):
        """
        input the key
        :param values
        :return:
        """
        try:
            element_dict = get_el__dict(activity_name, element_name)
            path_type = element_dict.get("pathtype")
            path_value = element_dict.get("pathvalue")
            if self.path_type == "ID":
                if path_type == "ID":
                    element = self.driver.find_elements_by_id(self.path_value)
                    elem = element[index].find_elements_by_id(path_value)
                    return elem
                if path_type == "CLASSNAME":
                    element = self.driver.find_elements_by_id(self.path_value)
                    elem = element[index].find_elements_by_class_name(path_value)
                    return elem
                if path_type == "XPATH":
                    element = self.driver.find_elements_by_id(self.path_value)
                    elem = element.find_elements_by_xpath(path_value)
                    return elem
                if path_type == "NAME":
                    element = self.driver.find_elements_by_id(self.path_value)
                    elem = element[index].find_elements_by_name(path_value)
                    return elem
                if path_type == "ACCESSIBILITY":
                    element = self.driver.find_elements_by_id(self.path_value)
                    elem = element[index].find_elements_by_accessibility_id(path_value)
                    return elem
            if self.path_type == "NAME":
                if path_type == "ID":
                    element = self.driver.find_elements_by_name(self.path_value)
                    elem = element[index].find_elements_by_id(path_value)
                    return elem
                if path_type == "CLASSNAME":
                    element = self.driver.find_elements_by_name(self.path_value)
                    elem = element[index].find_elements_by_class_name(path_value)
                    return elem
                if path_type == "XPATH":
                    element = self.driver.find_elements_by_name(self.path_value)
                    elem = element[index].find_elements_by_xpath(path_value)
                    return elem
                if path_type == "NAME":
                    element = self.driver.find_elements_by_name(self.path_value)
                    elem = element[index].find_elements_by_name(path_value)
                    return elem
                if path_type == "ACCESSIBILITY":
                    element = self.driver.find_elements_by_name(self.path_value)
                    elem = element[index].find_elements_by_accessibility_id(path_value)
                    return elem
            if self.path_type == "CLASSNAME":
                if path_type == "ID":
                    element = self.driver.find_elements_by_class_name(self.path_value)
                    elem = element[index].find_elements_by_id(path_value)
                    return elem
                if path_type == "CLASSNAME":
                    element = self.driver.find_elements_by_class_name(self.path_value)
                    elem = element[index].find_elements_by_class_name(path_value)
                    return elem
                if path_type == "XPATH":
                    element = self.driver.find_elements_by_class_name(self.path_value)
                    elem = element[index].find_elements_by_xpath(path_value)
                    return elem
                if path_type == "NAME":
                    element = self.driver.find_elements_by_class_name(self.path_value)
                    elem = element[index].find_elements_by_name(path_value)
                    return elem
                if path_type == "ACCESSIBILITY":
                    element = self.driver.find_elements_by_class_name(self.path_value)
                    elem = element[index].find_elements_by_accessibility_id(path_value)
                    return elem
            if self.path_type == "XPATH":
                if path_type == "ID":
                    element = self.driver.find_elements_by_xpath(self.path_value)
                    elem = element[index].find_elements_by_id(path_value)
                    return elem
                if path_type == "CLASSNAME":
                    element = self.driver.find_elements_by_xpath(self.path_value)
                    elem = element[index].find_elements_by_class_name(path_value)
                    return elem
                if path_type == "XPATH":
                    element = self.driver.find_elements_by_xpath(self.path_value)
                    elem = element[index].find_elements_by_xpath(path_value)
                    return elem
                if path_type == "NAME":
                    element = self.driver.find_elements_by_xpath(self.path_value)
                    elem = element[index].find_elements_by_name(path_value)
                    return elem
                if path_type == "ACCESSIBILITY":
                    element = self.driver.find_elements_by_xpath(self.path_value)
                    elem = element[index].find_elements_by_accessibility_id(path_value)
                    return elem
        except AttributeError:
            raise
    def get_children_elements(self,activity_name,element_name):
        """
        input the key
        :param values
        :return:
        """
        try:
            element_dict = get_el__dict(activity_name, element_name)
            path_type = element_dict.get("pathtype")
            path_value = element_dict.get("pathvalue")
            if self.path_type == "ID":
                if path_type == "ID":
                    element = self.driver.find_element_by_id(self.path_value)
                    elem = element.find_elements_by_id(path_value)
                    return elem
                if path_type == "CLASSNAME":
                    element = self.driver.find_element_by_id(self.path_value)
                    elem = element.find_elements_by_class_name(path_value)
                    return elem
                if path_type == "XPATH":
                    element = self.driver.find_element_by_id(self.path_value)
                    elem = element.find_elements_by_xpath(path_value)
                    return elem
                if path_type == "NAME":
                    element = self.driver.find_element_by_id(self.path_value)
                    elem = element.find_elements_by_name(path_value)
                    return elem
                if path_type == "ACCESSIBILITY":
                    element = self.driver.find_element_by_id(self.path_value)
                    elem = element.find_elements_by_accessibility_id(path_value)
                    return elem
            if self.path_type == "NAME":
                if path_type == "ID":
                    element = self.driver.find_element_by_name(self.path_value)
                    elem = element.find_elements_by_id(path_value)
                    return elem
                if path_type == "CLASSNAME":
                    element = self.driver.find_element_by_name(self.path_value)
                    elem = element.find_elements_by_class_name(path_value)
                    return elem
                if path_type == "XPATH":
                    element = self.driver.find_element_by_name(self.path_value)
                    elem = element.find_elements_by_xpath(path_value)
                    return elem
                if path_type == "NAME":
                    element = self.driver.find_element_by_name(self.path_value)
                    elem = element.find_elements_by_name(path_value)
                    return elem
                if path_type == "ACCESSIBILITY":
                    element = self.driver.find_element_by_name(self.path_value)
                    elem = element.find_elements_by_accessibility_id(path_value)
                    return elem
            if self.path_type == "CLASSNAME":
                if path_type == "ID":
                    element = self.driver.find_element_by_class_name(self.path_value)
                    elem = element.find_elements_by_id(path_value)
                    return elem
                if path_type == "CLASSNAME":
                    element = self.driver.find_element_by_class_name(self.path_value)
                    elem = element.find_elements_by_class_name(path_value)
                    return elem
                if path_type == "XPATH":
                    element = self.driver.find_element_by_class_name(self.path_value)
                    elem = element.find_elements_by_xpath(path_value)
                    return elem
                if path_type == "NAME":
                    element = self.driver.find_element_by_class_name(self.path_value)
                    elem = element.find_elements_by_name(path_value)
                    return elem
                if path_type == "ACCESSIBILITY":
                    element = self.driver.find_element_by_class_name(self.path_value)
                    elem = element.find_elements_by_accessibility_id(path_value)
                    return elem
            if self.path_type == "XPATH":
                if path_type == "ID":
                    element = self.driver.find_element_by_xpath(self.path_value)
                    elem = element.find_elements_by_id(path_value)
                    return elem
                if path_type == "CLASSNAME":
                    element = self.driver.find_element_by_xpath(self.path_value)
                    elem = element.find_elements_by_class_name(path_value)
                    return elem
                if path_type == "XPATH":
                    element = self.driver.find_element_by_xpath(self.path_value)
                    elem = element.find_elements_by_xpath(path_value)
                    return elem
                if path_type == "NAME":
                    element = self.driver.find_element_by_xpath(self.path_value)
                    elem = element.find_elements_by_name(path_value)
                    return elem
                if path_type == "ACCESSIBILITY":
                    element = self.driver.find_element_by_xpath(self.path_value)
                    elem = element.find_elements_by_accessibility_id(path_value)
                    return elem
        except AttributeError:
            raise

    def get_element_list(self):
        """
        get elementList
        :return:elements
        """
        if self.does_exist():
            if self.path_type == "ID":
                element_list = self.driver.find_elements_by_id(self.path_value)
                return element_list
            if self.path_type == "CLASSNAME":
                element_list = self.driver.find_elements_by_class_name(self.path_value)
                return element_list
            if self.path_type == "XPATH":
                element_list = self.driver.find_elements_by_xpath(self.path_value)
                return element_list
            if self.path_type == "NAME":
                element_list = self.driver.find_elements_by_name(self.path_value)
                return element_list
            if self.path_type == "ACCESSIBILITY":
                element_list = self.driver.find_elements_by_accessibility_id(self.path_value)
                return element_list
            return None
        else:
            return None


    def get_lists(self,index):
        """
        get elementList
        :return:elements
        """
        if self.does_exist():
            if self.path_type == "ID":
                elements = self.driver.find_elements_by_id(self.path_value)
                return elements[index].find_elements_by_id("com.coupang.mobile:id/item")
            if self.path_type == "CLASSNAME":
                elements = self.driver.find_elements_by_class_name(self.path_value)
                return elements[index].find_elements_by_id("com.coupang.mobile:id/item")
            if self.path_type == "XPATH":
                elements = self.driver.find_elements_by_xpath(self.path_value)
                return elements[index].find_elements_by_id("com.coupang.mobile:id/item")
            if self.path_type == "NAME":
                elements = self.driver.find_elements_by_name(self.path_value)
                return elements[index].find_elements_by_id("com.coupang.mobile:id/item")
            if self.path_type == "ACCESSIBILITY":
                elements = self.driver.find_elements_by_accessibility_id(self.path_value)
                return elements[index].find_elements_by_id("com.coupang.mobile:id/item")
            return None
        else:
            return None

    def click(self):
        """
        click element
        :return:
        """
        try:
            element = self.get()
            element.click()
        except AttributeError:
            raise

    def clicks(self, index):
        """
        click element
        :return:
        """
        try:
            element = self.gets(index)
            element.click()
        except AttributeError:
            raise

    def send_key(self, values):
        """
        input the key
        :param values
        :return:
        """
        try:
            element = self.get()
            element.clear()
            element.send_keys(values)
        except AttributeError:
            raise

    def send_keys(self, index, values):
        """
        input the key
        :param index
        :param values
        :return:
        """
        try:
            element = self.gets(index)
            element.clear()
            element.send_keys(values)

        except AttributeError:
            raise

    def get_attribute(self, attribute):
        """
        get the element attribute
        :param attribute:
        :return:value
        """
        try:
            element = self.get()
            value = element.get_attribute(attribute)
            return value
        except AttributeError:
            raise