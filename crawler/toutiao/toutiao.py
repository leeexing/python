from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time

import io, sys
# 修改默认编码方式
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

driver = webdriver.PhantomJS()
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
}
driver.get('https://www.jianshu.com/')
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(3)
# elems = driver.find_element_by_css_selector('.note-list li')
elems = driver.find_element_by_css_selector('.note-list')
print(elems)
print(elems.text)
print('+'*30)

elems = driver.find_elements_by_xpath('//ul[@class="note-list"]//li')
print(len(elems))

for i in range(10):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    if i >= 2:
        load_more = driver.find_element_by_css_selector('.load-more').click()
    time.sleep(3)
    lists = driver.find_elements_by_css_selector('li[id ^= "note-"]')
    print(len(lists))

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
elems = driver.find_elements_by_css_selector('li[id ^= "note-"]')
print(len(elems))


# elems = driver.find_element_by_xpath('//ul[@class="note-list"]')
# print(elems.text)
# for ele in elems:
#     print(ele.text)
#     print('*'*30)
# driver.execute_script("arguments[0].scrollIntoView();", elems[len(elems) - 1])
print("<<<<<<<<getting content>>>>>>>>")

# data_source = driver.page_source

# print(data_source)

driver.quit()