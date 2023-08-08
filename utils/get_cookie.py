from time import sleep

import yaml

from page.base import BasePage


class GetCookie(BasePage):
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame'

    def get_cookie(self):
        # 等待10s手工扫码登录
        sleep(10)
        cookies = self.driver.get_cookies()
        with open('../data/cookie.yaml', 'w', encoding='u8') as f:
            yaml.safe_dump(cookies, f)


if __name__ == '__main__':
    GetCookie().get_cookie()
