import allure

from page.login_page import LoginPage
from utils.get_add_member_data import GetFakerData


@allure.feature("添加成员")
class TestAddMember:

    def setup_class(self):
        # 登录
        self.home = LoginPage().login()

    def teardown_class(self):
        # 退出浏览器
        self.home.quit()
        # pass

    def setup(self):
        self.fk = GetFakerData()

    def teardown(self):
        # 返回首页
        self.home = self.home.goto_home_page()

    @allure.story("主页入口添加成员")
    def test_add_member_from_homepage(self):
        result = self.home.click_add_member(). \
            edit_member_and_save(self.fk.get_random_name(), self.fk.get_random_id(),
                                 self.fk.get_random_phone()). \
            get_tips()
        assert result == "保存成功"

    @allure.story("通讯录入口添加成员")
    def test_add_member_from_memberlistpage(self):
        result = self.home.click_menu_contacts(). \
            click_add_member_btn(). \
            edit_member_and_save(self.fk.get_random_name(), self.fk.get_random_id(),
                                 self.fk.get_random_phone()). \
            get_tips()
        assert result == "保存成功"
