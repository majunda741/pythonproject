import threading
# 定义自己类的功能
import scrcpy
import getWandH


class phonerunThread(threading.Thread):
    def __init__(self, device_n, order_queue, event):
        threading.Thread.__init__(self)
        self.device_n = device_n
        self.device_n.start(threaded=True)
        # self.device_n.set_orientation('natural')
        self.order_queue = order_queue
        self._event = event

    # 　调用start自动执行的函数

    def run(self):
        slave_device_window_size = getWandH.get_raw_window_size(self.device_n)
        while True:
            if not self._event.is_set():
                break
            if not self.order_queue.empty():
                order = self.order_queue.get()
                # print(order)
                if order['action'] == 'move':
                    # self.device_n.touch.move(order['x'] * int(slave_device_window_size[0]),
                    #                          order['y'] * int(slave_device_window_size[1]))
                    self.device_n.control.touch(order['x'] * int(slave_device_window_size[0]),
                                                order['y'] * int(slave_device_window_size[1]), scrcpy.ACTION_MOVE)
                elif order['action'] == 'up':
                    # self.device_n.touch.up(order['x'] * int(slave_device_window_size[0]),
                    #                        order['y'] * int(slave_device_window_size[1]))
                    self.device_n.control.touch(order['x'] * int(slave_device_window_size[0]),
                                                order['y'] * int(slave_device_window_size[1]), scrcpy.ACTION_UP)
                elif order['action'] == 'down':
                    # self.device_n.touch.down(order['x'] * int(slave_device_window_size[0]),
                    #                          order['y'] * int(slave_device_window_size[1]))
                    self.device_n.control.touch(order['x'] * int(slave_device_window_size[0]),
                                                order['y'] * int(slave_device_window_size[1]), scrcpy.ACTION_DOWN)