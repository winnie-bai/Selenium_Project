import os

import yaml
from page.base import BasePage
from utils.log_utils import logger


class LoginPage(BasePage):

    _base_url = 'https://work.weixin.qq.com/wework_admin/frame'

    def login(self):
        # 读取本地cookie导入浏览器设置
        logger.debug("登录")
        dir_path = os.path.dirname(os.path.dirname(__file__))
        file_path = os.path.join(dir_path, 'data', 'cookie.yaml')
        with open(file_path) as f:
            cookies = yaml.safe_load(f)
        for cookie in cookies:
            self.do_set_cookies(cookie)
        self.refresh()
        from page.home_page import HomePage
        return HomePage(self.driver)
