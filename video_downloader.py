#!/usr/bin/env python

# To run this script type the following at the command line:
# ./video_downloader.py -e (ENTER THE EMAIL YOU USE TO LOGIN TO COURSERA)
# you will then be prompted for your password
# alternatively you can also type the following at the command line:
# ./video_downloader.py --email (ENTER THE EMAIL YOU USE TO LOGIN TO COURSERA)
# you will then be prompted for your password

# downloading part of the script to come

import argparse
import getpass

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

parser = argparse.ArgumentParser(description='deals with args')
parser.add_argument('-e', '--email', help='The email you use to log into Coursera.org', required=True)
args = parser.parse_args()
user_email = str(args.email)
user_password = getpass.getpass("Enter your Coursera password: ")

browser = webdriver.Firefox()

wait = WebDriverWait(browser, 10)

def sign_in(username, password):
    browser.find_element_by_id('signin-email').send_keys(username)
    browser.find_element_by_id('signin-password').send_keys(password)
    browser.find_element_by_class_name('coursera-signin-button').click()

def sign_out():
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.coursera-header-link.coursera-header-account')))
    account_menu = browser.find_elements_by_css_selector('a.coursera-header-link.coursera-header-account')[-1]
    account_menu.click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@href='/account/logout']")))
    browser.find_element_by_xpath("//*[@href='/account/logout']").click()

def go_to_page(page):
    browser.get(page)
    ready_to_proceed = wait.until(EC.presence_of_element_located((By.ID,'signin-email')))

go_to_page('https://accounts.coursera.org/signin')

sign_in(user_email, user_password)

sign_out()
