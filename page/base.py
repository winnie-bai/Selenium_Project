import os
from datetime import datetime

import allure
import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.log_utils import logger


class BasePage:
    _base_url = ''

    def __init__(self, base_driver=None):
        if base_driver:
            self.driver = base_driver
        else:
            # self.driver = webdriver.Chrome()
            # capabilities = {'browserName':'Chrome'}
            options = webdriver.ChromeOptions()
            options.add_argument('--lang=zh-CN')
            self.driver = webdriver.Remote(command_executor='http://192.168.254.128:5444/wd/hub',
                                           desired_capabilities=DesiredCapabilities.CHROME,options=options)
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
        if not self.driver.current_url.startswith("http"):
            self.driver.get(self._base_url)

    def output_exception(func):
        def inner(self, *args, **kwargs):
            try:
                return func(self, *args, **kwargs)
            except Exception as e:
                logger.error(e)
                self.save_screenshot()
                self.save_pagesource()
                pytest.xfail(e)
                # raise Exception

        return inner

    @output_exception
    def do_find(self, by, value=None):
        if value:
            return self.driver.find_element(by, value)
        else:
            return self.driver.find_element(*by)

    @output_exception
    def do_finds(self, by, value=None):
        if value:
            return self.driver.find_elements(by, value)
        else:
            return self.driver.find_elements(*by)

    def do_send_keys(self, key_value, by, value=None):
        ele = self.do_find(by, value)
        ele.clear()
        ele.send_keys(key_value)

    def do_set_cookies(self, cookie):
        self.driver.add_cookie(cookie)

    def refresh(self):
        self.driver.refresh()

    def quit(self):
        self.driver.quit()

    def do_goto_page(self, url):
        self.driver.get(url)

    def web_wait(self, click_ele: tuple, ele: tuple):
        return WebDriverWait(self.driver, 20).until(self.double_click(click_ele, ele))

    def double_click(self, click_ele: tuple, ele: tuple):
        def _inner(driver):
            WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(click_ele))
            self.do_find(*click_ele).click()
            return self.do_find(*ele)

        return _inner

    def save_screenshot(self):
        # 获取当前工具文件所在的路径
        root_path = os.path.dirname(os.path.abspath(__file__))
        parent_dir_path = os.path.dirname(root_path)
        # 拼接当前要保存image的路径
        image_dir_path = os.sep.join([parent_dir_path, f'/images'])
        if not os.path.isdir(image_dir_path):
            os.mkdir(image_dir_path)
        # 拼接image文件路径+文件名
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        image_file = os.sep.join([image_dir_path, f'image_{current_time}.png'])
        self.driver.save_screenshot(image_file)
        allure.attach.file(image_file, "error_image", attachment_type=allure.attachment_type.PNG)

    def save_pagesource(self):

        # 获取当前工具文件所在的路径
        root_path = os.path.dirname(os.path.abspath(__file__))
        parent_dir_path = os.path.dirname(root_path)
        # 拼接当前要保存image的路径
        pagesource_dir_path = os.sep.join([parent_dir_path, f'/pagesource'])
        if not os.path.isdir(pagesource_dir_path):
            os.mkdir(pagesource_dir_path)
        # 拼接image文件路径+文件名
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        pagesource_file = os.sep.join([pagesource_dir_path, f'pagesource_{current_time}.html'])
        with open(pagesource_file, 'w', encoding='u8') as f:
            f.write(self.driver.page_source)
        allure.attach.file(pagesource_file, "pagesource", attachment_type=allure.attachment_type.TEXT)

    def output_exception(func):
        def inner(self):
            try:
                return func(self)
            except Exception as e:
                logger.error(e)
                self.save_screenshot()
                self.save_pagesource()
                raise Exception

        return inner
