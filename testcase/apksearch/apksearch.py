# coding=utf-8

# TODO: "from testflow.lib" should be renamed according to your actual package name
from lib.case.android_app import AndroidAppCase
from lib.utils.installation import install_android_app
from airtest.core.api import device as current_device
from airtest.core.api import *


class APKSearchCase(AndroidAppCase):
    @classmethod
    def name(cls):
        return 'APKSearch (customized name)'

    @classmethod
    def getMetaInfo(cls):
        return {
            "author": 'baisong',
            "remark": '2018-08-21',
        }

    @classmethod
    def setUpClass(cls):
        super(APKSearchCase, cls).setUpClass()
        cls.package_name = 'com.sogou.androidtool'
        apk_path = cls.R('res/app/com.sogou.androidtool.apk')
        install_android_app(current_device().adb, apk_path)
        start_app(cls.package_name)

    @classmethod
    def tearDownClass(cls):
        stop_app(cls.package_name)
        super(APKSearchCase, cls).tearDownClass()

    def setUp(self):
        pass
        # clear previous result
        # clr = self.poco('com.google.android.calculator:id/clr')
        # if clr.exists():
        #     clr.click()


class SearchApp1(APKSearchCase):
    def runTest(self):
        accountPic = Template(self.R('res/img/apksearch/account.png'))
        self.assertTrue(exists(accountPic), 'App started.')

        self.poco("com.sogou.androidtool:id/search_prompt").click()
        text("斗地主")
        self.poco(text="天天斗地主（真人版）").click()
        time.sleep(1)
        result = self.poco('android.widget.TextView').get_text()

        self.assertEqual(result, '天天222斗地主（真人版）', '打开天天斗地主（真人版）详情页')
        print ("test")

class SearchApp2(APKSearchCase):
    def runTest(self):
        self.poco("com.sogou.androidtool:id/search_prompt").click()
        text("王者荣耀")
        time.sleep(1)
        self.poco("com.sogou.androidtool:id/result_list").child("android.widget.RelativeLayout")[0].child("com.sogou.androidtool:id/head").child("com.sogou.androidtool:id/app_name").click()
        result = self.poco('android.widget.TextView').get_text()
        time.sleep(1)
        self.assertEqual(result, '王者荣耀', '打开王者荣耀详情页')


if __name__ == '__main__':
    import pocounit
    pocounit.main()
