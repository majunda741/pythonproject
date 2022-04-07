import os

import re
# 获取所有正在连接手机的device
# 非实时获取


def get_deviceid():
    str_init = ' '
    all_info = os.popen('adb devices').readlines()
    for i in range(len(all_info)):
        str_init += all_info[i]
    devices_name = re.findall('\n(.+?)\t', str_init, re.S)
    # 正则表达式匹配device字段
    return devices_name
