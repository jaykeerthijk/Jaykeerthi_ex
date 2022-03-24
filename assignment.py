from selenium import webdriver
from time import sleep
from selenium.webdriver.support.color import Color
# ele = driver.find_element_by_xpath("//a[text()='Register']")
# print(ele.value_of_css_selector("color"))
# c = Color.from_string(color)
driver = webdriver.Chrome("./chromedriver")
driver.get("http://demowebshop.tricentis.com")
#To find size
ele1 = driver.find_element_by_xpath("//span[text()='Shopping cart']").size
print(ele1)
#to find location
ele2 = driver.find_element_by_xpath("//span[text()='Shopping cart']").location
print(ele2)
#To find both size and location at a time
ele3 = driver.find_element_by_xpath("//span[text()='Shopping cart']").rect
print(ele3)
# print(ele)
# c = Color.from_string(ele)
# print(c.hex)

# links = driver.find_elements_by_xpath("//a")
# list = []
# for item in links:
#     list.append(item.text)
#     sleep(1)
# print(list)
# for li in list:
#     if li == " ":
#         pass
#     li = sorted(list, key=len)
# print(li)
# print(list == li)
# ele = driver.find_element_by_xpath("//a[text()='Register']")
# print(ele.value_of_css_selector("color"))
# from selenium.webdriver.support.color import Color
# c = Color.from_string(bg_colour_first)











# def gen(n):
#     for i in n:
#         yield i
