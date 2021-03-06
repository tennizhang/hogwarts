from appium.webdriver.common.mobileby import MobileBy
from hogwarts.appium.addmemberpage import AddMemberPage
from hogwarts.appium.mainpage import MainPage
from hogwarts.appium.contactpage import ContactPage
from hogwarts.appium.workstudiopage import WorkStudioPage





class TestWechat:
    def setup_class(self):
        MainPage().start_app()

    def teardown(self):
        MainPage().app_back()

    def teardown_class(self):
        MainPage().app_stop()

    def test_addmember(self):
        name = 'acc'
        phonenumber ='13344466103'
        MainPage().getintocontactpage().addmem().addmember(name, phonenumber)
        AddMemberPage().addmembersucc()

    def test_checkin(self):
        MainPage().gotoWSpage().checkinoutside('打卡')
        assert WorkStudioPage().checkinoutsidesucc

    def test_delmember(self):
        username = 'acc'
        from hogwarts.appium.memberpage import MemberPage
        MainPage().getintocontactpage().searchmember(username).delmember(username)
        assert ContactPage().numberofnames() - 1 == MemberPage().delmemberresult()