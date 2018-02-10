#!/usr/bin/env python2
# coding=utf-8

import time
import re
import random
import pymongo
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

client = pymongo.MongoClient('localhost', 27017)
PKDB = client['myblog']['pkimg']
name_reg = re.compile(r'\d+\/(\w+)')

def save_2_db(obj):
    for item in obj:
        img_name = name_reg.findall(item[0])
        img = PKDB.find_one({'imgName': img_name[0]})
        if not img:
            obj = {
                'imgName': img_name[0],
                'isDanger': item[1]
            }
            PKDB.save(obj)

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)
driver.maximize_window() 
print (driver.get_window_size())
# driver.set_window_size(1024,768)
driver.get("http://pk.anjianba.cn")

# 图像的数据
img_data = {}

name_box = driver.find_element_by_name("username")
name_box.clear()
name_box.send_keys(u"李星")
start_btn = driver.find_element_by_class_name("mint-button")
start_btn.click()
time.sleep(3)
mask_btn = driver.find_element_by_class_name("a_page_btn_fix")
mask_btn.click()
time.sleep(3)
start_pk_btn = driver.find_element_by_class_name("pk-btn")
start_pk_btn.click()

match = 0
while (match < 10000):
    # time.sleep(3)
    # 匹配对手
    wait_match = False
    while (not wait_match):
        try:
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "count-down")))
            wait_match = True
            print('{:#^20}'.format(''))
        except Exception:
            print('匹配时出现错误。。。')
            time.sleep(0.2)
    
    i = 0
    # wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "dr-image")))
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "dr-image")))
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "a_btn_safe")))
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "a_btn_danger")))
    my_choose = []
    ret_in_page = []
    time.sleep(3)
    for i in range(10):
        found = False
        while (not found):
            try:
                img_elem = driver.find_element_by_class_name("dr-image")
                found = True
            except NoSuchElementException:
                time.sleep(1)
        img_src_url = img_elem.get_attribute("src")

        jianzhuang = False
        my_choice = None
        
        while (not jianzhuang):
            try:
                if random.random() < 0.5:
                    # safe_btn = driver.find_element_by_class_name("a_btn_safe")
                    safe_btn = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "a_btn_safe")))
                    safe_btn.click()
                    my_choice = 'safe'
                    my_choose.append('safe')
                else:
                    # danger_btn = driver.find_element_by_class_name("a_btn_danger")
                    danger_btn = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "a_btn_danger")))
                    danger_btn.click()
                    my_choice = 'danger'
                    my_choose.append('danger')
                jianzhuang = True
            except Exception:
                print('正在配对中。。。。。。')
                time.sleep(1)

        time.sleep(1.2)
        print('第 {} 题'.format(i))
        # if i > 1:
        # print(len(driver.find_elements_by_css_selector('.topic-result li')))
        # print(driver.find_elements_by_css_selector('.topic-result li')[i-1])
        className = driver.find_elements_by_css_selector('.topic-result li')[i].get_attribute('class')
        # 记录页面上的正确答案
        ret_in_page.append(className)
        if className == 'right':
            result = my_choice
        else:
            result = 'safe' if my_choice == 'danger' else 'danger'
        # img_data['imgName'] = img_src_url
        # img_data['result'] = result
        img_data[img_src_url] = result
        # print(img_data)
        i += 1
    
    print('作答选择的答案：')
    for item in my_choose:
        print('++ {} ++ '.format(item), end='')

    print('页面反馈答案：')
    for item in ret_in_page:
        print('-- {} -- '.format(item), end='')
    
    print('统计的标准答案：')
    this_time = list(img_data.items())[-10:]
    for item in this_time:
        print(item)
    save_2_db(this_time)
    

    # 答题结束 在记录一次
    # className = driver.find_elements_by_css_selector('.topic-result li')[i].get_attribute('class')
    # img_data[img_src_url] = className

    waitResult = False
    while (not waitResult):
        try:
            btn_again = wait.until(EC.element_to_be_clickable((By.ID, "btn-again")))
            waitResult = True
        except Exception:
            print(Exception)
            time.sleep(1)

    btn_again = wait.until(EC.element_to_be_clickable((By.ID, "btn-again"))) 
    btn_again.click()
    match += 1
    print('{:+^50}'.format(' 玩了第 {} 局啦 '.format(match)))

driver.close()