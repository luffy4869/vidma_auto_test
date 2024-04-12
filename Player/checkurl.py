# coding=utf-8
import unittest
import calendar
import time
import uiautomator2 as u2


def get_video_url():
    video_url_list = []
    file_path = './txt/videourl.txt'
    with open(file_path) as f:
        lines = f.readlines()
        for line in lines:
            video_url_list.append(line.strip())
    return video_url_list


link_list = get_video_url()


class PlayerTestCase(unittest.TestCase):
    def setUp(self):
        self.d = u2.connect()
        self.d.app_start("com.atlasv.android.vidmaplayer")
        self.d.implicitly_wait(10.0)

    def tearDown(self):
        self.d.app_stop("com.atlasv.android.vidmaplayer")

    def get_screen_photo(self):
        time.sleep(3)
        ts = calendar.timegm(time.gmtime())
        photo_name = './photo/%s.png' % ts
        self.d.screenshot(photo_name)

    def enter_video_link(self, link):
        self.d(resourceId="com.atlasv.android.vidmaplayer:id/tv_edit").click()
        self.d.send_keys(link, clear=True)
        self.d(resourceId="com.atlasv.android.vidmaplayer:id/play").click()
        self.get_screen_photo()
        self.d(resourceId="com.atlasv.android.vidmaplayer:id/iv_play_btn").click()
        self.get_screen_photo()
        self.d(resourceId="com.atlasv.android.vidmaplayer:id/iv_play_btn").click()
        self.d.press("back")

    def test_player(self):
        self.d(resourceId="com.atlasv.android.vidmaplayer:id/online").click()
        [self.enter_video_link(text) for text in link_list]


if __name__ == '__main__':
    unittest.main()
