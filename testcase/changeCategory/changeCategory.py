# coding=utf-8

# TODO: "from testflow.lib" should be renamed according to your actual package name
from case.android_app import AndroidAppCase
from utils.installation import install_android_app
from airtest.core.api import device as current_device
from airtest.core.api import *


class ChangeCategoryCase(AndroidAppCase):
    @classmethod
    def name(cls):
        return 'APKSearch (customized name)'

    @classmethod
    def getMetaInfo(cls):
        return {
            "author": 'baisong',
            "remark": '2018-08-22',
        }

    @classmethod
    def setUpClass(cls):
        super(ChangeCategoryCase, cls).setUpClass()
        cls.package_name = 'com.sogou.androidtool'
        apk_path = cls.R('res/app/com.sogou.androidtool.apk')
        install_android_app(current_device().adb, apk_path)
        start_app(cls.package_name)

    @classmethod
    def tearDownClass(cls):
        stop_app(cls.package_name)
        super(ChangeCategoryCase, cls).tearDownClass()

    def setUp(self):
        pass
        # clear previous result
        # clr = self.poco('com.google.android.calculator:id/clr')
        # if clr.exists():
        #     clr.click()


class SearchApp1(ChangeCategoryCase):
    def runTest(self):
        accountPic = Template(self.R('res/img/apksearch/account.png'))
        self.assertTrue(exists(accountPic), 'App started.')

        # self.poco(text="发现").click()
        # faxianPic = Template(self.R('res/img/changeCategory/faxian.png'))
        # self.assertTrue(exists(faxianPic), 'faxian.')

        self.poco(text="管理").click()
        nav_manage_selected = Template(self.R('res/img/changeCategory/nav_manage_unselected.png'), rgb=True, threshold=0.7)
        nav_select_selected = Template(self.R('res/img/changeCategory/nav_select_selected.png'), rgb=True, threshold=1)
        nav_app_selected = Template(self.R('res/img/changeCategory/nav_app_selected.png'), rgb=True, threshold=1)
        nav_game_selected = Template(self.R('res/img/changeCategory/nav_game_selected.png'), rgb=True, threshold=1)

        # nav_manage_unselected = Template(self.R('res/img/changeCategory/nav_manage_unselected.png'), rgb=True)
        self.assertTrue(exists(nav_manage_selected), 'guanli')
        self.assertFalse(exists(nav_select_selected), 'select')
        self.assertFalse(exists(nav_app_selected), 'app')
        self.assertFalse(exists(nav_game_selected), 'game')

        # self.poco(text="精品").click()
        # nav_select_selected = Template(self.R('res/img/changeCategory/nav_select_selected.png'), rgb=True)
        # nav_select_unselected = Template(self.R('res/img/changeCategory/nav_select_unselected.png'), rgb=True)
        # self.assertTrue(exists(nav_select_selected), 'jingpin')
        #
        # self.poco(text="应用").click()
        # nav_app_selected = Template(self.R('res/img/changeCategory/nav_app_selected.png'), rgb=True)
        # nav_app_unselected = Template(self.R('res/img/changeCategory/nav_app_unselected.png'), rgb=True)
        # self.assertTrue(exists(nav_app_selected), 'yingyong')
        #
        # self.poco(text="游戏").click()
        # nav_game_selected = Template(self.R('res/img/changeCategory/nav_game_selected.png'), rgb=True)
        # nav_game_unselected = Template(self.R('res/img/changeCategory/nav_game_unselected.png'), rgb=True)
        # self.assertTrue(exists(nav_game_selected), 'youxi')



if __name__ == '__main__':
    import pocounit
    pocounit.main()
