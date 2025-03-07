# RMIT University Vietnam
# Course: COSC2767 Systems Deployment and Operations
# Semester: 2022B
# Assessment: Assignment 3
# Author: Nguyen Hoang Thien An
# ID: 3825455
# Created  date: 08/09/2022
# Last modified: 15/09/2022
# Acknowledgement: Jenkins, Ansible, AWS EC2, AWS ECS, AWS SQS, AWS EventBridge, Selenium

# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')

class TestAppearanceCheck():
  def setup_method(self, method):
    self.driver = webdriver.Chrome(options=chrome_options)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_appearanceCheck(self):
    self.driver.get("http://127.0.0.1/")
    self.driver.set_window_size(1936, 1056)
    assert self.driver.title == "RMIT Store"
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".navbar-brand > img")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".slider_inner")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.LINK_TEXT, "Clothing")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.LINK_TEXT, "Accessories")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.LINK_TEXT, "Stationery")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.LINK_TEXT, "Course")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.LINK_TEXT, "Special-Collection")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.LINK_TEXT, "Sale")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".nav_searchFrom > .lnr")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.XPATH, "//h2[contains(.,\'Global University\')]")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.XPATH, "//h5[contains(.,\'Buy at Our Store\')]")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.XPATH, "//a[contains(@href, \'#item-list\')]")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.XPATH, "//h1[contains(.,\'Database connection error\')]")
    assert len(elements) == 0
    self.driver.find_element(By.CSS_SELECTOR, ".learn-more").click()
    self.vars["url"] = self.driver.execute_script("return window.location.href")
    assert(self.vars["url"] == "http://127.0.0.1/#item-list")
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".col-md-3:nth-child(1) > img")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".col-md-3:nth-child(2) > img")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".col-md-3:nth-child(3) > img")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".col-md-3:nth-child(4) > img")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".col-md-3:nth-child(5) > img")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".col-md-3:nth-child(6) > img")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".col-md-3:nth-child(7) > img")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".col-md-3:nth-child(8) > img")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".col-md-3:nth-child(9) > img")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".col-md-3:nth-child(10) > img")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".col-md-3:nth-child(11) > img")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".col-md-3:nth-child(12) > img")
    assert len(elements) > 0
  
