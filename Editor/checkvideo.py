# coding=utf-8
# 此脚本用于检查文件夹视频是否正常
import os
import subprocess

paths = os.walk(r"/Users/wan/Downloads/Video/resolution/")
file_list = []
for dir_path, dir_names, file_names in paths:
    for file_name in file_names:
        file_list.append(os.path.join(dir_path, file_name))

file_list.remove("/Users/wan/Downloads/Video/resolution/.DS_Store")
a = 'ffmpeg -i '
command_list = [f'{a}{fl}' for fl in file_list]
file_list1 = []
for cl in command_list:
    result = subprocess.Popen(cl, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                              encoding='ISO-8859-1').communicate()[0]
    if 'moov' in result:
        file_list1.append(cl.split('-i')[1].strip())

print(file_list1)
