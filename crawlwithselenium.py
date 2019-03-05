#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException

#selenium 開連結
options = webdriver.FirefoxOptions()
# options.add_argument('-headless')  # headless mode
driver = webdriver.Firefox(executable_path=r'/Users/danielm/Desktop/geckodriver', options=options)

#連結 以中時電子報為例
driver.get(r'https://www.facebook.com/pg/CTfans/posts/')

#開檔案 輸出至CT_output.txt
fo = open("CT_output.txt", "w")

#抓時間 寫入檔案
localtime = time.asctime( time.localtime(time.time()) )
fo.write (localtime)
fo.write('\n')
fo.write('\n')

#找FB Class標籤 content是個list
content = driver.find_elements_by_class_name("_4vn1")

#丟進檔案
for i in content:
    asa = i.find_element_by_css_selector('a').get_attribute('href')
    fo.write ( asa.encode('utf-8') )
    fo.write('\n')

    b = i.text
    fo.write ( b.encode('utf-8') )
    fo.write('\n')
    fo.write('\n')
    time.sleep(1)

#關檔案 print Finish & Time
fo.close()
print ("Finish")
print (localtime)


# 等一下再關
time.sleep(5)
driver.quit()
