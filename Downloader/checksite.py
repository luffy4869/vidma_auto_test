# coding=utf-8
import unittest
from time import sleep
import uiautomator2 as u2


def get_enter_text():
    file_path = './txt/website.txt'
    with open(file_path) as f:
        lines = f.readlines()
        text_list = [line.strip() for line in lines]
    return text_list


def get_third_index(word, sentence):
    word_index = [n for n in range(len(sentence)) if sentence.find(word, n) == n]
    return word_index[2]


t_list = get_enter_text()


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

    def enter_keyword(self, word):
        self.d(resourceId="free.video.downloader.converter.music:id/tvSearch").click()
        self.d.send_keys(word, clear=True)
        self.d.press("enter")
        sleep(15)
        popups_value = self.d(resourceId="free.video.downloader.converter.music:id/tvGotIt").exists
        if popups_value:
            self.d(resourceId="free.video.downloader.converter.music:id/tvGotIt").click()
        sleep(5)

    def test_check_url(self):
        unparse_urls = []
        for t in t_list:
            try:
                self.enter_keyword(t)
                ele1_value = self.d(resourceId="free.video.downloader.converter.music:id/normalLoadView").exists
                # ele2_value = self.d(resourceId="free.video.downloader.converter.music:id/completeLoadView").exists
                # ele3_text = self.d(resourceId="free.video.downloader.converter.music:id/debugInfo").get_text()
                if ele1_value:
                    unparse_urls.append(t)
            except Exception as e:
                print(f"an error occurred: {e}")
        with open("./txt/unparse_urls.txt", "w") as f1:
            [f1.write(f"{i1[:get_third_index('/', i1)]}\n") for i1 in unparse_urls]


if __name__ == '__main__':
    unittest.main()
