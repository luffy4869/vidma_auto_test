# coding=utf-8
import uiautomator2 as u2
from time import sleep

d = u2.connect()
d.app_start("vidma.video.editor.videomaker")
d.implicitly_wait(10.0)
d(resourceId="vidma.video.editor.videomaker:id/clMusic").click()
d.xpath(
    '//*[@resource-id="vidma.video.editor.videomaker:id/rvList"]/android.view.ViewGroup[2]/android.widget.ImageView[1]').click()
d(resourceId="vidma.video.editor.videomaker:id/ivNext").click()
sleep(5)

play_error_list = []
# 音乐分类
category_list = ["Free", "Romantic", "Vlog", "Birthday", "Hip Hop", "Game", "Fun", "Happy", "Electronic", "Acoustic",
                 "Pop", "Fitness", "Tech", "Travel", "Spooky", "Chill", "Rock", "Ambient", "Dramatic", "Lifestyle",
                 "Intense", "Sports", "Business", "Groovy", "Cinematic", "Melancholic", "Speed Up", "Food", "Energetic",
                 "Inspiring", "Documentary"]


def click_music_category(category_name):
    ele_category = d(resourceId="vidma.video.editor.videomaker:id/tvName", text=category_name)
    # 分类名存在就直接点击，不存在则向上滑动到出现然后点击
    if ele_category.exists:
        ele_category.click()
    else:
        while not ele_category.exists:
            d.swipe_ext("up")
        ele_category.click()
    sleep(3)
    ele_music_name = d(resourceId="vidma.video.editor.videomaker:id/music_name")
    # 点击第一首音乐
    ele_music_name[0].click()
    sleep(5)
    # 播放栏的音乐名
    ele_music_name_current = d(resourceId="vidma.video.editor.videomaker:id/name")
    current_music_name = ele_music_name_current.get_text()

    # 如果出现toast就把当前音乐名存到列表
    def add_play_list():
        if d.toast.show("Oops!"):
            play_error_list.append(current_music_name)

    add_play_list()
    title = d(resourceId="vidma.video.editor.videomaker:id/tvName")
    # 滑动到最后一首音乐
    while not title.exists:
        d.swipe_ext("up")
    # 存储最后一首音乐名
    last_music_name = ele_music_name[len(ele_music_name) - 1].get_text()
    # 如果当前音乐名不等于最后一首音乐名就一直点击下一首
    while current_music_name != last_music_name:
        d(resourceId="vidma.video.editor.videomaker:id/ivNext").click()
        sleep(5)
        add_play_list()
    # 点击返回按钮
    d.xpath('//android.widget.ImageButton').click()


# 循环遍历所有音乐分类
for i in category_list:
    click_music_category(i)
print(play_error_list)
