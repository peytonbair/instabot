#instagram bot driver. Created by Peyton Bair on 5 April 2020.
from selenium import webdriver
import time
class Driver():
    def __init__(self, username, password):
        #setup for instagram login
        self.username = username
        self.password = password
        url = ("https://www.instagram.com/accounts/login/")
        driver = webdriver.Firefox()
        self.driver = driver
        self.driver.get(url)
    def login(self):
        #wait and login
        time.sleep(5)
        self.driver.find_element_by_name("username").send_keys(self.username)
        self.driver.find_element_by_name("password").send_keys(self.password)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button").click()
        #exit out of notification popup

        self.driver.save_screenshot('login.png')
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click();
        time.sleep(1) #sleep before running any other commands
    #actice will get the activity of whoever is in the general list of messages
    def messages(self):
        #click on the message
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div[1]/nav/a[2]").click()
    def getactivity(self):
        activity = self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[3]/div/div/div/div/div[1]/a/div/div[2]/div[2]/div/div/span/span').get_attribute('innerHTML')
        return activity
    def refresh(self):
        self.driver.refresh()
        time.sleep(3)
