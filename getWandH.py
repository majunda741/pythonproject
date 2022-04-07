# 获取手机长宽分辨率
import re


def get_raw_window_size(device):
    # 获取逻辑分辨率
    output = device.device.shell("wm size")
    o = re.search(r"Override size: (\d+)x(\d+)", output)
    m = re.search(r"Physical size: (\d+)x(\d+)", output)
    if m:
        if o:
            w, h = o.group(1), o.group(2)
            return int(w), int(h)
        else:
            w, h = m.group(1), m.group(2)
            return int(w), int(h)


def get_raw_window_size1(device):
    # 获取物理分辨率
    output = device.shell("wm size")
    o = re.search(r"Override size: (\d+)x(\d+)", output)
    m = re.search(r"Physical size: (\d+)x(\d+)", output)
    if m:
        w, h = m.group(1), m.group(2)
        return int(w), int(h)
    elif o:
        w, h = o.group(1), o.group(2)
        return int(w), int(h)
