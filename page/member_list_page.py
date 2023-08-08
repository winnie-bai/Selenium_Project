import allure
from selenium.webdriver.common.by import By
from page.base import BasePage
from utils.log_utils import logger


class MemberListPage(BasePage):
    __TIPS_SAVE = (By.ID, "js_tips")
    __BTN_ADD_MEMBER = (By.CSS_SELECTOR, ".ww_operationBar>.js_add_member")

    def get_tips(self):
        with allure.step("获取提示文案"):
            res = self.do_find(*self.__TIPS_SAVE).text
        logger.debug(f"获取提示文案为【{res}】")
        return res

    def click_add_member_btn(self):
        from page.addmember_page import AddMemberPage
        logger.info("点击【添加成员】按钮")
        with allure.step("点击【添加成员】按钮"):
            self.web_wait(self.__BTN_ADD_MEMBER, AddMemberPage(self.driver).get_attribute_input_username())
        return AddMemberPage(self.driver)
