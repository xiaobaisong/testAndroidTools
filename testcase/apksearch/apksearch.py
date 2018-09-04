# coding=utf-8

# TODO: "from testflow.lib" should be renamed according to your actual package name
from lib.case.android_app import AndroidAppCase
from pocounit.suite import PocoTestSuite
from lib.utils.installation import install_android_app
from airtest.core.api import device as current_device
from airtest.core.api import *


class APKSearchCaseSuite(PocoTestSuite):
    def setUp(self):
        if not current_device():
            connect_device('Android:///')
        apk_path = self.R('res/app/com.sogou.androidtool.apk')
        install_android_app(current_device().adb, apk_path)


class APKSearchCase(AndroidAppCase):
    def setUp(self):
        self.package_name = 'com.sogou.androidtool'
        start_app(self.package_name)
        accountPic = Template(self.R('res/img/apksearch/account.png'))
        if exists(accountPic):
            print('App started.')

    def tearDown(self):
        stop_app('com.sogou.androidtool')
        # pass


class SearchApp1(APKSearchCase):
    def runTest(self):
        self.poco("com.sogou.androidtool:id/search_prompt").click()
        text("斗地主")
        # self.poco("android:id/content").child("android.widget.RelativeLayout")[1].child("com.sogou.androidtool:id/key_suggestion_list").child("android.widget.RelativeLayout")[0].click()
        # time.sleep(1)
        self.poco(text="天天斗地主（真人版）").click()
        result = self.poco('android.widget.TextView').get_text()
        self.assertEqual(result, '天天斗地主（真人版）', '打开天天斗地主（真人版）详情页')


class SearchApp2(APKSearchCase):
    def runTest(self):
        self.poco("com.sogou.androidtool:id/search_prompt").click()
        text("王者荣耀")
        self.poco(text="王者荣耀").click()
        self.poco("com.sogou.androidtool:id/result_list").child("android.widget.RelativeLayout")[0].click()
        result = self.poco('android.widget.TextView').get_text()
        self.assertEqual(result, '王者荣耀', '打开王者荣耀详情页')


if __name__ == '__main__':
    suite = APKSearchCaseSuite([
        SearchApp1(),
        # SearchApp2(),
    ])
    import pocounit
    pocounit.run(suite)
