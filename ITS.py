# coding=utf-8
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select

url1="https://as.its-kenpo.or.jp/apply/empty_new?s=PVVqTTIwRFpwWlNaMUpIZDlrSGR3MVda"
url2="https://as.its-kenpo.or.jp/apply/empty_new?s=PVlqTTIwRFpwWlNaMUpIZDlrSGR3MVda"
dates_in_jpy=["2017年05月03日","2017年05月04日","2017年05月05日","2017年05月06日"]
dates_in_eng=["2017-05-03","2017-05-04","2017-05-05","2017-05-06"]
email="********@gmail.com"

browser=webdriver.Chrome()

while 1:
 try:
  for num in range(len(dates_in_jpy)):
   browser.get(url1)
   dates=browser.find_element_by_id("apply_join_time").text.encode('utf-8')
   result=dates.find(dates_in_jpy[num])
   if result == -1:
    browser.get(url2)
    dates=browser.find_element_by_id("apply_join_time").text.encode('utf-8')
    result=dates.find(dates_in_jpy[num])
   if result != -1:
    index=num
    break
   
  if result != -1:
   print "Greate!!", dates_in_jpy[index]
   dropdown=Select(browser.find_element_by_id("apply_join_time"))
   dropdown.select_by_value(dates_in_eng[index])
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
   browser.find_element_by_xpath("//input[@class='button button-primary']").click()
   browser.switch_to.alert.accept()
  else:
   sleep(30)
 except:
  print "Error happened, retry"
  sleep(30)
