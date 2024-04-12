# coding=utf-8
import uiautomator2 as u2
from time import sleep


def click_fx():
    d = u2.connect()
    d.app_start("vidma.video.editor.videomaker")
    d.implicitly_wait(10.0)
    d(resourceId="vidma.video.editor.videomaker:id/flToolFx").click()
    d.xpath(
        '//*[@resource-id="vidma.video.editor.videomaker:id/rvList"]/android.view.ViewGroup[2]/android.widget.ImageView[1]').click()
    d(resourceId="vidma.video.editor.videomaker:id/tvNext").click()
    sleep(5)

    def find_fx():
        els = d(resourceId="vidma.video.editor.videomaker:id/ivVFXCover")
        for i in range(0, len(els)):
            els[i].click()
            sleep(3)
            if i == len(els) - 1:
                break

    def run_time(num, title):
        for x in range(num):
            if x < num:
                find_fx()
                sleep(3)
                d.swipe_ext("down", box=(300, 1600, 300, 750))
                sleep(3)
            else:
                find_fx()
        sleep(3)
        d(resourceId="vidma.video.editor.videomaker:id/tvTab", text=title).click()
        sleep(3)

    run_time(4, "Motion")
    run_time(4, "Mood")
    run_time(6, "Glitch")
    run_time(3, "Party")
    run_time(5, "Retro")
    run_time(6, "Love")


if __name__ == '__main__':
    click_fx()
