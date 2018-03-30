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

    def output_html(self):
        with open('output.html', 'w') as f:
            f.write("<html>")
            f.write("<body>")
            f.write("<table>")
            for data in self.datas:
                f.write("<tr>")
                f.write(f"<td>{data['page_url']}</td>")
                f.write(f"<td>{data['title']}</td>")
                f.write(f"<td>{data['price']}</td>")
                f.write(f"<td>{data['min_order']}</td>")
                f.write(f"<td>{data['order']}</td>")
                f.write(f"<td>{data['feedback']}</td>")
                f.write(f"<td>{data['seller']}</td>")
                f.write(f"<td>{data['store_url']}</td>")
                f.write(f"<td>{data['store_feedback']}</td>")
                f.write("</tr>")
            f.write("</table>")
            f.write("</body>")
            f.write("</html>")

    def output_csv(self, path="output.csv"):
        with open(path, 'w', newline="") as f:
            writer = csv.DictWriter(f, self.datas[0].keys())
            writer.writeheader()
            for data in self.datas:
                writer.writerow(data)
