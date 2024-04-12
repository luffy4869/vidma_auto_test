# coding=utf-8
import uiautomator2 as u2
import calendar
import time
import unittest


class EditorCheckPageTestCase(unittest.TestCase):
    def setUp(self):
        self.d = u2.connect()
        self.d.app_start("vidma.video.editor.videomaker")
        self.d.implicitly_wait(10.0)

    def tearDown(self):
        self.d.app_stop("vidma.video.editor.videomaker")

    def get_screen_photo(self):
        time.sleep(3)
        ts = calendar.timegm(time.gmtime())
        photo_name = './photo/%s.png' % ts
        self.d.screenshot(photo_name)

    def test_editor_page(self):
        self.d(resourceId="vidma.video.editor.videomaker:id/ivAdd").click()
        self.d.xpath(
            '//*[@resource-id="vidma.video.editor.videomaker:id/rvList"]/android.view.ViewGroup[2]/android.widget.ImageView[1]').click()
        self.d(resourceId="vidma.video.editor.videomaker:id/tvNext").click()
        self.d(resourceId="vidma.video.editor.videomaker:id/tvBadge", text="Edit").click()
        self.d(resourceId="vidma.video.editor.videomaker:id/tvBadge", text="Filter").click()
        self.get_screen_photo()
        self.d(resourceId="vidma.video.editor.videomaker:id/iv_cancel").click()
        self.d(resourceId="vidma.video.editor.videomaker:id/tvBadge", text="Effect").click()
        self.get_screen_photo()
        self.d(resourceId="vidma.video.editor.videomaker:id/iv_cancel").click()
        self.d(resourceId="vidma.video.editor.videomaker:id/iv_confirm").click()
        self.d(resourceId="vidma.video.editor.videomaker:id/tvBadge", text="Edit").click()
        self.d(resourceId="vidma.video.editor.videomaker:id/tvBadge", text="Animation").click()
        self.get_screen_photo()
        self.d(resourceId="vidma.video.editor.videomaker:id/ivCancel").click()
        self.d.swipe_ext("left", box=(196, 2710, 1315, 2710))
        time.sleep(3)
        self.d(resourceId="vidma.video.editor.videomaker:id/tvBadge", text="Speed").click()
        time.sleep(3)
        self.d(description="Curve").click()
        self.get_screen_photo()
        self.d(resourceId="vidma.video.editor.videomaker:id/iv_cancel").click()
        self.d.swipe_ext("left", box=(196, 2710, 1315, 2710))
        time.sleep(3)
        self.d(resourceId="vidma.video.editor.videomaker:id/tvBadge", text="Background").click()
        self.get_screen_photo()
        self.d(resourceId="vidma.video.editor.videomaker:id/iv_cancel").click()
        self.d(resourceId="vidma.video.editor.videomaker:id/tvBadge", text="Voice Fx").click()
        self.get_screen_photo()
        self.d(resourceId="vidma.video.editor.videomaker:id/iv_cancel").click()
        self.d(resourceId="vidma.video.editor.videomaker:id/down").click()
        self.d(resourceId="vidma.video.editor.videomaker:id/tvBadge", text="Audio").click()
        self.d(resourceId="vidma.video.editor.videomaker:id/tvBadge", text="Music").click()
        self.get_screen_photo()
        self.d(resourceId="vidma.video.editor.videomaker:id/tvName", text="Romantic").click()
        self.get_screen_photo()
        self.d.xpath('//android.widget.ImageButton').click()
        self.d(resourceId="vidma.video.editor.videomaker:id/music_name", text="Strain").click()
        self.get_screen_photo()
        self.d(resourceId="vidma.video.editor.videomaker:id/ivClose").click()
        self.d(resourceId="vidma.video.editor.videomaker:id/tvBadge", text="Sound").click()
        self.get_screen_photo()
        self.d(resourceId="vidma.video.editor.videomaker:id/tvName", text="Christmas").click()
        self.get_screen_photo()
        self.d.xpath('//android.widget.ImageButton').click()
        self.d(resourceId="vidma.video.editor.videomaker:id/ivClose").click()
        self.d(resourceId="vidma.video.editor.videomaker:id/down").click()
        self.d(resourceId="vidma.video.editor.videomaker:id/tvBadge", text="Text").click()
        self.get_screen_photo()
        self.d(resourceId="vidma.video.editor.videomaker:id/animationImageView").click()
        self.get_screen_photo()
        self.d(resourceId="vidma.video.editor.videomaker:id/cancelImageView").click()
        self.d(resourceId="vidma.video.editor.videomaker:id/tvBadge", text="Sticker").click()
        self.get_screen_photo()
        self.d(resourceId="vidma.video.editor.videomaker:id/ivDone").click()
        self.d.swipe_ext("left", box=(200, 2260, 1100, 2260))
        time.sleep(3)
        self.d(resourceId="vidma.video.editor.videomaker:id/lfTransition").click()
        self.d(resourceId="vidma.video.editor.videomaker:id/ivPopupSplitMove").click()
        self.d(resourceId="vidma.video.editor.videomaker:id/down").click()
        self.d.xpath(
            '//*[@resource-id="vidma.video.editor.videomaker:id/lfTransition"]/android.widget.ImageView[1]').click()
        self.get_screen_photo()
        self.d(resourceId="vidma.video.editor.videomaker:id/iv_cancel").click()
        self.d(resourceId="vidma.video.editor.videomaker:id/ivBack").click()


if __name__ == '__main__':
    unittest.main()
