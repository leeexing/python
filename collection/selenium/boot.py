#!/usr/bin/env python2
# coding=utf-8

import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import random

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
    time.sleep(3)
    has_start = False
    while (not has_start):
        try:
            has_start = EC.visibility_of_element_located(driver.find_element_by_class_name("count-down"))
            print(has_start)
            time.sleep(2)
        except NoSuchElementException:
            print('还没有出现图片')
            time.sleep(0.1)
    i = 0
    clickable = False
    while (not clickable):
        if wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "a_btn_safe"))):
            clickable = True
            print('可以点击啦？')
        else:
            print('*'*20)
            time.sleep(0.2)
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "dr-image")))
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "a_btn_safe")))
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "a_btn_danger")))
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "a_btn_danger")))
    safe_btn = driver.find_element_by_class_name("a_btn_safe")
    danger_btn = driver.find_element_by_class_name("a_btn_danger")
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
        while (not jianzhuang):
            try:
                if random.random() < 0.5:
                    safe_btn.click()
                else:
                    danger_btn.click()
                jianzhuang = True
            except Exception:
                print(Exception)
                time.sleep(1)
        time.sleep(2)
        i += 1
        print('第 {} 题'.format(i))
    btn_again = wait.until(EC.element_to_be_clickable((By.ID, "btn-again")))
    btn_again.click()
    # match_result_out = False
    # while (not match_result_out):
    #     try:
    #         again_btn = driver.find_element_by_xpath("//*[@id='btn-again']")
    #         again_btn.click()
    #         match_result_out = True
    #     except NoSuchElementException:
    #         time.sleep(5)
    match += 1
    print('玩了一局啦' + '*'*10)

driver.close()