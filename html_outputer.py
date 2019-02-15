# -*- coding: utf-8 -*-
# Created on 2018年3月9日
# @author: Administrator
import csv


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.extend(data)

    def to_html(self):
        with open('output.html', 'w') as f:
            f.write("<html>")
            f.write("<body>")
            f.write("<table>")
            f.write("<tr>")
            for key in self.datas[0].keys():
                f.write(f"<td>{key}</td>")
            f.write("</tr>")
            for data in self.datas:
                f.write("<tr>")
                for key, value in data.items():
                    f.write(f"<td>{value}</td>")
                f.write("</tr>")
            f.write("</table>")
            f.write("</body>")
            f.write("</html>")

    def to_csv(self, path="output.csv"):
        with open(path, 'w', newline="") as f:
            try:
                writer = csv.DictWriter(f, self.datas[0].keys())
            except IndexError:
                print(self.datas[0].keys())

            writer.writeheader()
            for data in self.datas:
                writer.writerow(data)
