import time

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from features.business_utils.test_locators import TestLocators

# This class contains all the required methods for performing automation
class BusinessLogic:

    def __init__(self):
        self.test_locator = TestLocators()

    def open_browser(self):
        try:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
        except Exception as e:
            print('Error -->' + str(e))

    def navigate_to_page(self, url):
        try:
            self.driver.get(url)
        except Exception as e:
            print('Error -->' + str(e))
            self.driver.close()

    def select_parking_type(self,parking_type):
        try:
            parking_dropdown = Select(WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.test_locator.parking_type_dd))))
            parking_dropdown.select_by_visible_text(parking_type)
            # Added this time.sleep just to show the assessment reviewer the desired result, otherwise there is no need of adding it
            time.sleep(1)
        except NoSuchElementException:
            self.driver.close()

    def select_parking_date_time(self, **kwargs):
        try:
            parking_date = kwargs.get("parking_date")
            parking_time = kwargs.get("parking_time")
            parking_mode = kwargs.get("parking_mode")
            parking_date_field=''
            if parking_date is not None:
                if parking_mode.upper() == "ENTRY":
                    parking_date_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.test_locator.parking_entry_date)))
                elif parking_mode.upper() == "EXIT":
                    parking_date_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.test_locator.parking_exit_date)))
                parking_date_field.clear()
                parking_date_field.send_keys(parking_date)
            if parking_time is not None:
                if parking_mode.upper() == "ENTRY":
                    parking_date_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.test_locator.parking_entry_time)))
                elif parking_mode.upper() == "EXIT":
                    parking_date_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.test_locator.parking_exit_time)))
                parking_date_field.clear()
                parking_date_field.send_keys(parking_time)
        except NoSuchElementException:
            self.driver.close()

    def select_time_mode(self, parking_mode, time_mode):
        try:
            if parking_mode.upper()== "ENTRY" and time_mode.upper() == "AM":
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.test_locator.entry_time_am))).click()
            if parking_mode.upper()== "ENTRY" and time_mode.upper() == "PM":
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.test_locator.entry_time_pm))).click()
            if parking_mode.upper()== "EXIT" and time_mode.upper() == "AM":
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.test_locator.exit_time_am))).click()
            if parking_mode.upper()== "EXIT" and time_mode.upper() == "PM":
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.test_locator.exit_time_pm))).click()
        except NoSuchElementException:
            self.driver.close()

    def click_calculate_btn(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.test_locator.calculate_btn))).click()
        except NoSuchElementException:
            self.driver.close()

    def verify_result(self, expected_result):
        try:
            bln_flag = False
            content_to_verify = self.driver.find_element(By.XPATH, self.test_locator.verify_cost).text
            if expected_result in content_to_verify:
                bln_flag = True
                print("Right cost was found in calculation i.e. " + expected_result)
            else:
                print("Required cost was not found in calculation")
            return bln_flag
        except NoSuchElementException:
            print("Required cost was not found in calculation")
            self.driver.close()

    def close_driver(self):
        try:
            self.driver.close()
        except Exception as e:
            print('Error -->' + str(e))

    @pytest.fixture(autouse=True, scope= "module")
    def test_clean_up_process(self):
        yield
        # Teardown
        self.close_driver()




