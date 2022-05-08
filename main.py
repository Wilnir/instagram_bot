import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

service = Service("/usr/local/bin/chromedriver")
ACCOUNT = ""
PASSWORD = ""


class InstaFollower:

    def __init__(self):
        # self.driver = webdriver.ChromeOptions(service=service)
        # self.driver.add_argument("--incognito")
        self.driver = webdriver.Chrome(service=service)

    def login(self):
        time.sleep(6)
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        username = self.driver.find_element(By.NAME, "username")
        username.send_keys(ACCOUNT)
        time.sleep(6)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(PASSWORD)
        time.sleep(3)
        password.send_keys(Keys.ENTER)
        time.sleep(4)
        save_info = self.driver.find_element(By.CLASS_NAME, "y3zKF")
        save_info.click()
        time.sleep(5)
        notifications = self.driver.find_element(By.CLASS_NAME, "HoLwm")
        notifications.click()

    def find_followers(self):
        time.sleep(5)
        self.driver.get("http://instagram.com/blog_noisered/")
        time.sleep(5)

        followers = self.driver.find_element(By.XPATH, "//a[contains(@href, '/followers')]")
        followers.click()
        time.sleep(5)

        modal = self.driver.find_element(By.XPATH, "//div[@Class='isgrP']")
        time.sleep(2)
        for i in range(10):
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', modal)
            time.sleep(3)

    def follow(self):
        followers_list = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for button in followers_list:
            try:
                button.click()
                time.sleep(2)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.CLASS_NAME, "HoLwm")
                cancel_button.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()

