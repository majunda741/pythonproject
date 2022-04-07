import os
import threading
import tkinter
import adbutils


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


class installpackage(threading.Thread):
    def __init__(self, device, fileroutename):
        # 需要device，信号，以及指令队列
        threading.Thread.__init__(self)
        self.device = device
        self.fileroutename = fileroutename

    def run(self):
        issucc = 0
        device_1 = adbutils.adb.device(serial=self.device)
        opmodle = device_1.shell("getprop ro.product.model", stream=True)
        # 获取机型
        for line in split_raw_to_lines1(opmodle):
            strmodle = line
            break
        strzifu = str(strmodle, 'utf-8')
        aaa = os.popen('adb -s ' + self.device + ' install ' + self.fileroutename)
        data = aaa.read()
        for line in data.split():
            if line == 'Success':
                issucc = 1
        if issucc == 1:
            success = tkinter.messagebox.showinfo('安装成功', strzifu + '\n已成功安装')
        else:
            nosuccess = tkinter.messagebox.showerror('安装失败', strzifu + '\n安装失败')
        aaa.close()