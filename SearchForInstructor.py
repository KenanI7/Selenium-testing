# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestSearchForInstructor():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_searchForInstructor(self):
    self.driver.get("https://ecampus.ius.edu.ba/")
    self.driver.set_window_size(1920, 1053)
    self.driver.find_element(By.LINK_TEXT, "Office Hours").click()
    self.driver.find_element(By.ID, "edit-title").click()
    self.driver.find_element(By.ID, "edit-title").send_keys("O")
    self.driver.find_element(By.ID, "edit-submit-office-hours").click()
    element = self.driver.find_element(By.ID, "edit-submit-office-hours")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.ID, "edit-title--2").click()
    self.driver.find_element(By.ID, "edit-title--2").click()
    self.driver.find_element(By.ID, "edit-title--2").send_keys("Ozge")
    self.driver.find_element(By.ID, "edit-submit-office-hours--2").click()
    element = self.driver.find_element(By.ID, "edit-submit-office-hours--2")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".oh-display:nth-child(1) > .oh-display-label").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oh-display:nth-child(1) > .oh-display-label").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oh-display:nth-child(1) > .oh-display-label").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".oh-display:nth-child(1) > .oh-display-label")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
  
