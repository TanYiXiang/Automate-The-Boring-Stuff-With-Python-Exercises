# Author: Tan Yi Xiang
# Source: Automate the Boring stuff with python Ch. 11 Project
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

"""Automatically plays the game 2048."""

browser = webdriver.Firefox(executable_path='D:\Python\Python37-32\geckodriver.exe')  # Change path if needed
browser.get('https://gabrielecirulli.github.io/2048/')
gameElement = browser.find_element_by_tag_name('html')

"""Stimulate direction key presses."""
while True:
    gameElement.send_keys(Keys.UP)
    gameElement.send_keys(Keys.RIGHT)
    gameElement.send_keys(Keys.DOWN)
    gameElement.send_keys(Keys.LEFT)
