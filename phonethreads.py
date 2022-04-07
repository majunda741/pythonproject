import threading
# 从控手机根据读取到的指令进行操作
import scrcpy
import getWandH


class phonerunThread(threading.Thread):
    def __init__(self, device_n, order_queue, event):
        # 需要device，信号，以及指令队列
        threading.Thread.__init__(self)
        self.device_n = device_n
        self.device_n.start(threaded=True)
        # self.device_n.set_orientation('natural')
        self.order_queue = order_queue
        self._event = event

    def run(self):
        slave_device_window_size = getWandH.get_raw_window_size(self.device_n)
        while True:
            # 根据信号开始执行操作
            if not self._event.is_set():
                break
            if not self.order_queue.empty():
                order = self.order_queue.get()
                # print(order)
                if order['action'] == 'move':
                    self.device_n.control.touch(order['x'] * int(slave_device_window_size[0]),
                                                order['y'] * int(slave_device_window_size[1]), scrcpy.ACTION_MOVE)
                elif order['action'] == 'up':
                    self.device_n.control.touch(order['x'] * int(slave_device_window_size[0]),
                                                order['y'] * int(slave_device_window_size[1]), scrcpy.ACTION_UP)
                elif order['action'] == 'down':
                    self.device_n.control.touch(order['x'] * int(slave_device_window_size[0]),
                                                order['y'] * int(slave_device_window_size[1]), scrcpy.ACTION_DOWN)