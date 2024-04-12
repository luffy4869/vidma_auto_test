# -*- coding: UTF-8 -*-
import os
from time import sleep
import unittest

import xmlrunner as xmlrunner
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By


class RecorderTest(unittest.TestCase):
    def setUp(self):
        print('handle driver set up .')
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '',  # match all platforms
            'deviceName': '<unknown>',
            'newCommandTimeout': 1000,
            'automationName': 'UiAutomator2',
            'appPackage': os.getenv("CT_APP_PKG_NAME"),
            'appWaitPackage': os.getenv("CT_APP_PKG_NAME"),
            'appActivity': os.getenv("CT_APP_LAUNCH_ACTIVITY"),
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    def tearDown(self):
        self.driver.quit()

    def click_element(self, *loc):
        try:
            WebDriverWait(self.driver, 5, 0.5).until(EC.visibility_of_element_located(loc))
            ele = self.driver.find_element(*loc)
        except (NoSuchElementException, TimeoutException):
            print("No This Element!")
        else:
            ele.click()

    def is_feature_exist(self, *loc):
        try:
            WebDriverWait(self.driver, 5, 0.5).until(EC.visibility_of_element_located(loc))
            self.driver.find_element(*loc)
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    @staticmethod
    def splice_xpath(cls, msg):
        s1 = "//android.widget."
        s2 = "[contains(@text,'"
        s3 = "')][1]"
        return f'{s1}{cls}{s2}{msg}{s3}'

    def click_allow(self):
        locale_command = "adb shell getprop persist.sys.locale"
        osLocale = os.popen(locale_command).read().strip()
        if "en" in osLocale:
            con1 = self.is_feature_exist(By.XPATH, self.splice_xpath("Button", "A"))
            if con1:
                self.click_element(By.XPATH, self.splice_xpath("Button", "A"))
            else:
                self.click_element(By.XPATH, self.splice_xpath("Button", "W"))
        else:
            con2 = self.is_feature_exist(By.XPATH, self.splice_xpath("Button", "允"))
            if con2:
                self.click_element(By.XPATH, self.splice_xpath("Button", "允"))
            else:
                self.click_element(By.XPATH, self.splice_xpath("Button", "时"))

    def is_photo_text_exist(self):
        locale_command = "adb shell getprop persist.sys.locale"
        osLocale = os.popen(locale_command).read().strip()
        if "en" in osLocale:
            term1 = self.is_feature_exist(By.XPATH, self.splice_xpath("TextView", "pictures"))
            term2 = self.is_feature_exist(By.XPATH, self.splice_xpath("TextView", "camera"))
            term = term1 or term2
        else:
            term3 = self.is_feature_exist(By.XPATH, self.splice_xpath("TextView", "照"))
            term4 = self.is_feature_exist(By.XPATH, self.splice_xpath("TextView", "相"))
            term = term3 or term4
        return term

    def record_flow(self):
        sleep(13)
        self.click_element(By.ID, "fabStop")
        sleep(3)
        self.click_element(By.ID, "ivClose")
        sleep(3)
        self.driver.keyevent(4)
        sleep(3)

    def start_flow1(self):
        sleep(3)
        self.click_element(By.ID, "tvOpenSettings")
        self.click_allow()
        self.click_element(By.ID, "fabControl")
        if self.is_photo_text_exist():
            self.click_allow()
            self.click_allow()
        else:
            self.click_allow()
        self.click_element(By.ID, "android:id/button1")
        self.record_flow()

    def start_flow2(self):
        sleep(3)
        self.click_element(By.ID, "fabControl")
        self.click_element(By.ID, "android:id/button1")
        self.record_flow()

    # your test cases start here
    def test_record_normal_flow(self):
        print('test record start .')
        # 首次录制
        self.click_element(By.ID, "btn_continue")
        if self.is_feature_exist(By.ID, "tvOpenSettings"):
            self.start_flow1()
        else:
            self.start_flow2()
        # 修改录音参数
        self.click_element(By.ID, "ivMic")
        self.click_element(By.ID, "ivMic")
        self.click_element(By.ID, "fabControl")
        self.record_flow()
        # 修改视频参数
        self.click_element(By.ID, "action_settings")
        sleep(3)
        self.driver.find_elements(By.ID, "android:id/title")[1].click()
        sleep(3)
        self.click_element(By.ID, "hd")
        sleep(3)
        self.driver.find_elements(By.ID, "ctResolution")[0].click()
        self.click_element(By.ID, "hq")
        sleep(3)
        self.driver.find_elements(By.ID, "ctResolution")[1].click()
        self.click_element(By.ID, "fps")
        sleep(3)
        self.driver.find_elements(By.ID, "ctResolution")[1].click()
        self.click_element(By.CLASS_NAME, "android.widget.ImageButton")
        self.click_element(By.CLASS_NAME, "android.widget.ImageButton")
        self.click_element(By.ID, "fabControl")
        self.record_flow()
        # 修改录制方向
        self.click_element(By.ID, "action_settings")
        sleep(3)
        self.driver.find_elements(By.ID, "android:id/title")[2].click()
        sleep(3)
        self.driver.find_elements(By.ID, "android:id/text1")[2].click()
        self.click_element(By.CLASS_NAME, "android.widget.ImageButton")
        self.click_element(By.ID, "fabControl")
        self.record_flow()
        print('test record end.')
    # your test cases end here


if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output=os.getenv("UPLOADDIR")))
