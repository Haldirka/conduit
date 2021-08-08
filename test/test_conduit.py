import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

browser_options = Options()
browser_options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)


class TestConduit(object):
    def setup(self):
        self.driver = webdriver.Chrome("C:\\Users\Zsolt\Desktop\webdriver\\chromedriver.exe")
        self.driver.get("http://localhost:1667/")

    def teardown(self):
        self.driver.quit()

    def test_registration(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//a[@class="nav-link" and @href="#/register"]'))).click()
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Username"]'))).send_keys(
                "Gzs")
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Email"]'))).send_keys(
                "gzs@gmail.com")
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Password"]'))).send_keys("Asd12345")
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]'))).click()

            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//button[@class="swal-button swal-button--confirm"]'))).click()
            logout_button = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//a[@active-class="active"]')))
            assert logout_button.text == " Log out"

        except:
            print("hiba")

    def test_accept_cookies(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH,
                                                '//button[@class="cookie__bar__buttons__button cookie__bar__buttons__button--accept"]'))).click()
        # assertion hiányzik
        except:
            print("hiba")

    def test_sign_in(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//a[@class="nav-link" and @href="#/login"]'))).click()
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Email"]'))).send_keys("gzs@gmail.com")
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Password"]'))).send_keys("Asd12345")
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]'))).click()

            logout_button = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//a[@class="nav-link" and @active-class="active"]')))
            assert logout_button.text == " Log out"
        except:
            print("hiba")

    def test_sign_out(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//a[@class="nav-link" and @href="#/login"]'))).click()
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Email"]'))).send_keys("gzs@gmail.com")
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Password"]'))).send_keys("Asd12345")
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]'))).click()

            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//a[@class="nav-link" and @active-class="active"]'))).click()
            login_button = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//a[@class="nav-link" and @href="#/login"]')))
            assert login_button.text == "Sign in"
        except:
            print("hiba")

    def test_new_article(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//a[@class="nav-link" and @href="#/login"]'))).click()
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Email"]'))).send_keys("gzs@gmail.com")
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Password"]'))).send_keys("Asd12345")
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]'))).click()

            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//a[@class="nav-link" and @href="#/editor"]'))).click()
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Article Title"]'))).send_keys(
                "Test Title")
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//input[@type="text" and @class="form-control"]'))).send_keys("It's all about testing")
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//textarea[@placeholder="Write your article (in markdown)"]'))).send_keys(
                "This is the best article i've ever written")
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Enter tags"]'))).send_keys(
                "my favourite tag", Keys.RETURN)

            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]'))).click()

            article_text = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//div[@class="col-xs-12"]//div//p'))).text
            assert article_text == "This is the best article i've ever written"

        except:
            print("hiba")

    def test_creating_comment(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//a[@class="nav-link" and @href="#/login"]'))).click()
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Email"]'))).send_keys("gzs@gmail.com")
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Password"]'))).send_keys("Asd12345")
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]'))).click()

            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//a[@href="#/my-feed"]'))).click()
            time.sleep(1)
            h1_list = self.driver.find_elements_by_xpath('//a[@class="preview-link"]')
            h1_list[0].click()
            with open("text.csv") as opened_file:
                file_text = csv.reader(opened_file, delimiter=";")
                file_text_list = list(file_text)
            time.sleep(1)
            for i in file_text_list:
                WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '//textarea[@placeholder="Write a comment..."]'))).send_keys(
                    i)
                WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//button[@class="btn btn-sm btn-primary"]'))).click()
                time.sleep(1)
            comment_text = WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located((By.XPATH, '//p[@class="card-text"]')))
            assert comment_text[0].text == "10. komment"
        except:
            print("hiba")

    def test_delete_article(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//a[@class="nav-link" and @href="#/login"]'))).click()
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Email"]'))).send_keys("gzs@gmail.com")
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Password"]'))).send_keys("Asd12345")
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]'))).click()

            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//a[@class="nav-link" and @href="#/@Gzs/"]'))).click()
            time.sleep(1)
            h1_list = self.driver.find_elements_by_xpath('//a[@class="preview-link"]')
            h1_list[0].click()
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//button[@class="btn btn-outline-danger btn-sm"]'))).click()
            time.sleep(1)
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//a[@class="nav-link" and @href="#/@Gzs/"]'))).click()
            h1_list2 = self.driver.find_elements_by_xpath('//a[@class="preview-link"]')
            assert len(h1_list) > len(h1_list2)
        except:
            print("hiba")

    def test_edit_article(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//a[@class="nav-link" and @href="#/login"]'))).click()
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Email"]'))).send_keys("gzs@gmail.com")
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Password"]'))).send_keys("Asd12345")
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]'))).click()

            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//a[@class="nav-link" and @href="#/@Gzs/"]'))).click()
            time.sleep(2)
            h1_list = self.driver.find_elements_by_xpath('//a[@class="preview-link"]')
            h1_list[0].click()
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//a[@class="btn btn-sm btn-outline-secondary"]'))).click()

            title = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Article Title"]')))
            about = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//input[@type="text" and @class="form-control"]')))
            text = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
                (By.XPATH, '//textarea[@placeholder="Write your article (in markdown)"]')))
            tag = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Enter tags"]')))
            title.clear()
            title.send_keys("This is an edited title")
            about.clear()
            about.send_keys("This is also edited")
            text.clear()
            text.send_keys("This is already edited")
            tag.clear()
            tag.send_keys("not my favourite tag", Keys.RETURN)
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]'))).click()
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//a[@class="nav-link" and @href="#/@Gzs/"]'))).click()
            time.sleep(2)
            h1_list = self.driver.find_elements_by_xpath('//a[@class="preview-link"]//h1')
            assert h1_list[0].text == "This is an edited title"
        except:
            print("hiba")

    def test_save_article_to_file(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//a[@class="nav-link" and @href="#/login"]'))).click()
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Email"]'))).send_keys("gzs@gmail.com")
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Password"]'))).send_keys("Asd12345")
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]'))).click()

            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//a[@href="#/my-feed"]'))).click()
            time.sleep(1)
            h1_list = self.driver.find_elements_by_xpath('//a[@class="preview-link"]')
            h1_list[0].click()
            textarea = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//div[@class="col-xs-12"]//div//p')))

            with open("textfromarticle.txt", "w", encoding="utf-8") as file:
                file.write(textarea.text)

            with open("textfromarticle.txt", "r", encoding="utf-8") as opened_file:
                file_text = opened_file.read()
            assert textarea.text == file_text
        except:
            print("hiba")

    def test_article_list(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//a[@class="nav-link" and @href="#/login"]'))).click()
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Email"]'))).send_keys("gzs@gmail.com")
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Password"]'))).send_keys("Asd12345")
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]'))).click()

            buttons = WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located((By.XPATH, '//a[@class="page-link"]')))
            for i in buttons:
                i.click()

            active_button_text = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//li[@class="page-item active"]//a'))).text
            assert active_button_text == "2"
        except:
            print("hiba")

        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)

