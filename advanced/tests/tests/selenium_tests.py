import time
from selenium import webdriver


class YandexPassportTestCase:
    def __init__(self):
        self.test_login = 'test-login'
        self.test_pwd = 'pwd'
        self.people_delay = 3

    def open_webdriver(self):
        return webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')

    def test_page_passport(self):
        page_url = 'https://passport.yandex.ru/auth/'
        driver = self.open_webdriver()
        driver.maximize_window()
        driver.get(page_url)

        ele_user_message = driver.find_element_by_id('passp-field-login')
        ele_user_message.clear()
        ele_user_message.send_keys(self.test_login)

        login_btn = driver.find_element_by_css_selector('div > .button2_type_submit')
        login_btn.click()

        time.sleep(self.people_delay)

        try:
            user_pwd_input = driver.find_element_by_id('passp-field-passwd')
        except Exception:
            driver.close()
            return False
        user_pwd_input.send_keys(self.test_pwd)

        time.sleep(self.people_delay)

        login_btn = driver.find_element_by_css_selector('div > .button2_type_submit')
        login_btn.click()

        time.sleep(self.people_delay)

        try:
            driver.find_element_by_css_selector('.personal-info-login')
        except Exception:
            driver.close()
            return False
        driver.close()

        return True


if __name__ == '__main__':
    test_class = YandexPassportTestCase()
    print(test_class.test_page_passport())
