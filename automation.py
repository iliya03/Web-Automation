import selenium;
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://mainedot.drakewell.com/login.asp")

username_field = driver.find_element(By.ID, "username")
username_field.send_keys("APOUDEL")

password_field = driver.find_element(By.ID, "password")
password_field.send_keys("40c9d336")

login_button = driver.find_element(By.ID, "login")
login_button.click()
print("Login button clicked.")

# Wait for the new page to load
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

    # Select the first option from the dropdown
    first_option = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID, 'bs-select-1-1'))
    )
    first_option.click()
    print("First node selected.")

#     dropdown_menu = WebDriverWait(driver, 15).until(
#     EC.visibility_of_element_located((By.XPATH, "//option[@value='node=maine_dot_counters']"))
# )

    

    # dropdown_trigger = WebDriverWait(driver, 15).until(
    #     EC.element_to_be_clickable((By.CLASS_NAME, 'btn dropdown-toggle group-select'))
    # )
    
    # print("Dropdown trigger is clickable.")
    # dropdown_trigger.click()
    # print("Dropdown trigger clicked.")

    # print("'MAINE_DOT_CCS' node selected.")

    desired_item = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID, 'tabular_calendar'))
    )
    desired_item.click()
    print("Tabular calendar clicked.")

     # Wait for the site dropdown to be present and visible
    dropdown_trigger2 = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "search_inner"))
    )
    print("Dropdown trigger is clickable.")
    dropdown_trigger2.click()
    print("Dropdown trigger clicked.")


# Select the first option from the dropdown
    site_option = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID, '1_B5416AAE-8F21-470B-80CD-4271EDBC02C2'))
    )
    site_option.click()
    print("First site selected.")

    
    
    #  # Get all the site elements
    # site_elements =  dropdown_trigger2.find_elements(By.XPATH, './/a[@title]')
    # print(f"Found {len(site_elements)} sites.")

    # # Loop through each site
    # for index, site_element in enumerate(site_elements):
    #     site_name = site_element.text
    #     print(f"Selecting site: {site_name}")
    #     site_element.click()

    #     # Wait a little before moving to the next site
    #     time.sleep(2)  # Adjust the sleep time if necessary
        
    #     # Re-open the site dropdown to select the next site (if there's more to select)
    #     if index < len(site_elements) - 1:
    #         dropdown_trigger = WebDriverWait(driver, 15).until(
    #             EC.element_to_be_clickable((By.CLASS_NAME, "filter-option-inner-inner"))
    #         )
    #         dropdown_trigger.click()


    

    
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