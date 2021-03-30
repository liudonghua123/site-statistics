from selenium import webdriver

from selenium.webdriver.common.keys import Keys
# http://allselenium.info/wait-for-elements-python-selenium-webdriver/
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import WebDriverException

def _find_element(driver, by):
    """Looks up an element. Logs and re-raises ``WebDriverException``
    if thrown."""
    try:
        return driver.find_element(*by)
    except NoSuchElementException as e:
        raise e
    except WebDriverException as e:
        raise e
class texts_to_be_present_in_element(object):
    """ An expectation for checking if the given texts is present in the
    specified element.
    locator, texts
    """
    def __init__(self, locator, texts_):
        self.locator = locator
        self.texts = texts_

    def __call__(self, driver):
        try:
            element_text = _find_element(driver, self.locator).text
            return any([text == element_text for text in self.texts])
        except StaleElementReferenceException:
            return False


browser = webdriver.Chrome()

browser.get('https://www.ping.cn/ping/www.ynu.edu.cn')

wait = WebDriverWait(browser, 120)
wait.until(texts_to_be_present_in_element((By.CSS_SELECTOR, "div.main > div.mainMsg1 > span"), ['', '已检测结束']))
elem = browser.find_element_by_css_selector(' div.page04d6 > div:nth-child(4) > p')

print(elem.text)

browser.quit()