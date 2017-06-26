# coding=utf-8
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select

url1="https://as.its-kenpo.or.jp/apply/empty_new?s=PUFETzIwRFpwWlNaMUpIZDlrSGR3MVda"
url2="https://as.its-kenpo.or.jp/apply/empty_new?s=PWd6TjIwRFpwWlNaMUpIZDlrSGR3MVda"
url3="https://as.its-kenpo.or.jp/apply/empty_new?s=PWNqTjIwRFpwWlNaMUpIZDlrSGR3MVda"
dates_in_jpy=["2017年07月07日","2017年07月08日"]
dates_in_eng=["2017-07-07","2017-07-08"]
urls=[url1,url2,url3]
email="**********@gmail.com"
flags=[[0 for i in range(len(dates_in_jpy))] for i in range(len(urls))]
result=-1

browser=webdriver.Chrome()

while 1:
 try:
  for i in range(len(urls)):
   for j in range (len(dates_in_jpy)):
    if flags[i][j] != 1:
     browser.get(urls[i])
     dates=browser.find_element_by_id("apply_join_time").text.encode('utf-8')
     result=dates.find(dates_in_jpy[j])
    if result != -1:
     flags[i][j]=1
     index=j
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
