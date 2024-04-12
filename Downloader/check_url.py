# coding=utf-8
import unittest
from time import sleep
import uiautomator2 as u2


def get_enter_keyword():
    keyword_list = []
    file_path = './txt/website.txt'
    with open(file_path) as f:
        lines = f.readlines()
        for line in lines:
            keyword_list.append(line.strip())
    return keyword_list


enter_list = get_enter_keyword()


class DownloaderTestCase(unittest.TestCase):
    d = None

    @classmethod
    def setUpClass(cls):
        cls.d = u2.connect()
        cls.d.app_start("free.video.downloader.converter.music")
        cls.d.implicitly_wait(10.0)

    @classmethod
    def tearDownClass(cls):
        cls.d.app_stop("free.video.downloader.converter.music")

    def get_screen_photo(self, model, word):
        sleep(10)
        if model == "normal":
            photo_name = './photo/normal/%s.png' % word
        elif model == "desktop":
            photo_name = './photo/desktop/%s.png' % word
        else:
            photo_name = './photo/private/%s.png' % word
        self.d.screenshot(photo_name)

    def click_setting_button(self):
        test_url = "www.google.com"
        self.d(resourceId="free.video.downloader.converter.music:id/tvSearch").click()
        self.d.send_keys(test_url, clear=True)
        self.d.press("enter")
        self.d(resourceId="free.video.downloader.converter.music:id/ivTopMore").click()

    def choice_model(self, model):
        match model:
            case "normal":
                pass
            case "desktop":
                self.click_setting_button()
                self.d(resourceId="free.video.downloader.converter.music:id/scDesktopStatus").click()
                self.d.press("back")
            case "private":
                self.click_setting_button()
                self.d(resourceId="free.video.downloader.converter.music:id/scDesktopStatus").click()
                self.d(resourceId="free.video.downloader.converter.music:id/privateBrowserSwitch").click()

    def enter_keyword(self, model, word):
        self.d(resourceId="free.video.downloader.converter.music:id/ivGoHome").click()
        self.d(resourceId="free.video.downloader.converter.music:id/tvSearch").click()
        word = f"https://{word}"
        self.d.send_keys(word, clear=True)
        self.d.press("enter")
        word = word[7:]
        self.get_screen_photo(model, word)

    def test_1_downloader_normal(self):
        self.choice_model("normal")
        [self.enter_keyword("normal", text) for text in enter_list]

    def test_2_downloader_desktop(self):
        self.choice_model("desktop")
        [self.enter_keyword("desktop", text) for text in enter_list]

    def test_downloader_private(self):
        self.choice_model("private")
        [self.enter_keyword("private", text) for text in enter_list]


if __name__ == '__main__':
    unittest.main()
