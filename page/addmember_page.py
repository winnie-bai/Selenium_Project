import allure
from selenium.webdriver.common.by import By
from page.base import BasePage
from utils.log_utils import logger


class AddMemberPage(BasePage):
    __INPUT_USERNAME = (By.ID, "username")
    __INPUT_ACCTID = (By.ID, "memberAdd_acctid")
    __INPUT_PHONE = (By.ID, "memberAdd_phone")
    __BTN_SAVE_MEMBER = (By.CSS_SELECTOR, ".js_btn_save")

    @allure.title("编辑成员并保存")
    def edit_member_and_save(self, username, acctid, phone):
        logger.debug(f"输入姓名{username},用户id{acctid},电话{phone}")
        with allure.step(f"输入姓名{username}"):
            self.do_send_keys(username, *self.__INPUT_USERNAME)
        with allure.step(f"输入用户id{acctid}"):
            self.do_send_keys(acctid, *self.__INPUT_ACCTID)
        with allure.step(f"输入电话{phone}"):
            self.do_send_keys(phone, *self.__INPUT_PHONE)
        with allure.step("点击保存"):
            self.do_find(*self.__BTN_SAVE_MEMBER).click()
        from page.member_list_page import MemberListPage
        return MemberListPage(self.driver)

    def get_attribute_input_username(self):
        return self.__INPUT_USERNAME
