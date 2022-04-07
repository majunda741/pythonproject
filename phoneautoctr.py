import getWandH
import mainctrl
# 读主控手机操作，优化后的以SYN为节点读取操作
action_mapping = {
    "BTN_TOUCH": {
        "DOWN": "down",
        "UP": "up"
    },
    "ABS_MT_PRESSURE": "move",
}

args_mapping = {
    "ABS_MT_POSITION_X": "x",
    "ABS_MT_POSITION_Y": "y",
    "ABS_MT_TRACKING_ID": "pointer",
    "SYN_REPORT": "end"
}


def split_raw_to_lines(stream):
    # 读取stream
    trunk_size = 4
    tmp_info = b''
    while True:
        tmp_info += stream.read(trunk_size)
        while b'\n' in tmp_info:
            split_index = tmp_info.index(b'\n')
            yield tmp_info[:split_index]
            tmp_info = tmp_info[split_index + 1:]


def split_raw_to_lines1(stream):
    # 读取stream，这里只为了读取手机的型号，用来匹配表判断是否适配
    trunk_size = 4
    tmp_info = b''
    while True:
        tmp_info += stream.read(trunk_size)
        if b'\r' in tmp_info:
            while b'\r' in tmp_info:
                split_index = tmp_info.index(b'\r')
                yield tmp_info[:split_index]
                tmp_info = tmp_info[split_index + 1:]
        else:
            while b'\n' in tmp_info:
                split_index = tmp_info.index(b'\n')
                yield tmp_info[:split_index]
                tmp_info = tmp_info[split_index + 1:]


def generate_order(device):
    width, height = getWandH.get_raw_window_size1(device)
    opmodle = device.shell("getprop ro.product.model", stream=True)
    # 获取机型
    for line in split_raw_to_lines1(opmodle):
        strmodle = line
        break
    strzifu = str(strmodle,'utf-8')
    if strzifu == "OPPO A37m":
        # 单独适配OPPO a37m这台设备
        width = 1100
        height = 1800
    op = device.shell("getevent -l", stream=True)
    order = {
        "action": None,
        "x": 0,
        "y": 0,
        "pointer": None,
        "action_lock": False
    }
    # ready_ignore_times = ignore_move_times
    for line in split_raw_to_lines(op):
        # print(line)
        info = line.decode().split()
        # start_time = time.time()
        if len(info) != 4:
            continue
        if info[2] in args_mapping.keys():
            if info[2] == 'ABS_MT_POSITION_X':
                order['x'] = int(info[3], 16) / width
                if strzifu == "M2012K11AC":
                    # 单独适配红米k40
                    order['x'] = (int(info[3], 16) / width)/8
            elif info[2] == 'ABS_MT_POSITION_Y':
                order['y'] = int(info[3], 16) / height
                if strzifu == "M2012K11AC":
                    # 单独适配红米k40
                    order['y'] = (int(info[3], 16) / height)/8
            elif info[2] == "SYN_REPORT":
                order['action_lock'] = False
                yield order
                order['action'] = 'move'
        elif info[2] in action_mapping.keys():
            if info[2] == "BTN_TOUCH":
                # 判断是按下还是抬起
                order['action_lock'] = True
                order['action'] = action_mapping[info[2]][info[3]]
                if order['action'] == 'up':
                    yield order
            else:
                if not order['action_lock']:
                    order['action'] = action_mapping[info[2]]
