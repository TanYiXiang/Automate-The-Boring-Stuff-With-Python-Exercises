# Author: Tan Yi Xiang
# Source: Automate the Boring stuff with python Ch. 11 Project

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import re
import time

"""Automatically logs into yahoo email account and send messages."""

emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+      # username
        @                      # @ symbol
        [a-zA-Z0-9.-]+         # domain name
        (\.[a-zA-Z]{2,4})      # dot-something
        )''', re.VERBOSE)

sourceEmail = input('What is your email address?:\n')
destEmail = input('What is the address of the destination email?:\n')
if not emailRegex.match(sourceEmail):
    print("Invalid source email address provided.")
elif not emailRegex.match(destEmail):
    print('Invalid destination email address provided.')
else:
    password = input("What is your password?:\n")
    message = input("What is the message you want to send?:\n")

    browser = webdriver.Firefox(executable_path='D:\Python\Python37-32\geckodriver.exe')  # Change path if needed
    browser.get('https://login.yahoo.com')
    time.sleep(3)

    # Login
    loginTextField = browser.find_element_by_id('login-username')
    loginTextField.send_keys(sourceEmail)
    loginTextField.send_keys(Keys.ENTER)
    time.sleep(3)

    # Password
    passwordTextField = browser.find_element_by_id('login-passwd')
    passwordTextField.send_keys(password)
    passwordTextField.send_keys(Keys.ENTER)
    time.sleep(5)

    # Click mail
    mailLink = browser.find_element_by_id('mega-bottombar-mail')
    mailLink.send_keys(Keys.ENTER)
    time.sleep(4)

    # Click compose
    composeButton = WebDriverWait(browser, 20).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, '[data-test-id = "compose-button"]')))
    composeButton.send_keys(Keys.ENTER)
    time.sleep(2)

    # Recipient
    recipientTextField = browser.find_element_by_id('message-to-field')
    recipientTextField.send_keys(destEmail)

    # Enter Subject
    messageSubjectElem = browser.find_element_by_css_selector('input[placeholder = "Subject"]')
    messageSubjectElem.send_keys('Test')

    # Message
    messageField = WebDriverWait(browser, 20).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, '[data-test-id = "rte"]')))
    messageField.send_keys(message)

    # Send
    sendButton = browser.find_element_by_css_selector('button[data-test-id = "compose-send-button"]')
    sendButton.send_keys(Keys.ENTER)

    browser.close()
