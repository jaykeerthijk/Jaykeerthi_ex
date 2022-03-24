from selenium import webdriver
from time import sleep
driver = webdriver.Chrome("./chromedriver")
driver.get("http://www.monster.com")
sleep(2)
driver.find_element_by_xpath("//span[text()='Upload Resume']").click()
sleep(2)
driver.find_element_by_xpath("(//input[@type='file'])[2]").send_keys(r"C:\Users\Jagadeesh\Desktop\sample2.txt")
sleep(2)
driver.find_element_by_xpath("(//div[@class='close-button mqfi-cross'])[2]")
sleep(2)

