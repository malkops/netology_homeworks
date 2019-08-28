import time
import unittest

from selenium import webdriver


class YandexPassportTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
        self.test_login = 'test-yandex-login'
        self.test_pwd = 'pwd'
        self.people_delay = 3

    def test_page_passport(self):
        page_url = 'https://passport.yandex.ru/auth/'
        driver = self.driver
        driver.maximize_window()
        driver.get(page_url)

        ele_user_message = driver.find_element_by_id('passp-field-login')
        ele_user_message.clear()
        ele_user_message.send_keys(self.test_login)

        login_btn = driver.find_element_by_css_selector('div > .button2_type_submit')
        login_btn.click()

        time.sleep(self.people_delay)

        user_pwd_input = driver.find_element_by_id('passp-field-passwd')
        user_pwd_input.send_keys(self.test_pwd)

        login_btn = driver.find_element_by_css_selector('div > .button2_type_submit')
        login_btn.click()

        time.sleep(self.people_delay)

        user_login_elem_first = driver.find_element_by_css_selector('.personal-info-login')
        user_test_text = user_login_elem_first.text

        self.assertEqual(self.test_login, user_test_text)

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
