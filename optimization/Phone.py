import pandas as pd


class Phone():
    def __init__(self, name, model, device, judge, Bangshight):
        self.name = name
        self.model = model
        self.device = device
        self.judge = judge
        self.Bangshight = Bangshight

    def getExceldevice(self, t=[]):
        t.clear()
        df = pd.read_excel('设备对应device.xlsx', header=0, names=["A", "B", "C", "D", "E", "F",
                                                               "G", "H", "I", "J", "K"
                                                               ])
        for i in range(len(df)):
            self.name = df["B"][i]
            self.model = df["H"][i]
            self.device = df["I"][i]
            self.judge = df["J"][i]
            self.Bangshight = df["K"][i]
            a = Phone(self.name, self.model, self.device, self.judge, self.Bangshight)
            t.append(a)
        return t
