import os
import unittest
from appium import webdriver
from time import sleep

# Returns abs path relative to this file and not cwd
import setasdf

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class setting_tests(unittest.TestCase):
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

    def test_health(self):
        health = self.driver.find_element_by_id('com.qihoo.appstore:id/clean_animation')
        health.click()
        sleep(10)
        done = self.driver.find_element_by_id('com.qihoo.appstore:id/btn_finish')
        done.click()
        sleep(2)
        quit = self.driver.find_element_by_id('com.qihoo.appstore:id/btn_left')
        quit.click()
        sleep(2)
        clean = self.driver.find_element_by_id('com.qihoo.appstore:id/bodyview')
        clean.click()
        sleep(2)
        clean_back = self.driver.find_element_by_id('com.qihoo360.mobilesafe.clean:id/common_img_back')
        clean_back.click()
        clean_back.click()
        down = self.driver.find_element_by_id('com.qihoo.appstore:id/grid_icon')
        down.click()
        sleep(2)




if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(setting_tests)
    unittest.TextTestRunner(verbosity=2).run(suite)
