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
    trunk_size = 4
    tmp_info = b''
    while True:
        tmp_info += stream.read(trunk_size)
        while b'\n' in tmp_info:
            split_index = tmp_info.index(b'\n')
            yield tmp_info[:split_index]
            tmp_info = tmp_info[split_index + 1:]


def generate_order(device):
    width, height = getWandH.get_raw_window_size1(device)
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
            elif info[2] == 'ABS_MT_POSITION_Y':
                order['y'] = int(info[3], 16) / height
            elif info[2] == "SYN_REPORT":
                order['action_lock'] = False
                # if ready_ignore_times > 0 and order['action'] not in ['down', 'up']:
                #     # 产生信号频率过高，删选部分
                #     ready_ignore_times -= 1
                #     continue
                # ready_ignore_times = ignore_move_times
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
