import os
import threading
import datetime
import tkinter
import adbutils


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


class screenShot(threading.Thread):
    def __init__(self, device):
        # 需要device，信号，以及指令队列
        threading.Thread.__init__(self)
        self.device = device

    def run(self):
        device_n = adbutils.adb.device(serial=self.device)
        phmodle = device_n.shell("getprop ro.product.model", stream=True)
        for line in split_raw_to_lines1(phmodle):
            strmodle = line
            break
        demodle = str(strmodle, 'utf-8')
        demodle = demodle.replace(' ', '')
        dangqian = datetime.datetime.now()
        strzifu = str(dangqian)
        b = strzifu.replace(' ', '')
        b = b.replace('-', '')
        b = b.replace(':', '')
        Index = b.rfind(".")
        c = b[Index:]
        b = b.replace(c, "")
        isaaa = os.path.exists("./screenshot\\" + demodle)
        if not isaaa:
            os.mkdir("./screenshot\\" + demodle)
        os.system("adb -s " + self.device + " shell /system/bin/screencap -p /sdcard/" + b + ".png")
        os.system("adb -s " + self.device + " pull /sdcard/" + b + ".png ./screenshot/" + demodle + "/" + b + ".png")
        sucscree = tkinter.messagebox.showinfo('提示', demodle + '的截图已成功保存至screenshot目录下')