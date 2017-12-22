import os
import unittest
from appium import webdriver
from time import sleep

# Returns abs path relative to this file and not cwd
import setasdf

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class ContactsAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = PATH(
            'apps/com.qihoo.appstore_300070142.apk'
        )
        desired_caps['appPackage'] = 'com.qihoo.appstore'
        desired_caps['appActivity'] = 'com.qihoo.appstore.home.LauncherActivity'
        #desired_caps.setCapability("noReset", true)
        #把输入法关掉
        desired_caps['unicodeKeyboard'] = True
        desired_caps['noReset'] = True

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()


    def test_add_contacts(self):
        sleep(5)
        try:
            male = self.driver.find_element_by_id('com.qihoo.appstore:id/btn_sel_male_icon')
            male.click()
            sleep(2)
            age = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout[4]/android.widget.TextView')
            age.click()
            sleep(2)
            next = self.driver.find_element_by_id('com.qihoo.appstore:id/set_btn')
            next.click()
            sleep(2)
            guangzhu = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.GridView/android.widget.FrameLayout[2]/android.widget.TextView')
            guangzhu.click()
            sleep(2)
            liji = self.driver.find_element_by_id('com.qihoo.appstore:id/set_btn')
            liji.click()
            sleep(2)
        except:
            print('获取跳过页面失败')
            sleep(3)
            pass
    def test_asd(self):
        sleep(5)
        seach = self.driver.find_element_by_id('com.qihoo.appstore:id/search_hint_view')
        seach.click()
        seach2 = self.driver.find_element_by_id('com.qihoo360.mobilesafe.recommend:id/qc')
        seach2.click()
        seach2.send_keys('荒野行动')
        sleep(8)

        back = self.driver.find_element_by_id('com.qihoo360.mobilesafe.recommend:id/b7')
        back.click()
        sleep(2)
        health = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ListView/android.widget.LinearLayout[5]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.Button[2]')
        health.click()
        sleep(2)

        #手机清理的简单测试
        clean = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout[4]/android.widget.GridView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout')
        clean.click()
        sleep(2)

        sleep(10)
        laji = self.driver.find_element_by_id('com.qihoo360.mobilesafe.clean:id/common_btn_middle')
        laji.click()
        wc = self.driver.find_element_by_id('com.qihoo.appstore:id/bottom_btn')
        wc.click()
        sleep(2)
        laji_back = self.driver.find_element_by_id('com.qihoo.appstore:id/btn_left')
        laji_back.click()
        sleep(1)
            

        clean_back = self.driver.find_element_by_id('com.qihoo360.mobilesafe.clean:id/common_img_back')
        clean_back.click()
        #clean_back.click()
        sleep(3)

        #下载管理测试

        down_ctrl = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout[4]/android.widget.GridView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout')
        down_ctrl.click()
        sleep(2)
        self.driver.get_screenshot_as_file('down_picture.jpg')
        down_back = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ImageView')
        down_back.click()
        sleep(2)















        












if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
