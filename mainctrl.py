import os
import threading
import tkinter
import scrcpy
import re
import getWandH
import optimization.Phone as ph
import getDevices
import majorCode
from tkinter import ttk, DISABLED, NORMAL
import tkinter.messagebox
from tkinter import filedialog
from optimization import installpac, screenshot


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


if __name__ == '__main__':
    # 全局变量插入的设备，显示的设备名称，以及对应表
    alldevice = getDevices.get_deviceid()
    event = threading.Event()
    event.set()
    tall = []
    heibian = []
    tname = []
    tjudged = []
    # 获取一些手机的信息
    ph1 = ph.Phone
    a = ph1.getExceldevice(ph1)
    # 定义GUI
    top = tkinter.Tk()
    # 进入消息循环
    top.title("一机多控")
    top.geometry('360x90')
    aLabel = ttk.Label(top, text="点击开始控制")
    aLabel.place(relx=0, rely=0)
    t = None
    top.resizable(width=False, height=False)

    # 开始控制按钮
    def clickIn():
        heibian.clear()
        panduanshifcunzai = False
        # 标识
        zhupanduan = 3
        tjudged.clear()
        alldevicein = getDevices.get_deviceid()
        alldevice = alldevicein
        action.configure(text="开始多控")
        # 判断是否支持多控
        for j in range(len(alldevicein)):
            tname.append(alldevicein[j])
            for i in range(len(a)):
                if alldevicein[j] == a[i].device:
                    tjudged.append([a[i].name,a[i].device, a[i].judge])
        for c in range(len(tjudged)):
            if tjudged[c][2] == 0:
                acheck = tkinter.messagebox.showerror('提示', tjudged[c][0]+'该设备不支持多控,请拔出该设备')
                return acheck
            if tjudged[c][2] == 2:
                achecktis = tkinter.messagebox.askokcancel('提示', tjudged[c][0] + '该设备不支持从控，可为主控')
        event.set()
        aaa = var.get()
        feidevice = 1
        # 判断选择的主控机是否为连接状态
        for jjj in range(len(alldevicein)):
            if aaa == alldevicein[jjj]:
                panduanshifcunzai = True
        if not panduanshifcunzai:
            for i in range(len(tall)):
                if aaa == tall[i][0]:
                    bbb = aaa
                    aaa = tall[i][1]
                    zhupanduan = tall[i][2]
                    feidevice = 0
                    break
        for ggg in range(len(alldevicein)):
            if aaa == alldevicein[ggg]:
                panduanshifcunzai = True
        # 判断高宽比给予相应提示
        if panduanshifcunzai:
            if zhupanduan == 1:
                acheckt = tkinter.messagebox.showerror('提示', bbb + '该设备不支持主控,请选择其他设备主控')
                return acheckt
            device = scrcpy.Client(device=aaa)
            width, height = getWandH.get_raw_window_size(device)
            gaokuanbi = height / width
            linshikuang = 'Ture'
            for ll in range(len(tjudged)):
                devicelinshi = scrcpy.Client(device=tjudged[ll][1])
                width1, height1 = getWandH.get_raw_window_size(devicelinshi)
                gaokuanlinshi = height1 / width1
                linshisuanshu = abs(gaokuanbi - gaokuanlinshi)
                if linshisuanshu > 0.25:
                    linshikuang = tkinter.messagebox.askokcancel('提示', tjudged[ll][0] + '与主控机屏幕比例存在较大偏差，不建议多控，是否继续多控？')
                elif linshisuanshu > 0.15:
                    linshikuang = tkinter.messagebox.askokcancel('提示', tjudged[ll][0] + '与主控机屏幕比例存在偏差，是否继续多控？')
                devicelinshi.stop()
            device.stop()
            if linshikuang:
                global t
                # 读取黑边设备的刘海高度
                for lv2 in range(len(alldevicein)):
                    linshipanudanhei = 0
                    if alldevicein[lv2] != aaa:
                        for lv1 in range(len(tall)):
                            if  alldevicein[lv2] == tall[lv1][1]:
                                lianshitall = tall[lv1]
                                linshipanudanhei = 1
                        if linshipanudanhei == 1:
                            heibian.append(lianshitall)
                        elif linshipanudanhei == 0:
                            heibian.append(["未知", alldevicein[lv2], 3, 0])
                # test
                print(heibian)

                # test
                # 开始执行多控
                t = majorCode.majorcode(aaa, event)
                t.start()
                if feidevice == 0:
                    acheckcg = tkinter.messagebox.showinfo('提示', tall[i][0] + '正在作为主控机进行控制')
                else:
                    acheckcg = tkinter.messagebox.showinfo('提示', aaa + '正在作为主控机进行控制')
                aLabel.configure(text="正在控制..........")
                action.configure(state=DISABLED)
                action1.configure(state=NORMAL)
                action2.configure(state=DISABLED)
                action4.configure(state=NORMAL)
                comb.configure(state=DISABLED)
            else:
                return False
        else:
            achecktcuowu = tkinter.messagebox.showerror('提示', '您选择的主控机未连接，请重新插入并刷新！！！')
            return achecktcuowu

    action = ttk.Button(top, text="开始多控", command=clickIn)
    action.place(relx=0.25, rely=0)

    # 停止控制按钮
    def clickOut():
        heibian.clear()
        comb.configure(state=NORMAL)
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
                        tall.append([a[i].name, a[i].device, a[i].judge, a[i].Bangshight])
            comb['value'] = tname
            comb.current(0)
            achecktz = tkinter.messagebox.showinfo('提示','停止控制')
            action.configure(state=NORMAL)
            action1.configure(state=DISABLED)
            action2.configure(state=NORMAL)
            action4.configure(state=DISABLED)
    action1 = ttk.Button(top, text="停止多控", command=clickOut)
    action1.configure(state=DISABLED)
    action1.place(relx=0.5, rely=0)

    # 刷新按钮
    def Refresh():
        action2.configure(text="刷新设备")
        alldevice = getDevices.get_deviceid()
        if len(alldevice) == 0:
            comb['value'] = "请插入至少2台连接设备"
            comb.current(0)
            action.configure(state=DISABLED)
            action1.configure(state=DISABLED)
        if len(alldevice) == 1:
            tname.clear()
            tall.clear()
            comb['value'] = "请插入至少2台连接设备"
            comb.current(0)
            action.configure(state=DISABLED)
            action1.configure(state=DISABLED)
            for j in range(len(alldevice)):
                tname.append(alldevice[j])
                for i in range(len(a)):
                    if alldevice[j] == a[i].device:
                        tname[j] = a[i].name
                        tall.append([a[i].name, a[i].device, a[i].judge, a[i].Bangshight])
        if len(alldevice) > 1:
            # 实时获取插入的设备
            tname.clear()
            tall.clear()
            for j in range(len(alldevice)):
                tname.append(alldevice[j])
                for i in range(len(a)):
                    if alldevice[j] == a[i].device:
                        tname[j] = a[i].name
                        tall.append([a[i].name, a[i].device, a[i].judge, a[i].Bangshight])
            comb['value'] = tname
            comb.current(0)
            action.configure(state=NORMAL)
            action1.configure(state=DISABLED)


    action2 = ttk.Button(top, text="刷新设备", command=Refresh)
    action2.place(relx=0.75, rely=0)

    # 截图
    def screen():
        screens = {}
        screens.clear()
        for devicescreen in range(len(alldevice)):
            screens[devicescreen] = screenshot.screenShot(alldevice[devicescreen])
            screens[devicescreen].start()


    action4 = ttk.Button(top, text="一键截图所有", command=screen)
    action4.place(relx=0.73, rely=0.33)
    action4.configure(state=DISABLED)
    # 文字提示

    aLabel = ttk.Label(top, text="请选择主控机")
    aLabel.place(relx=0, rely=0.35)

    # 多选框
    var = tkinter.StringVar()
    comb = ttk.Combobox(top, textvariable=var)
    if len(alldevice) == 0:
        comb['value'] = "请插入至少2台连接设备"
        action.configure(state=DISABLED)
        action1.configure(state=DISABLED)
    if len(alldevice) == 1:
        tname.clear()
        tall.clear()
        comb['value'] = "请插入至少2台连接设备"
        action.configure(state=DISABLED)
        action1.configure(state=DISABLED)
        for j in range(len(alldevice)):
            tname.append(alldevice[j])
            for i in range(len(a)):
                if alldevice[j]==a[i].device:
                    tname[j] = a[i].name
                    tall.append([a[i].name, a[i].device, a[i].judge, a[i].Bangshight])
    if len(alldevice) > 1:
        # 翻译device显示机型
        tname.clear()
        for j in range(len(alldevice)):
            tname.append(alldevice[j])
            for i in range(len(a)):
                if alldevice[j]==a[i].device:
                    tname[j] = a[i].name
                    tall.append([a[i].name, a[i].device,a[i].judge, a[i].Bangshight])
        comb['value'] = tname
    comb.current(0)
    comb.place(relx=0.22, rely=0.35, relwidth=0.5)
    # 装包

    def install():
        # 获取包的路径
        tname.clear()
        tall.clear()
        alldevice = getDevices.get_deviceid()
        for j in range(len(alldevice)):
            tname.append(alldevice[j])
            for i in range(len(a)):
                if alldevice[j] == a[i].device:
                    tname[j] = a[i].name
                    tall.append([a[i].name, a[i].device, a[i].judge])
        fileroute = filedialog.askopenfilename()
        isapk = re.search('.apk', fileroute)
        if isapk is not None:
            if len(alldevice) < 1:
                filerouteff = tkinter.messagebox.showerror('提示', '无手机连接')
            if len(alldevice) == 1:
                os.popen('adb install ' + fileroute)
                fileroutet1 = tkinter.messagebox.showinfo('提示', '以下设备正在装包\n' + tname[0])
            if len(alldevice) > 1:
                inpac = {}
                for ll in range(len(tall)):
                    inpac[ll] = installpac.installpackage(alldevice[ll], fileroute)
                    inpac[ll].start()
                fileroutet = tkinter.messagebox.showinfo('提示', '以下设备正在装包\n' + str(tname) + "请耐心等待提示")
        else:
            fileroutef = tkinter.messagebox.showerror('提示', '请选择apk文件')
    action5 = ttk.Button(top, text="一键装包", command=install)
    action5.place(relx=0.25, rely=0.63)
    top.protocol('WM_DELETE_WINDOW', top.destroy)

    #选择需要适配的机型

    top.mainloop()
