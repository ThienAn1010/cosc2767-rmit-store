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

class TestAppearanceCheck():
  def setup_method(self, method):
    self.driver = webdriver.Chrome('/usr/bin/chromedriver',chrome_options=chrome_options)
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
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".animated:nth-child(1)")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".fadeIn")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".learn-more")
    assert len(elements) > 0
    self.driver.find_element(By.CSS_SELECTOR, ".learn-more").click()
    self.vars["url"] = self.driver.execute_script("return window.location.href")
    assert(self.vars["url"] == "http://127.0.0.1/#item-list")
  
