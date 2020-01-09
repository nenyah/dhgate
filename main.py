import tkinter as tk
from tkinter import ttk  # 导入内部包
from tkinter import filedialog, messagebox

from spider_main import SpiderMain


class MainWindows(tk.Tk):
    def __init__(self):
        super().__init__()  # 初始化基类
        self.title("Dhgate数据采集")
        # self.config(bg='#303030')
        self.iconbitmap('dhgate.ico')
        self.ini_ui()
        self.spider = SpiderMain()

    def ini_ui(self):
        # 设置顶部区域
        self.top_frame = tk.Frame(width=800, height=200)
        self.top_frame.config(bg='#303030')
        # 设置底部区域
        self.bottom_frame = tk.Frame(width=800, height=400)
        self.bottom_frame.config(bg='#303030')

        # 定义顶部区域
        self.lb1 = tk.Label(self.top_frame,
                            text='输入关键词',
                            font=('Hack', 15, 'bold'),
                            bg='#303030',
                            fg='white')
        self.lb2 = tk.Label(self.top_frame,
                            text='页数',
                            font=('Hack', 15, 'bold'),
                            bg='#303030',
                            fg='white')
        self.keyword = tk.Entry(self.top_frame)
        self.num = tk.Entry(self.top_frame)
        self.lb3 = tk.Label(self.top_frame,
                            text='',
                            font=('Hack', 15, 'bold'),
                            bg='#303030',
                            fg='white')
        self.btn1 = tk.Button(self.top_frame, text='开始', command=self.scrapy)
        self.btn2 = tk.Button(self.top_frame,
                              text='清空',
                              command=self.clear_entry_value)
        self.btn3 = tk.Button(self.top_frame,
                              text='导出Excel',
                              command=self.save_data)

        self.lb1.grid(row=0, column=0, padx=10, pady=10)
        self.keyword.grid(row=0, column=1, padx=10, pady=10)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.num.grid(row=1, column=1, padx=10, pady=10)
        self.lb3.grid(row=3, column=0, columnspan=5)
        self.btn1.grid(row=0, column=5)
        self.btn2.grid(row=1, column=5)
        self.btn3.grid(row=0, column=6)

        # 定义底部区域
        self.tree = ttk.Treeview(self.bottom_frame,
                                 show="headings",
                                 height=20,
                                 columns=("编号", "列表链接", "标题", "产品链接", "最低价",
                                          "最高价", "起订量", "销量", "好评数", "卖家",
                                          "店铺链接"))  # 表格
        self.vbar = ttk.Scrollbar(self.bottom_frame,
                                  orient='vertical',
                                  command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        for head in self.tree['columns']:
            self.tree.column(head, width=66)  # 表示列,不显示
            self.tree.heading(head, text=head)  # 显示表头

        self.tree.grid(row=0, column=0)
        self.vbar.grid(row=0, column=1, sticky='NS')
        # 整体布局
        self.top_frame.grid(row=0, column=0)
        self.bottom_frame.grid(row=1, column=0)
        self.top_frame.grid_propagate(0)
        self.bottom_frame.grid_propagate(0)

    def scrapy(self):
        self.clear_result()
        keyword = self.keyword.get()
        page_num = self.num.get()
        print(keyword, page_num)
        if keyword == '':
            messagebox.showinfo(message="关键字不能为空")
            return
        if page_num == '':
            messagebox.showinfo(message="页数不能为空")
            return
        obj_spider = self.spider
        self.lb3.config(text=f"开始采集{keyword}")
        datas = obj_spider.craw(keyword, page_num)
        # print(f"开始采集{keyword}")
        self.lb3.config(text=f"采集完毕")
        self.show_result(datas)

    # 清空文本输入框的值
    def clear_entry_value(self):
        self.keyword.delete(0, tk.END)
        self.num.delete(0, tk.END)
        self.keyword.focus_set()  # 对第一个文本输入框设置光标焦点
        self.clear_result()

    def clear_result(self):
        child_item = self.tree.get_children()
        for item in child_item:
            self.tree.delete(item)

    def show_result(self, datas):
        for i in range(len(datas)):
            self.tree.insert("",
                             i,
                             text=f"line{i+1}",
                             values=(i + 1, *list(datas[i].values())))  # 插入数据

    def save_data(self):
        path = filedialog.asksaveasfilename()  # 返回文件名
        print(path)
        out = self.spider.outputer
        out.to_csv(path)


if __name__ == '__main__':
    app = MainWindows()
    app.mainloop()
