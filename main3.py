# from majorCode import majorcode
# import scrcpy
#
# if __name__ == '__main__':
#     d = scrcpy.Client(device="5714a99c")
#     print()
#     d.start(threaded=True)
#     d.control.swipe(800, 100, 0.1, 100)
#     # d.control.touch(500, 500, 0, 0)
#     # d.control.touch(550, 550, 2, 0)
#     # d.control.touch(800, 1000, 2, 0)
#     # d.control.touch(700, 1000, 2, 0)
#     # d.control.touch(600, 1000, 2, 1)
#     # d.control.touch(500, 1000, 2, 1)
#     # d.control.touch(400, 1000, 2, 1)
#     # d.control.touch(300, 1000, 2, 1)
#     # d.control.touch(200, 1000, 2, 1)
#     # d.control.touch(100, 1000, 2, 1)
#     # d.control.touch(100, 900, 2, 1)
#     # d.control.touch(100, 800, 2, 1)
#     # d.control.touch(100, 700, 2, 1)
#     # d.control.touch(100, 600, 2, 1)
#     # d.control.touch(100, 500, 2, 1)
#     # d.control.touch(100, 400, 2, 1)
#     # d.control.touch(100, 300, 2, 1)
#     # d.control.touch(100, 200, 2, 1)
#     # d.control.touch(100, 100, 1, 1)
#     d.stop()
#
# import tkinter
# import tkinter.messagebox
# def but():
#     a=tkinter.messagebox.askokcancel('提示', '要执行此操作吗')
#     print (a)
# root=tkinter.Tk()
# root.title('GUI')#标题
# root.geometry('800x600')#窗体大小
# root.resizable(False, False)#固定窗体
# tkinter.Button(root, text='hello button',command=but).pack()
# root.mainloop()
import os
from datetime import datetime

# import cv2.cv2
# import scrcpy
# from PIL import Image
#
#
# def frame_handler(res):
#     if res is not None:
#         ndarray_convert_img = Image.fromarray(cv2.cvtColor(res, cv2.COLOR_BGR2RGB))
#         print(ndarray_convert_img)
#         # ndarray_convert_img.save(f"./{datetime.now().timestamp()}.png")
#         ndarray_convert_img.show()
#
# d = scrcpy.Client(device="D121156105B1")
# d.add_listener("frame", frame_handler)
# d.start()


# import subprocess
#
#
# class Screenshot():  # 截取手机屏幕并保存到电脑
#     def __init__(self):
#         # 查看连接的手机
#         connect = subprocess.Popen("adb devices", stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
#         stdout, stderr = connect.communicate()  # 获取返回命令
#         # 输出执行命令结果结果
#         stdout = stdout.decode("utf-8")
#         stderr = stderr.decode("utf-8")
#         print(stdout)
#         print(stderr)
#
#     def screen(self, cmd):  # 在手机上截图
#         screenExecute = subprocess.Popen(str(cmd), stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
#         stdout, stderr = screenExecute.communicate()
#         # 输出执行命令结果结果
#
#         print("11111111111")
#
#
#     def saveComputer(self, cmd):  # 将截图保存到电脑
#         screenExecute = subprocess.Popen(str(cmd), stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
#         stdout, stderr = screenExecute.communicate()
#
#         print("222222222222222222222")
#
#
# cmd1 = r"adb shell /system/bin/screencap -p /sdcard/3.png"  # 命令1：在手机上截图3.png为图片名
# cmd2 = r"adb pull /sdcard/3.png d:/3.png"  # 命令2：将图片保存到电脑 d:/3.png为要保存到电脑的路径
# screen = Screenshot()
# screen.screen(cmd1)
# screen.saveComputer(cmd2)
#

# if __name__ == '__main__':
#     screen = Screenshot()
#     cmd2 = r"adb pull /sdcard/3.png C:\Users\majunda\Desktop"  # 命令2：将图片保存到电脑 d:/3.png为要保存到电脑的路径
#     screen.saveComputer(cmd2)


# import tkinter
#
# # 创建主窗口
# win = tkinter.Tk()
#
# # 设置标题
# win.title('选择题')
#
# # 设置大小和位置,前两个x大小 后两个+位置
# win.geometry('400x400+500+200')
#
#
# def updata():
#     message = ''
#     if hobby1.get():
#         message += '权利\n'
#     if hobby2.get():
#         message += '金钱\n'
#     if hobby3.get():
#         message += '女人\n'
#
#     # 清除text中的所有内容(从头到尾）
#     text.delete(0.0, tkinter.END)
#     # 插入到文本框中
#     text.insert(tkinter.INSERT, message)
#
#
# # 要绑定的变量 布尔类型
# hobby1 = tkinter.BooleanVar()
#
# check1 = tkinter.Checkbutton(win, text='选项A', variable=hobby1, command=updata)
# check1.pack()
# hobby2 = tkinter.BooleanVar()
# check2 = tkinter.Checkbutton(win, text='选项B', variable=hobby2, command=updata)
# check2.pack()
# hobby3 = tkinter.BooleanVar()
# check3 = tkinter.Checkbutton(win, text='选项C', variable=hobby3, command=updata)
# check3.pack()
#
# text = tkinter.Text(win, width=30, height=4)
# text.pack()
# # 进入消息循环
# win.mainloop()
import datetime


dangqian = datetime.datetime.now()
strzifu = str(dangqian)
b = strzifu.replace(' ', '')
b = b.replace('-', '')
b = b.replace(':', '')
Index = b.rfind(".")
c= b[Index:]
b = b.replace(c, "")
print(b)
isaaa = os.path.exists("./screenshot\\faa3259c")
if not isaaa:
    os.mkdir("./screenshot\\faa3259c")
print(isaaa)
os.system("adb shell /system/bin/screencap -p /sdcard/"+b+".png")
os.system("adb pull /sdcard/"+b+".png ./screenshot/faa3259c/"+b+".png")
