from multiprocessing import Queue
from copy import deepcopy
import adbutils
import scrcpy
import getDevices
import phonethreads
import phoneautoctr
import threading
# 主控机主进程代码


class majorcode(threading.Thread):
    def __init__(self, device1, event):
        # 存取device和控制信号
        threading.Thread.__init__(self)
        self.device1 = device1
        device_main = scrcpy.Client(device=device1, lock_screen_orientation=0)
        device_main.start(threaded=True)
        self._event = event
        self.device_list = {}

        # 　调用start自动执行的函数
    def getDevices(self):
        return self.device_list

    def run(self):
        alldevice = getDevices.get_deviceid()
        alldevicelen = len(alldevice)
        device_1 = adbutils.adb.device(serial=self.device1)  # connect to device
        slave_devices: list = []
        for j in range(0, alldevicelen):
            if alldevice[j] != self.device1:
                # 如果不是主控机器
                slave_devices.append(scrcpy.Client(device=alldevice[j], lock_screen_orientation=0))
        # 以下代码为多控代码
        order_queue = {

        }
        self.device_list = {}
        # a: int = 1
        # print(slave_devices)
        for k in slave_devices:
            # 逐一开启从控机的线程
            order_queue[k] = Queue()
            self.device_list[k] = phonethreads.phonerunThread(k, order_queue[k], self._event)
            self.device_list[k].start()

        for o in phoneautoctr.generate_order(device_1):
            if not self._event.is_set():
                break

            for k, v in order_queue.items():
                # 深拷贝出操作指令，然后put
                v.put(deepcopy(o))

