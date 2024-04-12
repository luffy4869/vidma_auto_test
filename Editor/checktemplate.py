# coding=utf-8
import os
import time
from multiprocessing import Process
import uiautomator2 as u2


def get_devices_serials():
    devices_list = []
    fd = os.popen("adb devices")
    devices_list_src = fd.readlines()
    fd.close()
    for device in devices_list_src:
        if "device\n" in device:
            device = device.replace("\tdevice\n", "")
            devices_list.append(device)
    return devices_list


def test_template(serial):
    d = u2.connect(serial)
    print(d.info)
    d.app_start("vidma.video.editor.videomaker")
    d.implicitly_wait(10.0)
    d(resourceId="vidma.video.editor.videomaker:id/tvMore").click()
    d(resourceId="vidma.video.editor.videomaker:id/ivBack").click()
    d(resourceId="vidma.video.editor.videomaker:id/ivCover").click()
    while True:
        time.sleep(5)
        d.swipe_ext("up")


if __name__ == "__main__":
    process_list = []
    serial_list = get_devices_serials()
    for index in range(len(serial_list)):
        p = Process(target=test_template, args=(serial_list[index],))
        p.start()
        process_list.append(p)
    for p in process_list:
        p.join()
    print("all task done!")
