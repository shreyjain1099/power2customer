from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import time
chrome_path = r"C:\Users\Lenovo\Desktop\chromedriver.exe"

import datetime
start_date = datetime.date(2019, 6, 13)
end_date   = datetime.date(2019, 6, 15)
date = pd.date_range(start_date, end_date)
y = []
for testdate in date:
    z = datetime.datetime.strptime(str(testdate.date()), '%Y-%m-%d').strftime('%d/%m/%y')
    y.append(z)    

driver = webdriver.Chrome(chrome_path)
driver.get("https://www.power2customer.com/")
time.sleep(1)
inputElement = driver.find_element_by_id("loginName")
inputElement.send_keys('parakh')
inputElement = driver.find_element_by_id("loginPassword")
inputElement.send_keys('15356')
#time.sleep(2)
inputElement.submit() 
performance_report = driver.find_element_by_link_text('Performance Reports')
hover = ActionChains(driver).move_to_element(performance_report)
hover.perform()
driver.find_element_by_id("submenu3_1").click()

for finaldates in y:
    #print(finaldates)
    #time.sleep(1)

    javascript_date = "document.getElementsByClassName('subpagetext')[0].value = '"+finaldates+"';"
    driver.execute_script(javascript_date) 

    driver.find_element_by_xpath('/html/body/div/table[2]/tbody/tr/td[2]/center/form/table[2]/tbody/tr[3]/td/input[1]').click()
    table = driver.find_element_by_xpath('/html/body/div/table[2]/tbody/tr/td[2]/center')
    rows=table.text.split('\n')
    if len(rows) > 5:
        c
    else:
        driver.find_element_by_xpath('//*[@id="BUTTON1"]').click()
