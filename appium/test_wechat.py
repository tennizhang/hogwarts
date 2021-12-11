from appium.webdriver.common.mobileby import MobileBy
from hogwarts.appium.addmemberpage import AddMemberPage
from hogwarts.appium.mainpage import MainPage
from hogwarts.appium.contactpage import ContactPage
from hogwarts.appium.workstudiopage import WorkStudioPage


class TestWechat:
    def test_addmember(self):
        name, phonenumber = 'acc', '12300873333'
        MainPage().getintocontactpage().addmem().addmember(name, phonenumber)
        AddMemberPage().addmembersucc()

    def test_checkin(self):
        MainPage().gotoWSpage().checkinoutside('打卡')
        assert WorkStudioPage().checkinoutsidesucc

    def test_delmember(self):
        username = 'acc'
        from hogwarts.appium.memberpage import MemberPage
        MainPage().getintocontactpage().searchmember(username).delmember()
        assert ContactPage().numberofnames() - 1 == MemberPage().delmemberresult()