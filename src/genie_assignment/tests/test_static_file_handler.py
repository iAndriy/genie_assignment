__author__ = 'aivaney'

from selenium import webdriver
from unittest import TestCase
from tornado.testing import get_unused_port, AsyncTestCase
from genie_assignment.lib import semantic_server
from genie_assignment.lib import utils
import threading
import time
import os
class FileHandlerTest(TestCase):

    def setUp(self):
        self.port=get_unused_port()
        self.driver = webdriver.Firefox()

        self.home_page = 'index.html'
        self.definitions_link_xpath = '//*[@id="menu"]/div[1]/div/a[1]'
        self.definitions_link_css = 'a.item[href*=definitions]'
        self.overview_link_xpath = '//*[@id="menu"]/div[1]/div/a[2]'
        self.overview_link_css = 'a.item[href*=overview]'
        self.script_xpath = '/html/body/script[2]'
        self.introduction_block_css = 'div.introduction'
        self.menu_xpath = '//*[@id="example"]/div[3]'
        self.URL = "http://localhost:%s/%s" % (self.port, self.home_page)

        self.process_thread = threading.Thread(target=semantic_server.start_semantic_ui_server, args=(self.port,))
        self.process_thread.start()

    def tearDown(self):
        self.driver.quit()
        semantic_server.stop_tornado()
        self.process_thread.join()

    def test_js_injection(self):
        """
        Test js function expression injection as variable by inserting say_holla_from_selenium method and call function
        to change 'href' attribute value of definitions page urls to 'www.google.com'
        """
        self.driver.get(self.URL)
        try:
            script = self.driver.find_element_by_xpath(self.script_xpath)
        except:
            script = None
        assert script is None
        var_name = 'say_holla_from_selenium'
        js_func_expr = 'function(str){ alert(str);};'
        if utils.insert_js_as_var(js_func_expr, var_name, self.driver):
            script = self.driver.find_element_by_xpath(self.script_xpath)
            script_text = script.get_attribute('text')
            self.driver.execute_script(var_name+"('Holla from Selenium!');")
            # Sleep to view 'Holla from Selenium' message
            time.sleep(3)
            assert var_name in script_text
            assert js_func_expr in script_text

    def test_link_clicking(self):
        self.driver.get(self.URL)
        assert "index.html" in self.driver.current_url

        # Click on menu_xpath to open menu grid. Reason of such move is that Firefox driver work incorrectly
        # with hidden menus, so in case if we won't activate menu grid, error will be raised
        # find_element_by_css_selector(self.overview_link_css).click()
        self.driver.find_element_by_xpath(self.menu_xpath).click()
        self.driver.find_element_by_css_selector(self.overview_link_css).click()
        assert "index.html" not in self.driver.current_url
        assert "overview.html" in self.driver.current_url

    def test_attribute_changing(self):
        self.driver.get(self.URL)
        definitions_link = self.driver.find_element_by_css_selector(self.definitions_link_css)
        assert definitions_link.get_attribute('text') == 'Definitions'
        assert 'introduction/definitions.html' in definitions_link.get_attribute('href')
        var_name = 'replace_attribute_by_x_path'
        js_val = 'function(xpath, attr, val){ var elem = document.evaluate( xpath ,document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null ).singleNodeValue;' \
                 'elem.setAttribute(attr,val);};'
        if utils.insert_js_as_var(js_val, var_name, self.driver):
            self.driver.execute_script(var_name+"('%s','href', 'introduction/overview.html');"%(self.definitions_link_xpath))
            assert 'introduction/overview.html' in definitions_link.get_attribute('href')

    def test_element_removing(self):
        self.driver.get(self.URL)
        introduction_block = self.driver.find_element_by_css_selector(self.introduction_block_css)
        path = os.path.join(os.path.dirname(__file__),'screenshots')
        self.driver.save_screenshot(os.path.join(path, 'test_element_rm_before.png'))
        self.driver.execute_script("""
                                      var element = arguments[0];
                                      element.parentNode.removeChild(element);
                                      """, introduction_block)
        self.driver.save_screenshot(os.path.join(path, 'test_element_rm_after.png'))
        try:
            introduction_block = self.driver.find_element_by_css_selector(self.introduction_block_css)
        #handle exception in case if introduction_block doesn't exist.
        except:
            introduction_block = None
        assert introduction_block is None


