from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_path = "/usr/bin/chromedriver"

zip = input("Place your zip: ")
adress = input("Place your adress: ")
number = input("Place your number: ")


driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)
driver.get("https://submit.sfbb.gr/EligibilityCheck.aspx")

driver.find_element_by_id("ctl00_cphMain_txtZipCode_I").send_keys(zip)
time.sleep(1)

driver.find_element_by_class_name("dx-vam").click()
time.sleep(1)

driver.find_element_by_id("ctl00_cphMain_txtAddress_I").send_keys(adress)
time.sleep(1)

driver.find_element_by_class_name("dx-vam").click()
time.sleep(1)

driver.find_element_by_id("ctl00_cphMain_txtStreetNumber_I").send_keys(number)
time.sleep(1)

driver.find_element_by_class_name("dx-vam").click()
time.sleep(1)

message = driver.find_element_by_xpath("//div[contains(@class, 'alert')]/span").text

print(message)
driver.close()
