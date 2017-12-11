import os
import unittest
from appium import webdriver
from time import sleep

# Returns abs path relative to this file and not cwd
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
            'apps/com.tcpan.ltsj_2.1.2_12.apk'
        )
        desired_caps['appPackage'] = 'com.tcpan.ltsj'
        desired_caps['appActivity'] = 'com.tcpan.ltsj.ui.activity.SplashActivity'

        #desired_caps['unicodeKeyboard'] = True

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_add_contacts(self):
        sleep(2)
        el = self.driver.find_element_by_name("我的")
        el.click()
        sleep(2)
        el = self.driver.find_element_by_id('com.tcpan.ltsj:id/rel_avatar').click()
        el = self.driver.find_element_by_id('com.tcpan.ltsj:id/rel_nickname').click()
        el = self.driver.find_element_by_id('com.tcpan.ltsj:id/editContent').click()
        #el.send_keys("我的一天")
        self.driver.keyevent(4)
        sleep(2)
        self.driver.keyevent(4)
        #el = self.driver.find_element_by_id('com.tcpan.ltsj:id/btn_sure')
        #el.click()
        sleep(2)
        el = self.driver.find_element_by_id('com.tcpan.ltsj:id/rel_age').click()#click age
        sleep(2)
        el = self.driver.find_element_by_id('com.tcpan.ltsj:id/tv_select').click()
        sleep(2)
        el = self.driver.find_element_by_id('com.tcpan.ltsj:id/rel_sex').click()
        sleep(2)
        el = self.driver.find_element_by_id('com.tcpan.ltsj:id/btn_nan').click()
        sleep(2)
        el = self.driver.find_element_by_id('com.tcpan.ltsj:id/rel_sex_action').click()
        sleep(2)
        #el = self.driver.find_element_by_id('com.tcpan.ltsj:id/btn1').click()
        #sleep(2)
        #el = self.driver.find_element_by_id('com.tcpan.ltsj:id/yes').click()
        #sleep(2)
        #el = self.driver.find_element_by_id('com.tcpan.ltsj:id/rel_sign').click()
        #sleep(2)
        self.driver.keyevent(4)








if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
