import os

import re
# 获取所有正在连接手机的device


def get_deviceid():
    str_init = ' '
    all_info = os.popen('adb devices').readlines()
    # print('adb devices 输出的内容是：', all_info)

    for i in range(len(all_info)):
        str_init += all_info[i]
    devices_name = re.findall('\n(.+?)\t', str_init, re.S)

    # print('所有设备名称：\n', devices_name)
    # print(1)
    return devices_name

if __name__ == '__main__':
    print(get_deviceid())
# a = get_deviceid()
# b = len(a)
# for j in range(b):
#     print(a[j])