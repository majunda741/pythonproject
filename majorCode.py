from multiprocessing import Queue
from copy import deepcopy
import adbutils
import scrcpy
import getDevices
import phonethreads
import phoneautoctr
import threading
# 选择主控机器测试


class majorcode(threading.Thread):
    # 先遍历连接的手机在一一connect
    # def __init__(self, onoroff):
    #     threading.Thread.__init__(self)
    #     self.onoroff = onoroff

    def __init__(self, device1, event):
        threading.Thread.__init__(self)
        self.device1 = device1
        self._event = event

    def run(self):
        alldevice = getDevices.get_deviceid()
        alldevicelen = len(alldevice)
        device_1 = adbutils.adb.device(serial=self.device1)  # connect to device
        # device_1 = scrcpy.Client(device=alldevice[0])
        slave_devices: list = []
        print(self.device1 +"/t"+"sucsess---------------------------------------------"+"主控机")
        for j in range(0, alldevicelen):
            if alldevice[j] != self.device1:
                # 如果不是主控机器
                print(alldevice[j] +"/t"+"sucsess---------------------------------------------从控机")
                slave_devices.append(scrcpy.Client(device=alldevice[j], lock_screen_orientation=0))
        # 以下代码为多控代码
        order_queue = {

        }
        t = {}
        # a: int = 1
        # print(slave_devices)
        for k in slave_devices:
            order_queue[k] = Queue()
            t[k] = phonethreads.phonerunThread(k, order_queue[k], self._event)
            t[k].start()

        for o in phoneautoctr.generate_order(device_1):
            if not self._event.is_set():
                break
            # if self.onoroff == 0:
            #     for k in slave_devices:
            #         order_queue[k] = Queue()
            #         t[k] = phonethreads.phonerunThread(k, order_queue[k])
            #         t[k].join()
            #     break
            # print(o)
            for k, v in order_queue.items() :
                v.put(deepcopy(o))
                # if self.onoroff == 0:
                #     for k in slave_devices:
                #         order_queue[k] = Queue()
                #         t[k] = phonethreads.phonerunThread(k, order_queue[k])
                #         t[k].join()
                #     break
                # print("put ", k, o)

