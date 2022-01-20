import os
import sys
import threading
import tkinter
import optimization.Phone as ph
import getDevices
import majorCode
from tkinter import ttk, DISABLED, NORMAL

if __name__ == '__main__':
    # 全局变量插入的设备，显示的设备名称，以及对应表
    event = threading.Event()
    event.set()
    tall = []
    tname = []
    ph1 = ph.Phone
    a = ph1.getExceldevice(ph1)

    # 定义GUI
    top = tkinter.Tk()
    # 进入消息循环
    top.title("一机多控")
    top.geometry('350x60')
    aLabel = ttk.Label(top, text="点击开始控制")
    aLabel.grid(column=0, row=0)
    t = majorCode.majorcode("", event)
    top.resizable(width=False, height=False)

    # 开始控制按钮
    def clickIn():
        action.configure(text="开始多控")
        aLabel.configure(text="正在控制..........")
        event.set()
        aaa = var.get()
        for i in range(len(tall)):
            if aaa == tall[i][0]:
                aaa = tall[i][1]
                break
        t = majorCode.majorcode(aaa, event)
        # t.run(aaa)
        t.start()
        action.configure(state=DISABLED)
        action1.configure(state=NORMAL)
        action2.configure(state=DISABLED)
    action = ttk.Button(top, text="开始多控", command=clickIn)
    action.grid(column=1, row=0)


    # 停止控制按钮
    def clickOut():
        action1.configure(text="停止多控")
        aLabel.configure(text="请选择主控机")
        event.clear()
        # os._exit(1)
        alldevice1 = getDevices.get_deviceid()
        if len(alldevice1) == 0:
            comb['value'] = "请插入至少2台连接设备"
            comb.current(0)
            action.configure(state=DISABLED)
            action1.configure(state=DISABLED)
        if len(alldevice1) == 1:
            comb['value'] = "请插入至少2台连接设备"
            comb.current(0)
            action.configure(state=DISABLED)
            action1.configure(state=DISABLED)
        if len(alldevice1) > 1:
            # 实时获取插入的设备
            tname.clear()
            tall.clear()
            for j in range(len(alldevice1)):
                tname.append(alldevice1[j])
                for i in range(len(a)):
                    if alldevice1[j] == a[i].device:
                        tname[j] = a[i].name
                        tall.append([a[i].name, a[i].device])
            comb['value'] = tname
            comb.current(0)
            action.configure(state=NORMAL)
            action1.configure(state=DISABLED)
            action2.configure(state=NORMAL)
    action1 = ttk.Button(top, text="停止多控", command=clickOut)
    action1.configure(state=DISABLED)
    action1.grid(column=2, row=0)


    # 刷新按钮
    def Refresh():
        action2.configure(text="刷新设备")
        alldevice1 = getDevices.get_deviceid()
        if len(alldevice1) == 0:
            comb['value'] = "请插入至少2台连接设备"
            comb.current(0)
            action.configure(state=DISABLED)
            action1.configure(state=DISABLED)
        if len(alldevice1) == 1:
            comb['value'] = "请插入至少2台连接设备"
            comb.current(0)
            action.configure(state=DISABLED)
            action1.configure(state=DISABLED)
        if len(alldevice1) > 1:
            # 实时获取插入的设备
            tname.clear()
            tall.clear()
            for j in range(len(alldevice1)):
                tname.append(alldevice1[j])
                for i in range(len(a)):
                    if alldevice1[j] == a[i].device:
                        tname[j] = a[i].name
                        tall.append([a[i].name, a[i].device])
            comb['value'] = tname
            comb.current(0)
            action.configure(state=NORMAL)
            action1.configure(state=DISABLED)


    action2 = ttk.Button(top, text="刷新设备", command=Refresh)
    action2.grid(column=3, row=0)

    # 文字提示
    aLabel = ttk.Label(top, text="请选择主控机")
    aLabel.place(relx=0, rely=0.5)

    # 多选框
    var = tkinter.StringVar()
    alldevice = getDevices.get_deviceid()
    comb = ttk.Combobox(top, textvariable=var)
    if len(alldevice) == 0:
        comb['value'] = "请插入至少2台连接设备"
        action.configure(state=DISABLED)
        action1.configure(state=DISABLED)
    if len(alldevice) == 1:
        comb['value'] = "请插入至少2台连接设备"
        action.configure(state=DISABLED)
        action1.configure(state=DISABLED)
    if len(alldevice) > 1:
        # 翻译device显示机型
        tname.clear()
        # for i in range(len(a)):
        #     for j in range(len(alldevice)):
        #         tname.append(alldevice[j])
        #         if alldevice[j] == a[i].device:
        #             tname[j] = a[i].name
        #             tall.append([a[i].name,a[i].device])
        for j in range(len(alldevice)):
            tname.append(alldevice[j])
            for i in range(len(a)):
                if alldevice[j]==a[i].device:
                    tname[j] = a[i].name
                    tall.append([a[i].name, a[i].device])
        comb['value'] = tname
    comb.current(0)
    comb.place(relx=0.22, rely=0.5, relwidth=0.5)
    top.protocol('WM_DELETE_WINDOW', top.destroy)
    top.mainloop()
