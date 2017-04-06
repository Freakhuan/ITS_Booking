# coding=utf-8
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select

url="https://as.its-kenpo.or.jp/apply/empty_new?s=PVVqTTIwRFpwWlNaMUpIZDlrSGR3MVda"
target_date="2017年05月08日"
email="freakhuan@gmail.com"

browser=webdriver.Chrome()
browser.get(url)

dates=browser.find_element_by_id("apply_join_time").text.encode('utf-8')
result=dates.find(target_date)

if result != -1:
 index=result+1
 print "Greate!!", target_date
 dropdown=Select(browser.find_element_by_id("apply_join_time"))
 dropdown.select_by_index(index)
 dropdown=Select(browser.find_element_by_id("apply_night_count"))
 dropdown.select_by_index(0)
 browser.find_element_by_id("apply_stay_persons").send_keys("2")
 dropdown=Select(browser.find_element_by_id("house_select")) 
 dropdown.select_by_index(0)
 browser.find_element_by_xpath("//input[@class='button button-primary']").click()
 sleep(5)
 browser.find_element_by_xpath("//input[contains(@name,'apply') and @type='checkbox']").click()
 browser.find_element_by_xpath("//input[@class='button-select button-primary']").click()
 browser.find_element_by_xpath("//input[@class='button-select button-primary']").click()
 browser.find_element_by_id("email_inp").send_keys(email)
else:
 sleep(30)
