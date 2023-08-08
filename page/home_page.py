import allure
from selenium.webdriver.common.by import By
from page.base import BasePage
from utils.log_utils import logger


class HomePage(BasePage):
    __BTN_ADD_MEMBER = (By.CSS_SELECTOR, "[node-type='addmember']")
    __MENU_CONTACTS = (By.ID, "menu_contacts")
    __URL_HOME_PAGE = 'https://work.weixin.qq.com/wework_admin/frame'

    def click_add_member(self):
        logger.info('点击添加成员按钮')
        with allure.step('点击添加成员按钮'):
            self.do_find(self.__BTN_ADD_MEMBER).click()
        from page.addmember_page import AddMemberPage
        return AddMemberPage(self.driver)

    def goto_home_page(self):
        logger.info('返回首页')
        with allure.step('返回首页'):
            self.do_goto_page(self.__URL_HOME_PAGE)
        return HomePage(self.driver)

    def click_menu_contacts(self):
        logger.info('点击菜单：通讯录')
        with allure.step('点击菜单：通讯录'):
            self.do_find(*self.__MENU_CONTACTS).click()
        from page.member_list_page import MemberListPage
        return MemberListPage(self.driver)
