# coding=utf-8
import uiautomator2 as u2
from time import sleep

d = u2.connect()
d.app_start("vidma.mkv.xvideo.player.videoplayer.free")
sleep(5)
d.xpath('//*[@resource-id="vidma.mkv.xvideo.player.videoplayer.free:id/videoRV"]/android.view.ViewGroup[1]').click()
# while True:
#     sleep(2)
#     d(resourceId="vidma.mkv.xvideo.player.videoplayer.free:id/iv_seek_forward").click()
# sleep(2)
d(resourceId="vidma.mkv.xvideo.player.videoplayer.free:id/ivVMore").click()