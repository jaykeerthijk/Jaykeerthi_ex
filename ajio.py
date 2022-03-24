from selenium import webdriver
from time import sleep
import re
driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.ajio.com/")
driver.maximize_window()
sleep(4)
driver.find_element_by_xpath("//input[@name='searchVal']").send_keys("shoes")
sleep(4)
driver.find_element_by_xpath("//span[@class='ic-search']").click()
sleep(5)
shoes = driver.find_elements_by_xpath("//div[@class='nameCls']")
shoe = []
for item in shoes:
    shoe.append(item.text)
print(shoe)
print(len(shoe))
shoes_original_price = driver.find_elements_by_xpath("//span[@class='orginal-price']")
price = []
for rupee in shoes_original_price:
    price.append(rupee.text)
print(price)
prices = []
# a = ''
for item in price:
    match = re.findall(r"\d", item)
    prices.append(int(''.join(match)))
print(prices)

s = sorted(prices)
print(s[-1])
print(s[0])



# for ele in match:
#     a = ''
#     a += ''.join(ele)
#     print(a)
# shoes_actual_price = driver.find_elements_by_xpath("//span[@class='price  ']")


