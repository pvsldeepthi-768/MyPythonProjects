from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService
import time
import os

def send_whatsapp_message(contact_name,message):
    driver_path = r"C:\Users\bincy\Downloads\edgedriver_win64\msedgedriver.exe"
    service = EdgeService(executable_path=driver_path)
    driver = webdriver.Edge(service=service)

    driver.get("https://web.whatsapp.com")
    wait = WebDriverWait(driver, 60)

    print("🔄 Please scan the QR code...")

    # Wait for the search box to appear
    search_box = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
    ))

    print(f"🔍 Searching for contact: {contact_name}")
    search_box.clear()
    search_box.send_keys(contact_name)
    time.sleep(2)

    contact_xpath = f'//span[@title="{contact_name}"]'
    contact = wait.until(EC.element_to_be_clickable((By.XPATH, contact_xpath)))
    contact.click()
    # Wait for message box
    message_box = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
    ))

    # Send text message
    if message.strip():
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)
        print(f"✅ Text message sent to {contact_name}.")
    time.sleep(5)
    driver.quit()

# --- Run script ---
contact = input("Enter contact name: ")
message = input("Enter message: ")

send_whatsapp_message(contact, message)