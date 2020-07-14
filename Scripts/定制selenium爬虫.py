"""程序说明"""

# -*-  coding: utf-8 -*-
# Author: cao wang
# Datetime : 2020
# software: PyCharm
# 收获:
import math
import time
from selenium import webdriver
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.options import Options
import tkinter as tk
from tkinter import *
import os
from PIL import Image,ImageTk
import tkinter.messagebox


def selenium(keywords_1,index,time_1,time_2,head,type):
    """网页获取"""
    # 无弹窗
    path = "E:\Firefox\Download"
    if not os.path.exists(path):
        os.makedirs(path)
    profile = webdriver.FirefoxProfile()
    profile.set_preference('browser.download.dir', path.strip('\u202a'))
    profile.set_preference('browser.download.folderList', 2)
    profile.set_preference('browser.download.manager.showWhenStarting', False)
    profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/zip,application/octet-stream')
    #无图
    profile.set_preference('browser.migration.version', 9001)
    profile.set_preference('permissions.default.image', 2)
    #无头
    ops = Options()
    if head == 1:
        ops.add_argument('--headless')

    """网页获取"""
    browser = webdriver.Firefox(firefox_profile=profile,options=ops)
    actions = ActionChains(browser)

    try:
        browser.get('http://wenshu.court.gov.cn')
        wait = WebDriverWait(browser, 30)

        send = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="_view_1540966814000"]/div/div[1]/div[2]/input')))
        send.send_keys(keywords_1)

        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="_view_1540966814000"]/div/div[1]/div[3]')))
        button.click()

        try:
            """优化为：：高级检索 """
            click1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="_view_1545034775000"]/div/div[1]/div[1]')))
            click1.click()

            #发送country,
            """
            send1 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="s2"]')))
            send1.send_keys(country)
            """
            # 具体案由选择



            """案件类型选择:刑事案件"""
            if type == 1:
                click_type = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="s8"]')))
                click_type.click()
                click_this = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="gjjs_ajlx"]/li[3]')))
                click_this.click()
            else:
                click_ = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="selectCon_other_ajlx"]')))
                click_.click()
                click_type = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="gjjs_ajlx"]/li[4]')))
                click_type.click()
            if type == 1:
                """审判程序选择:一审程序"""
                click_type = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="s9"]')))
                click_type.click()
                click_this = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="0201_anchor"]')))
                click_this.click()
            else:
                """审判程序选择:一审程序"""
                click_type = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="s9"]')))
                click_type.click()
                click_this = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="0301_anchor"]')))
                click_this.click()



            """案由选择:选择案由、刑事案由、具体案由、确定的案由"""
            try:
                # 案由选择
                click_type = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="s16"]')))
                click_type.click()
                click_t = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="1"]/i')))
                click_t.click()
                if type ==1:

                    # 贪污渎职罪案由选择
                    # 具体案由选择2,15,161,199,212,341,363,376,408,440
                    # 小下拉框
                    if 2 <= int(index) < 15:
                        click_this = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="2"]/i')))
                        click_this.click()
                        click_crime = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="%d_anchor"]' % index)))
                        # 贪污：//*[@id="363_anchor"]
                        click_crime.click()
                    elif 15 <= index < 58:
                        click_this = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="15"]/i')))
                        click_this.click()
                        click_crime = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="%d_anchor"]' % index)))

                        click_crime.click()
                    elif 58<=index<161:
                        click_this = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="58"]/i')))
                        click_this.click()
                        click_crime = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="%d_anchor"]' % index)))
                        click_crime.click()

                    elif 161 <= index < 199:
                        click_this = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="161"]/i')))
                        click_this.click()
                        click_crime = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="%d_anchor"]' % index)))
                        click_crime.click()
                    elif 199 <= index < 212:
                        click_this = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="199"]/i')))
                        click_this.click()
                        click_crime = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="%d_anchor"]' % index)))
                        click_crime.click()
                    elif 212 <= index < 341:
                        click_this = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="212"]/i')))
                        click_this.click()
                        click_crime = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="%d_anchor"]' % index)))
                        click_crime.click()
                    elif 341 <= index < 363:
                        click_this = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="341"]/i')))
                        click_this.click()
                        click_crime = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="%d_anchor"]' % index)))
                        click_crime.click()
                    elif 363 <= index < 376:
                        click_this = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="363"]/i')))
                        click_this.click()
                        click_crime = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="%d_anchor"]' % index)))
                        click_crime.click()
                    elif 376 <= index < 408:
                        click_this = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="376"]/i')))
                        click_this.click()
                        click_crime = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="%d_anchor"]' % index)))
                        click_crime.click()
                    elif 408 <= index < 440:
                        click_this = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="408"]/i')))
                        click_this.click()
                        click_crime = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="%d_anchor"]' % index)))
                        click_crime.click()
                    elif index == 440:
                        click_this = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="440"]/i')))
                        click_this.click()
                        click_crime = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="%d_anchor"]' % index)))
                        click_crime.click()
                else:
                    print("民事案例检索中")
                    click_this = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="9000"]/i')))
                    click_this.click()
                    click_crime = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="%d_anchor"]' % index)))
                    click_crime.click()


            except:
                pass

            """审判日期：2019"""
            time_send = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cprqStart"]')))
            time_send.click()
            # 开始日期,直接sendkeys不行
            actions.send_keys_to_element(time_send, time_1).perform()

            time_send_end = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cprqEnd"]')))
            time_send_end.click()
            # time_send_end.clear()
            actions.send_keys_to_element(time_send_end, time_2).perform()  # 结束日期

            """检索确定"""
            button_1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchBtn"]')))
            button_1.click()


            """再次点击限制条件为省市,限制条件下循环"""
            #xpath制造
            a = ['//*[@id="%d_anchor"]' % (i * 100) for i in range(1, 10)]
            b = ['//*[@id="{name}00_anchor"]'.format(name=chr(x).upper()) for x in range(ord('a'), ord('x') + 1)]
            list_xpath = a + b
            if '//*[@id="W00_anchor"]' in list_xpath:
                list_xpath.remove('//*[@id="W00_anchor"]')

            for xpath_ in list_xpath:
                try:
                    time.sleep(1)
                    browser.find_element_by_xpath(xpath_)
                except:
                    pass
                else:
                    button_xpath =  wait.until(EC.element_to_be_clickable((By.XPATH, xpath_)))
                    button_xpath.click()
                    browser.refresh()
                    """文书数量：15"""
                    button_ = wait.until(
                        EC.presence_of_element_located((By.XPATH, '//div[@class="left_7_3"]/div/select')))
                    button_.click()
                    button_ = wait.until(
                        EC.element_to_be_clickable((By.XPATH, '//div[@class="left_7_3"]/div/select/option[3]')))
                    button_.click()
                    time.sleep(4)
                    """目的：减少遍历次数，进行页数遍历"""

                    condition = browser.find_element_by_xpath(
                        '//div[@class="LM_con clearfix"]/div[@class="fr con_right"]/span')
                    # return (condition.text)  # 不能直接//text()原因不明
                    conditions = math.ceil(int(condition.text) / 15)  # 最长12，最短6
                    if int(condition.text) == 0 or conditions == 0:
                        """取消省份限制"""
                        button_xpath = wait.until(EC.element_to_be_clickable((By.XPATH, '//p[@data-key="s33"]/i')))
                        button_xpath.click()
                        time.sleep(1)
                    elif int(conditions) > 40:  # condition本身已经除了15
                        with open('裁判文书超过600页.txt', 'a+', encoding='utf-8')as file:
                            file.write('出现超过600条的裁判文书,其所在区域为：' + '，其数量为：' + str(condition.text) + '\n')
                    elif 0 < int(conditions) <= 40:
                        for index in range(conditions):
                            # print('运行至遍历处。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。')
                            try:
                                '''全选的点击'''
                                click_1 = wait.until(EC.presence_of_element_located(
                                    (By.XPATH, '//div[@class="LM_tool clearfix"]/div[4]/a[1]/label')))

                                click_1.click()
                                '''批量下载的点击'''
                                click_2 = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                                     '//html/body/div/div[4]/div[2]//div[@class="LM_tool clearfix"]/div[4]/a[3]')))
                                click_2.click()
                                """下一页"""
                                button_ = wait.until(
                                    EC.presence_of_element_located((By.XPATH, '//div[@class="left_7_3"]/a[last()]')))
                                button_.click()
                                time.sleep(4)
                                message = "正在进行第%d页爬取中-----------------------" % index + "xpath为： {}".format(xpath_)
                                yield message
                            except Exception as e:
                                print("此处退出-------3-----------")
                                print("出现错误： ", e, xpath_)
                    else:

                        """取消省份限制"""
                        button_xpath = wait.until(EC.element_to_be_clickable((By.XPATH, '//p[@data-key="s33"]/i')))
                        button_xpath.click()
                        time.sleep(1)

                    """取消省份限制"""
                    button_xpath = wait.until(EC.element_to_be_clickable((By.XPATH, '//p[@data-key="s33"]/i')))
                    button_xpath.click()
                    time.sleep(1)




        except Exception as e:
            print("第一个",e)
            pass
    except Exception as e:
        print("第二个",e)
        pass


"""日历控件"""
# -*- coding: utf-8 -*-
import calendar
import tkinter.font as tkFont
from tkinter import ttk

datetime = calendar.datetime.datetime
timedelta = calendar.datetime.timedelta


class Calendar:

    def __init__(s, point=None, position=None):
        # point    提供一个基点，来确定窗口位置
        # position 窗口在点的位置 'ur'-右上, 'ul'-左上, 'll'-左下, 'lr'-右下
        # s.master = tk.Tk()
        s.master = tk.Toplevel()
        s.master.withdraw()
        fwday = calendar.SUNDAY

        year = datetime.now().year
        month = datetime.now().month
        locale = None
        sel_bg = 'orange'
        sel_fg = '#05640e'

        s._date = datetime(year, month, 1)
        s._selection = None  # 设置为未选中日期

        s.G_Frame = ttk.Frame(s.master)

        s._cal = s.__get_calendar(locale, fwday)

        s.__setup_styles()  # 创建自定义样式
        s.__place_widgets()  # pack/grid 小部件
        s.__config_calendar()  # 调整日历列和安装标记
        # 配置画布和正确的绑定，以选择日期。
        s.__setup_selection(sel_bg, sel_fg)

        # 存储项ID，用于稍后插入。
        s._items = [s._calendar.insert('', 'end', values='') for _ in range(6)]

        # 在当前空日历中插入日期
        s._update()

        s.G_Frame.pack(expand=1, fill='both')
        s.master.overrideredirect(1)
        s.master.update_idletasks()
        width, height = s.master.winfo_reqwidth(), s.master.winfo_reqheight()
        if point and position:
            if position == 'ur':
                x, y = point[0], point[1] - height
            elif position == 'lr':
                x, y = point[0], point[1]
            elif position == 'ul':
                x, y = point[0] - width, point[1] - height
            elif position == 'll':
                x, y = point[0] - width, point[1]
        else:
            x, y = (s.master.winfo_screenwidth() - width) / 2, (s.master.winfo_screenheight() - height) / 2
        s.master.geometry('%dx%d+%d+%d' % (width, height, x, y))  # 窗口位置居中
        s.master.after(300, s._main_judge)
        s.master.deiconify()
        s.master.focus_set()
        s.master.wait_window()  # 这里应该使用wait_window挂起窗口，如果使用mainloop,可能会导致主程序很多错误

    def __get_calendar(s, locale, fwday):
        # 实例化适当的日历类
        if locale is None:
            return calendar.TextCalendar(fwday)
        else:
            return calendar.LocaleTextCalendar(fwday, locale)

    def __setitem__(s, item, value):
        if item in ('year', 'month'):
            raise AttributeError("attribute '%s' is not writeable" % item)
        elif item == 'selectbackground':
            s._canvas['background'] = value
        elif item == 'selectforeground':
            s._canvas.itemconfigure(s._canvas.text, item=value)
        else:
            s.G_Frame.__setitem__(s, item, value)

    def __getitem__(s, item):
        if item in ('year', 'month'):
            return getattr(s._date, item)
        elif item == 'selectbackground':
            return s._canvas['background']
        elif item == 'selectforeground':
            return s._canvas.itemcget(s._canvas.text, 'fill')
        else:
            r = ttk.tclobjs_to_py({item: ttk.Frame.__getitem__(s, item)})
            return r[item]

    def __setup_styles(s):
        # 自定义TTK风格
        style = ttk.Style(s.master)
        arrow_layout = lambda dir: (
            [('Button.focus', {'children': [('Button.%sarrow' % dir, None)]})]
        )
        style.layout('L.TButton', arrow_layout('left'))
        style.layout('R.TButton', arrow_layout('right'))

    def __place_widgets(s):
        # 标头框架及其小部件
        Input_judgment_num = s.master.register(s.Input_judgment)  # 需要将函数包装一下，必要的
        hframe = ttk.Frame(s.G_Frame)
        gframe = ttk.Frame(s.G_Frame)
        bframe = ttk.Frame(s.G_Frame)
        hframe.pack(in_=s.G_Frame, side='top', pady=5, anchor='center')
        gframe.pack(in_=s.G_Frame, fill=tk.X, pady=5)
        bframe.pack(in_=s.G_Frame, side='bottom', pady=5)

        lbtn = ttk.Button(hframe, style='L.TButton', command=s._prev_month)
        lbtn.grid(in_=hframe, column=0, row=0, padx=12)
        rbtn = ttk.Button(hframe, style='R.TButton', command=s._next_month)
        rbtn.grid(in_=hframe, column=5, row=0, padx=12)

        s.CB_year = ttk.Combobox(hframe, width=5, values=[str(year) for year in
                                                          range(datetime.now().year, datetime.now().year - 11, -1)],
                                 validate='key', validatecommand=(Input_judgment_num, '%P'))
        s.CB_year.current(0)
        s.CB_year.grid(in_=hframe, column=1, row=0)
        s.CB_year.bind('<KeyPress>', lambda event: s._update(event, True))
        s.CB_year.bind("<<ComboboxSelected>>", s._update)
        tk.Label(hframe, text='年', justify='left').grid(in_=hframe, column=2, row=0, padx=(0, 5))

        s.CB_month = ttk.Combobox(hframe, width=3, values=['%02d' % month for month in range(1, 13)], state='readonly')
        s.CB_month.current(datetime.now().month - 1)
        s.CB_month.grid(in_=hframe, column=3, row=0)
        s.CB_month.bind("<<ComboboxSelected>>", s._update)
        tk.Label(hframe, text='月', justify='left').grid(in_=hframe, column=4, row=0)

        # 日历部件
        s._calendar = ttk.Treeview(gframe, show='', selectmode='none', height=7)
        s._calendar.pack(expand=1, fill='both', side='bottom', padx=5)

        ttk.Button(bframe, text="确 定", width=6, command=lambda: s._exit(True)).grid(row=0, column=0, sticky='ns',
                                                                                    padx=20)
        ttk.Button(bframe, text="取 消", width=6, command=s._exit).grid(row=0, column=1, sticky='ne', padx=20)

        tk.Frame(s.G_Frame, bg='#565656').place(x=0, y=0, relx=0, rely=0, relwidth=1, relheigh=2 / 200)
        tk.Frame(s.G_Frame, bg='#565656').place(x=0, y=0, relx=0, rely=198 / 200, relwidth=1, relheigh=2 / 200)
        tk.Frame(s.G_Frame, bg='#565656').place(x=0, y=0, relx=0, rely=0, relwidth=2 / 200, relheigh=1)
        tk.Frame(s.G_Frame, bg='#565656').place(x=0, y=0, relx=198 / 200, rely=0, relwidth=2 / 200, relheigh=1)

    def __config_calendar(s):
        # cols = s._cal.formatweekheader(3).split()
        cols = ['日', '一', '二', '三', '四', '五', '六']
        s._calendar['columns'] = cols
        s._calendar.tag_configure('header', background='grey90')
        s._calendar.insert('', 'end', values=cols, tag='header')
        # 调整其列宽
        font = tkFont.Font()
        maxwidth = max(font.measure(col) for col in cols)
        for col in cols:
            s._calendar.column(col, width=maxwidth, minwidth=maxwidth,
                               anchor='center')

    def __setup_selection(s, sel_bg, sel_fg):
        def __canvas_forget(evt):
            canvas.place_forget()
            s._selection = None

        s._font = tkFont.Font()
        s._canvas = canvas = tk.Canvas(s._calendar, background=sel_bg, borderwidth=0, highlightthickness=0)
        canvas.text = canvas.create_text(0, 0, fill=sel_fg, anchor='w')

        canvas.bind('<Button-1>', __canvas_forget)
        s._calendar.bind('<Configure>', __canvas_forget)
        s._calendar.bind('<Button-1>', s._pressed)

    def _build_calendar(s):
        year, month = s._date.year, s._date.month

        # update header text (Month, YEAR)
        header = s._cal.formatmonthname(year, month, 0)

        # 更新日历显示的日期
        cal = s._cal.monthdayscalendar(year, month)
        for indx, item in enumerate(s._items):
            week = cal[indx] if indx < len(cal) else []
            fmt_week = [('%02d' % day) if day else '' for day in week]
            s._calendar.item(item, values=fmt_week)

    def _show_select(s, text, bbox):
        """为新的选择配置画布。"""
        x, y, width, height = bbox

        textw = s._font.measure(text)

        canvas = s._canvas
        canvas.configure(width=width, height=height)
        canvas.coords(canvas.text, (width - textw) / 2, height / 2 - 1)
        canvas.itemconfigure(canvas.text, text=text)
        canvas.place(in_=s._calendar, x=x, y=y)

    def _pressed(s, evt=None, item=None, column=None, widget=None):
        """在日历的某个地方点击。"""
        if not item:
            x, y, widget = evt.x, evt.y, evt.widget
            item = widget.identify_row(y)
            column = widget.identify_column(x)

        if not column or not item in s._items:
            # 在工作日行中单击或仅在列外单击。
            return

        item_values = widget.item(item)['values']
        if not len(item_values):  # 这个月的行是空的。
            return

        text = item_values[int(column[1]) - 1]
        if not text:  # 日期为空
            return

        bbox = widget.bbox(item, column)
        if not bbox:  # 日历尚不可见
            s.master.after(20, lambda: s._pressed(item=item, column=column, widget=widget))
            return

        # 更新，然后显示选择
        text = '%02d' % text
        s._selection = (text, item, column)
        s._show_select(text, bbox)

    def _prev_month(s):
        """更新日历以显示前一个月。"""
        s._canvas.place_forget()
        s._selection = None

        s._date = s._date - timedelta(days=1)
        s._date = datetime(s._date.year, s._date.month, 1)
        s.CB_year.set(s._date.year)
        s.CB_month.set(s._date.month)
        s._update()

    def _next_month(s):
        """更新日历以显示下一个月。"""
        s._canvas.place_forget()
        s._selection = None

        year, month = s._date.year, s._date.month
        s._date = s._date + timedelta(
            days=calendar.monthrange(year, month)[1] + 1)
        s._date = datetime(s._date.year, s._date.month, 1)
        s.CB_year.set(s._date.year)
        s.CB_month.set(s._date.month)
        s._update()

    def _update(s, event=None, key=None):
        """刷新界面"""
        if key and event.keysym != 'Return': return
        year = int(s.CB_year.get())
        month = int(s.CB_month.get())
        if year == 0 or year > 9999: return
        s._canvas.place_forget()
        s._date = datetime(year, month, 1)
        s._build_calendar()  # 重建日历

        if year == datetime.now().year and month == datetime.now().month:
            day = datetime.now().day
            for _item, day_list in enumerate(s._cal.monthdayscalendar(year, month)):
                if day in day_list:
                    item = 'I00' + str(_item + 2)
                    column = '#' + str(day_list.index(day) + 1)
                    s.master.after(100, lambda: s._pressed(item=item, column=column, widget=s._calendar))

    def _exit(s, confirm=False):
        """退出窗口"""
        if not confirm: s._selection = None
        s.master.destroy()

    def _main_judge(s):
        """判断窗口是否在最顶层"""
        try:
            # s.master 为 TK 窗口
            # if not s.master.focus_displayof(): s._exit()
            # else: s.master.after(10, s._main_judge)

            # s.master 为 toplevel 窗口
            if s.master.focus_displayof() == None or 'toplevel' not in str(s.master.focus_displayof()):
                s._exit()
            else:
                s.master.after(10, s._main_judge)
        except:
            s.master.after(10, s._main_judge)

        # s.master.tk_focusFollowsMouse() # 焦点跟随鼠标

    def selection(s):
        """返回表示当前选定日期的日期时间。"""
        if not s._selection: return None

        year, month = s._date.year, s._date.month
        return str(datetime(year, month, int(s._selection[0])))[:10]

    def Input_judgment(s, content):
        """输入判断"""
        # 如果不加上==""的话，就会发现删不完。总会剩下一个数字
        if content.isdigit() or content == "":
            return True
        else:
            return False











"""可视化"""
app = tk.Tk()  # 根窗口的实例(root窗口)
#调节窗口大小
app.geometry('600x400')
app.geometry('+450+150')
app.title('裁判文书爬虫1.0',)  # 根窗口标题


"""背景图片"""
cav = Canvas(app, width=950, height=550,bg="orange")

def image_open(filename,width,height):
    img = Image.open(filename).resize((width,height))
    return ImageTk.PhotoImage(img)

file = os.path.join(os.path.split(__file__)[0],"logo.png")
im = image_open(file,600,150)

cav.create_image(0,0,anchor='nw', image=im)
cav.place(x=0,y=0)


"""输入框"""

theLabel = tk.Label(app, text='检索关键词：',bg="orange")
theLabel.place(x=50,y=180)  # pack()用于自动调节组件的尺寸
entry_1=tk.Entry(app,fg='blue',bg="yellow",width=50,bd=4)
entry_1.place(x=130,y=180)


theLabel_1 = tk.Label(app, text='案由索引：',bg="orange")
theLabel_1.place(x=50,y=200)  # pack()用于自动调节组件的尺寸
entry_2=Entry(app,fg='blue',bg="yellow",width=50,bd=4)
entry_2.place(x=130,y=200)

"""弹出框在菜单栏中"""
def Pop_up_box():
    tkinter.messagebox.showinfo('刑事索引框说明：索引范围','"危害国家安全罪":2, "危害公共安全罪":15, "破坏社会主义市场经济秩序罪":58, '
        '"侵犯公民人身权利民主权利罪":161, "侵犯财产罪":199, "妨害社会管理秩序罪":212,"危害国防利益罪:341, "贪污贿赂罪":363, '
                                          '"渎职罪":376, "军人违反职责罪":408,"九七年十月以前刑事案由或罪名":440')


def Pop_up_box_1():
    tkinter.messagebox.showinfo('民事索引框说明：索引范围9000-9999',"然而不能点击小的案由，从民事案由到最终案由一共两层，"
                                          "民事案由中只能在下一层点击而不能在下下一层点击")
"""顶部菜单"""
# 创建一个顶级菜单
menubar = Menu(app)

# 创建一个下拉菜单“文件”，然后将它添加到顶级菜单中
filemenu = Menu(menubar, tearoff=False)
#分下拉菜单到主菜单
filemenu.add_command(label="民事索引说明",command=Pop_up_box_1)
filemenu.add_command(label="刑事索引说明",command=Pop_up_box)
filemenu.add_command(label='退出', command=app.quit)
menubar.add_cascade(label="提示",menu=filemenu)
# 显示菜单
app.config(menu=menubar)





"""日历控件1"""
x=600
y=450
date_str_1 = tk.StringVar()
date_1 = Entry(app, textvariable=date_str_1,fg='blue',bg="yellow",width=22)
date_1.place(x=130, y=228)

# Calendar((x, y), 'ur').selection() 获取日期，x,y为点坐标
date_str_gain = lambda: [
    date_str_1.set(date)

    for date in [Calendar((x, y), 'ur').selection()]
    if date]
tk.Button(app, text='开始日期:',font=('微软雅黑',8), command=date_str_gain,bg="orange",width=10).place(x=50,y=225)






"""日历控件2"""
x_=800
y_=450
date_str = tk.StringVar()
date_2 = Entry(app, textvariable=date_str,fg='blue',bg="yellow",width=22)
date_2.place(x=330, y=228)

# Calendar((x, y), 'ur').selection() 获取日期，x,y为点坐标
date_str_gain = lambda: [
    date_str.set(date)

    for date in [Calendar((x_, y_), 'ur').selection()]
    if date]
tk.Button(app, text='结束日期:', font=('微软雅黑',8),command=date_str_gain,bg="orange",width=10,height=1).place(x=250,y=225)


"""选择框"""
def head_param():
    var1.set(0)
    print(var1.get())

var1 = tk.IntVar()
var1.set(1)
c1 = tk.Checkbutton(app, text='无头', variable=var1, onvalue=1, offvalue=0,command=head_param,bg="orange")
c1.place(x=50,y=150)
#print(var1.get())

#2
def type_param():
    var2.set(0)
    print(var2.get())

var2 = tk.IntVar()
var2.set(1)
c1 = tk.Checkbutton(app, text='刑事', variable=var2, onvalue=1, offvalue=0,command=head_param,bg="orange")
c1.place(x=100,y=150)
#print(var1.get())

"""启动爬虫"""
def run_selenium():
    keywords_1 = entry_1.get().strip()
    index = int(entry_2.get())
    time_1 = date_1.get().strip()
    time_2 = date_2.get().strip()
    head = var1.get()
    type = var2.get()
    if type ==1 and 1<=index<=443:
        theLabel_5 = tk.Label(app, text="刑事案件检索中", bg="orange")
        theLabel_5.place(x=100, y=300)

        for message in selenium(keywords_1, index, time_1, time_2, head=head, type=type):
            theLabel_3 = tk.Label(app, text=message, bg="orange")
            theLabel_3.place(x=100, y=320)  # pack()用于自动调节组件的尺寸

    elif type==0 and 9000<=index<=9999:
        theLabel_5 = tk.Label(app, text="民事案件检索中", bg="orange")
        theLabel_5.place(x=100, y=300)

        for message in selenium(keywords_1, index, time_1, time_2, head=head, type=type):
            theLabel_3 = tk.Label(app, text=message, bg="orange")
            theLabel_3.place(x=100, y=320)  # pack()用于自动调节组件的尺寸

    else:
        theLabel_5 = tk.Label(app, text="索引错误", bg="orange")
        theLabel_5.place(x=100, y=300)






button1 = Button(app, text="运行", command=run_selenium,width=10,bg='orange')
button1.place(x=260,y=270)
theLabel_5 = tk.Label(app, text='现存问题：1、网络问题：有时会遇到页面无法刷新处理，解决方法重启',bg="orange")
theLabel_5.place(x=100,y=350)  # pack()用于自动调节组件的尺寸


app.mainloop()  # 窗口的主事件循环，必须的




