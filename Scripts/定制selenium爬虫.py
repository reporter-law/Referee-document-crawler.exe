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


def selenium(keywords_1,index,time_1,time_2,head):
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
        wait = WebDriverWait(browser, 20)

        send = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="_view_1540966814000"]/div/div[1]/div[2]/input')))
        send.send_keys(keywords_1)

        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="_view_1540966814000"]/div/div[1]/div[3]')))
        button.click()

        try:
            """优化为：：高级检索 """
            click1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="_view_1545034775000"]/div/div[1]/div[1]')))
            click1.click()

            """发送country,暂时不用
            send1 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="s2"]')))
            send1.send_keys("2019")
            """

            """案件类型选择:刑事案件"""
            click_type = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="s8"]')))
            click_type.click()
            click_this = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="gjjs_ajlx"]/li[3]')))
            click_this.click()

            """案由选择:选择案由、刑事案由、具体案由、确定的案由"""
            try:
                #案由选择
                click_type = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="s16"]')))
                click_type.click()
                click_t = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="1"]/i')))
                click_t.click()

                # 贪污渎职罪案由选择
                # 具体案由选择2,15,161,199,212,341,363,376,408,440
                #小下拉框
                if 2 <= int(index)<15:
                    click_this = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="2"]/i')))
                    click_this.click()
                    click_crime = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="%d_anchor"]'%index)))
                    # 贪污：//*[@id="363_anchor"]
                    click_crime.click()
                elif 15<=index <161:
                    click_this = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="15"]/i')))
                    click_this.click()
                    click_crime = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="%d_anchor"]' % index)))
                    # 贪污：//*[@id="363_anchor"]
                    click_crime.click()
                elif 161 <= index <199:
                    click_this = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="161"]/i')))
                    click_this.click()
                    click_crime = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="%d_anchor"]' % index)))
                    click_crime.click()
                elif 199<=index<212:
                    click_this = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="199"]/i')))
                    click_this.click()
                    click_crime = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="%d_anchor"]' % index)))
                    click_crime.click()
                elif 212 <= index <341:
                    click_this = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="212"]/i')))
                    click_this.click()
                    click_crime = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="%d_anchor"]' % index)))
                    click_crime.click()
                elif 341<=index <363:
                    click_this = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="341"]/i')))
                    click_this.click()
                    click_crime = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="%d_anchor"]' % index)))
                    click_crime.click()
                elif 363<= index<376:
                    click_this = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="363"]/i')))
                    click_this.click()
                    click_crime = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="%d_anchor"]' % index)))
                    click_crime.click()
                elif 376<=index<408:
                    click_this = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="376"]/i')))
                    click_this.click()
                    click_crime = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="%d_anchor"]' % index)))
                    click_crime.click()
                elif 408<=index<440:
                    click_this = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="408"]/i')))
                    click_this.click()
                    click_crime = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="%d_anchor"]' % index)))
                    click_crime.click()
                else:
                    click_this = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="440"]/i')))
                    click_this.click()
                    click_crime = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="%d_anchor"]' % index)))
                    click_crime.click()

            except:
                pass

            """审判程序选择:一审程序"""
            click_type = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="s9"]')))
            click_type.click()
            # 具体案由选择
            click_this = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="0201_anchor"]')))
            click_this.click()

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

            """文书数量：15"""
            button_ = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="left_7_3"]/div/select')))
            button_.click()
            # time.sleep(1)
            button_ = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="left_7_3"]/div/select/option[3]')))
            button_.click()

            """再次点击限制条件为省市,限制条件下循环"""
            #xpath制造
            a = ['//*[@id="%d_anchor"]' % (i * 100) for i in range(1, 10)]
            b = ['//*[@id="{name}00_anchor"]'.format(name=chr(x).upper()) for x in range(ord('a'), ord('x') + 1)]
            list_xpath = a + b
            if '//*[@id="W00_anchor"]' in list_xpath:
                list_xpath.remove('//*[@id="W00_anchor"]')
                browser.refresh()

            for xpath_ in list_xpath:
                time.sleep(2)
                try:
                    button_xpath =  wait.until(EC.element_to_be_clickable((By.XPATH, xpath_)))
                    button_xpath.click()
                    """目的：减少遍历次数，进行页数遍历"""


                    condition = browser.find_element_by_xpath('//div[@class="LM_con clearfix"]/div[@class="fr con_right"]/span')
                    #return (condition.text)  # 不能直接//text()原因不明
                    conditions = math.ceil(int(condition.text) / 15)  # 最长12，最短6
                    if int(condition.text) == 0 or conditions==0:
                        browser.quit()
                    elif int(conditions) > 40:  # condition本身已经除了15
                        with open('裁判文书超过600页.txt', 'a+', encoding='utf-8')as file:
                            file.write('出现超过600条的裁判文书,其所在区域为：' + '，其数量为：' + str(condition.text) + '\n')
                    elif 0<int(conditions) <= 40:
                        for index in range(conditions):
                            #print('运行至遍历处。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。')
                            """由于不明原因而需要两次移动"""
                            try:
                                # pyautogui.scroll(10000000)
                                '''全选的点击'''
                                click_1 = wait.until(EC.presence_of_element_located(
                                    (By.XPATH, '//div[@class="LM_tool clearfix"]/div[4]/a[1]/label')))
                                # time.sleep(1)
                                click_1.click()
                                '''批量下载的点击'''
                                click_2 = wait.until(EC.presence_of_element_located((By.XPATH,
                                     '//html/body/div/div[4]/div[2]//div[@class="LM_tool clearfix"]/div[4]/a[3]')))
                                click_2.click()
                                """下一页"""
                                button_ = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="left_7_3"]/a[last()]')))
                                button_.click()
                                time.sleep(4)
                                message = "正在进行第%d页爬取中-----------------------" % index + "xpath为： {}".format(xpath_)
                                yield message
                            except Exception as e:
                                print("出现错误： ", e, xpath_)

                except:
                    browser.quit()
                    selenium(keywords_1, index, time_1, time_2,head=head)
                """取消省份限制"""

                button_xpath = wait.until(EC.element_to_be_clickable((By.XPATH, '//p[@data-key="s33"]/i')))
                button_xpath.click()
                time.sleep(1)


        except Exception as e:
            print(e)
            browser.quit()
            selenium(keywords_1,index,time_1,time_2,head=head)
    except Exception as e:
        print(e)
        browser.quit()
        selenium(keywords_1,index,time_1,time_2,head=head)


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


theLabel_2 = tk.Label(app, text='起始日期：',bg="orange")
theLabel_2.place(x=50,y=220)  # pack()用于自动调节组件的尺寸
entry_3=Entry(app,fg='blue',bg="yellow",width=50,bd=4)
entry_3.place(x=130,y=220)


theLabel_3 = tk.Label(app, text='结束日期：',bg="orange")
theLabel_3.place(x=50,y=240)  # pack()用于自动调节组件的尺寸
entry_4=Entry(app,fg='blue',bg="yellow",width=50,bd=4)
entry_4.place(x=130,y=240)


def head_param():
    var1.set(0)
    print(var1.get())



var1 = tk.IntVar()
var1.set(1)
c1 = tk.Checkbutton(app, text='无头', variable=var1, onvalue=1, offvalue=0,command=head_param,bg="orange")
c1.place(x=50,y=150)
print(var1.get())

"""启动爬虫"""
def run_selenium():
    keywords_1 = entry_1.get().strip()
    index = int(entry_2.get())
    time_1 = entry_3.get().strip()
    time_2 = entry_4.get().strip()
    head = var1.get()
    print(head)


    for message in selenium(keywords_1,index,time_1,time_2,head=head):
        theLabel_3 = tk.Label(app, text=message, bg="orange")
        theLabel_3.place(x=100, y=320)  # pack()用于自动调节组件的尺寸





button1 = Button(app, text="运行", command=run_selenium,width=10,bg='orange')
button1.place(x=260,y=270)
theLabel_5 = tk.Label(app, text='现存问题：某些关键词下省份不全、无法继续更换省份',bg="orange")
theLabel_5.place(x=150,y=350)  # pack()用于自动调节组件的尺寸


app.mainloop()  # 窗口的主事件循环，必须的




