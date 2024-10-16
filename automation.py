import selenium;
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://mainedot.drakewell.com/login.asp")

username_field = driver.find_element(By.ID, "username")
username_field.send_keys("ABC") //dummy user name

password_field = driver.find_element(By.ID, "password")
password_field.send_keys("40c9d336")

login_button = driver.find_element(By.ID, "login")
login_button.click()
print("Login button clicked.")

# For the new page to load
WebDriverWait(driver, 15).until(
    EC.url_to_be("https://mainedot.drakewell.com/c2.asp")
)
print("New page loaded.")

try:
    dropdown_trigger = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "filter-option-inner-inner"))
    )
    print("Dropdown trigger is clickable.")
    dropdown_trigger.click()
    print("Dropdown trigger clicked.")

    # Selects the first option from the dropdown
    first_option = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID, 'bs-select-1-1'))
    )
    first_option.click()
    print("First node selected.")

    desired_item = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID, 'tabular_calendar'))
    )
    desired_item.click()
    print("Tabular calendar clicked.")

     # Waits for the site dropdown
    dropdown_trigger2 = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "search_inner"))
    )
    print("Dropdown trigger is clickable.")
    dropdown_trigger2.click()
    print("Dropdown trigger clicked.")


# Selecting the first option from the dropdown
    site_option = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID, '1_B5416AAE-8F21-470B-80CD-4271EDBC02C2'))
    )
    site_option.click()
    print("First site selected.")

    except Exception as e:
    print(f"An error occurred: {e}")

print("The browser will remain open. Close it manually to end the session.")
try:
    while True:
        pass  # Keeps the script running
except KeyboardInterrupt:
    print("Script interrupted. Closing the browser.")
finally:
    driver.quit()
