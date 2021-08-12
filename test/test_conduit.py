import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager



def search_element_xpath(driver, value):
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, value)))
    return element


def search_all_element_xpath(driver, value):
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.XPATH, value)))
    return element


def sign_in(driver):
    search_element_xpath(driver, '//a[@class="nav-link" and @href="#/login"]').click()
    search_element_xpath(driver, '//input[@placeholder="Email"]').send_keys("gzs@gmail.com")
    search_element_xpath(driver, '//input[@placeholder="Password"]').send_keys("Asd12345")
    search_element_xpath(driver, '//button[@class="btn btn-lg btn-primary pull-xs-right"]').click()


class TestConduit(object):
    def setup(self):
        browser_options = Options()
        browser_options.headless = True
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        self.driver.get("http://localhost:1667/")

    def teardown(self):
        self.driver.quit()

    def test_registration(self):
        search_element_xpath(self.driver, '//a[@class="nav-link" and @href="#/register"]').click()
        search_element_xpath(self.driver, '//input[@placeholder="Username"]').send_keys("Gzs")
        search_element_xpath(self.driver, '//input[@placeholder="Email"]').send_keys("gzs@gmail.com")
        search_element_xpath(self.driver, '//input[@placeholder="Password"]').send_keys("Asd12345")
        search_element_xpath(self.driver, '//button[@class="btn btn-lg btn-primary pull-xs-right"]').click()

        search_element_xpath(self.driver, '//button[@class="swal-button swal-button--confirm"]').click()
        logout_button = search_element_xpath(self.driver, '//a[@active-class="active"]')
        assert logout_button.text == " Log out"

    def test_accept_cookies(self):
        search_element_xpath(self.driver,
                             '//button[@class="cookie__bar__buttons__button cookie__bar__buttons__button--accept"]').click()
        time.sleep(2)
        assert (self.driver.find_elements_by_xpath('//button') == [])

    def test_sign_in(self):
        search_element_xpath(self.driver, '//a[@class="nav-link" and @href="#/login"]').click()
        search_element_xpath(self.driver, '//input[@placeholder="Email"]').send_keys("gzs@gmail.com")
        search_element_xpath(self.driver, '//input[@placeholder="Password"]').send_keys("Asd12345")
        search_element_xpath(self.driver, '//button[@class="btn btn-lg btn-primary pull-xs-right"]').click()

        logout_button = search_element_xpath(self.driver, '//a[@class="nav-link" and @active-class="active"]')
        assert logout_button.text == " Log out"

    def test_sign_out(self):
        sign_in(self.driver)
        search_element_xpath(self.driver, '//a[@class="nav-link" and @active-class="active"]').click()
        login_button = search_element_xpath(self.driver, '//a[@class="nav-link" and @href="#/login"]')
        assert login_button.text == "Sign in"

    def test_new_article(self):
        sign_in(self.driver)
        search_element_xpath(self.driver, '//a[@class="nav-link" and @href="#/editor"]').click()
        search_element_xpath(self.driver, '//input[@placeholder="Article Title"]').send_keys("Test Title")
        search_element_xpath(self.driver, '//input[@type="text" and @class="form-control"]').send_keys(
            "It's all about testing")
        search_element_xpath(self.driver, '//textarea[@placeholder="Write your article (in markdown)"]').send_keys(
            "This is the best article i've ever written")
        search_element_xpath(self.driver, '//input[@placeholder="Enter tags"]').send_keys("my favourite tag",
                                                                                          Keys.RETURN)

        search_element_xpath(self.driver, '//button[@type="submit"]').click()

        article_text = search_element_xpath(self.driver, '//div[@class="col-xs-12"]//div//p').text
        assert article_text == "This is the best article i've ever written"

    def test_creating_comment(self):
        sign_in(self.driver)
        search_element_xpath(self.driver, '//a[@href="#/my-feed"]').click()
        time.sleep(1)
        h1_list = self.driver.find_elements_by_xpath('//a[@class="preview-link"]')
        h1_list[0].click()
        with open("test/text.csv", "r") as opened_file:
            file_text = csv.reader(opened_file, delimiter=";")
            file_text_list = list(file_text)
        time.sleep(1)
        for i in file_text_list:
            search_element_xpath(self.driver, '//textarea[@placeholder="Write a comment..."]').send_keys(i)
            search_element_xpath(self.driver, '//button[@class="btn btn-sm btn-primary"]').click()
            time.sleep(1)
        comment_text = search_all_element_xpath(self.driver, '//p[@class="card-text"]')
        assert comment_text[0].text == "10. komment"

    def test_delete_comment(self):
        sign_in(self.driver)
        h1_list = search_all_element_xpath(self.driver, '//a[@class="preview-link"]')
        h1_list[0].click()

        search_element_xpath(self.driver, '//textarea[@placeholder="Write a comment..."]').send_keys("positive comment")
        search_element_xpath(self.driver, '//button[@class="btn btn-sm btn-primary"]').click()
        time.sleep(1)

        delete_buttons = search_all_element_xpath(self.driver, '//i[@class="ion-trash-a"]')
        delete_buttons[0].click()

        time.sleep(1)
        delete_buttons2 = self.driver.find_elements_by_xpath('//i[@class="ion-trash-a"]')
        assert len(delete_buttons) > len(delete_buttons2) or delete_buttons2 == []

    def test_save_article_to_file(self):
        sign_in(self.driver)
        search_element_xpath(self.driver, '//a[@href="#/my-feed"]').click()
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//a[@href="#/my-feed"]'))).click()
        time.sleep(1)
        h1_list = self.driver.find_elements_by_xpath('//a[@class="preview-link"]')
        h1_list[0].click()

        textarea = search_element_xpath(self.driver, '//div[@class="col-xs-12"]//div//p')

        with open("textfromarticle.txt", "w", encoding="utf-8") as file:
            file.write(textarea.text)

        with open("textfromarticle.txt", "r", encoding="utf-8") as opened_file:
            file_text = opened_file.read()
        assert textarea.text == file_text

    def test_article_list(self):
        sign_in(self.driver)

        buttons = WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, '//a[@class="page-link"]')))
        for i in buttons:
            i.click()

        active_button_text = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//li[@class="page-item active"]//a'))).text
        assert active_button_text == "2"

    def test_listing_article_titles_to_file(self):
        sign_in(self.driver)

        article_title_list = WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, '//div[@class="article-preview"]//a//h1')))
        count = 1
        with open("article_title_list.txt", "w") as file:
            for i in article_title_list:
                file.write(f"{count}.  {i.text} \n")
                count += 1

        with open("article_title_list.txt", "r") as read_file:
            file_text = read_file.read()
        index = 0
        for i in article_title_list:
            assert article_title_list[index].text in file_text
            index = + 1

    def test_editing_user_img(self):
        sign_in(self.driver)

        search_element_xpath(self.driver, '//a[@href="#/@Gzs/"]').click()
        old_img_src = search_element_xpath(self.driver, '//img[@class="user-img"]').get_attribute("src")

        search_element_xpath(self.driver, '//a[@href="#/settings" and @class="nav-link"]').click()

        img_input = search_element_xpath(self.driver, '//input[@placeholder="URL of profile picture"]')
        img_input.clear()
        img_input.send_keys("https://cdn.pixabay.com/photo/2014/09/20/13/52/board-453758_960_720.jpg")

        search_element_xpath(self.driver, '//button[@class="btn btn-lg btn-primary pull-xs-right"]').click()
        search_element_xpath(self.driver, '//button[@class="swal-button swal-button--confirm"]').click()

        search_element_xpath(self.driver, '//a[@href="#/@Gzs/"]').click()
        new_img_src = search_element_xpath(self.driver, '//img[@class="user-img"]').get_attribute("src")

        assert old_img_src != new_img_src
