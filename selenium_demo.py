from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get('http://seo.chinaz.com/www.ynu.edu.cn')
elem = browser.find_element_by_css_selector('#seo_BaiduSiteIndex > a > font')
print(elem.text)

browser.quit()