# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTestRedirect():
  def setup_method(self, method):
    self.driver = webdriver.Chrome(options=chrome_options)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testRedirect(self):
    self.driver.get("http://127.0.0.1/")
    self.driver.set_window_size(1936, 1056)
    assert self.driver.title == "RMIT Store"
    self.driver.find_element(By.LINK_TEXT, "Clothing").click()
    assert self.driver.title == "Official RMIT Apparel - RMIT Store"
    self.driver.execute_script("window.history.go(-1)")
    self.driver.find_element(By.LINK_TEXT, "Accessories").click()
    assert self.driver.title == "Accessories - RMIT Store"
    self.driver.execute_script("window.history.go(-1)")
    self.driver.find_element(By.LINK_TEXT, "Stationery").click()
    assert self.driver.title == "Stationery - RMIT Store"
    self.driver.execute_script("window.history.go(-1)")
    self.driver.find_element(By.LINK_TEXT, "Course").click()
    assert self.driver.title == "Course - RMIT Store"
    self.driver.execute_script("window.history.go(-1)")
    self.driver.find_element(By.LINK_TEXT, "Special-Collection").click()
    assert self.driver.title == "Special Collection - RMIT Store"
    self.driver.execute_script("window.history.go(-1)")
    self.driver.find_element(By.LINK_TEXT, "Sale").click()
    assert self.driver.title == "Sale - RMIT Store"
  
