import os
import time
import secrets
import threading
from colorama import init
from termcolor import colored
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

init()
print('\033[35m' """
██████╗░░█████╗░████████╗  ██████╗░██╗░░░██╗  ░░░░░██╗██╗░░░██╗██████╗░░█████╗░████████╗
██╔══██╗██╔══██╗╚══██╔══╝  ██╔══██╗╚██╗░██╔╝  ░░░░░██║██║░░░██║██╔══██╗██╔══██╗╚══██╔══╝
██████╦╝██║░░██║░░░██║░░░  ██████╦╝░╚████╔╝░  ░░░░░██║██║░░░██║██████╦╝██║░░██║░░░██║░░░
██╔══██╗██║░░██║░░░██║░░░  ██╔══██╗░░╚██╔╝░░  ██╗░░██║██║░░░██║██╔══██╗██║░░██║░░░██║░░░
██████╦╝╚█████╔╝░░░██║░░░  ██████╦╝░░░██║░░░  ╚█████╔╝╚██████╔╝██████╦╝╚█████╔╝░░░██║░░░
╚═════╝░░╚════╝░░░░╚═╝░░░  ╚═════╝░░░░╚═╝░░░  ░╚════╝░░╚═════╝░╚═════╝░░╚════╝░░░░╚═╝░░░
""")
print('\033[33m' """          Code Grepper Follower Bot By @Jub0t on Instagram & jareer12 on Github.
―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
""")

user_Id = "98467"

Options = Options()
Options.headless = True
Options.add_experimental_option('excludeSwitches', ['enable-logging'])

while True:
   random_string = secrets.token_hex(nbytes=16)
   chrome_driver_path = "C:/Users/0726abja/Documents/Code-Grepper/CG BOT/chromedriver.exe"

   driver = webdriver.Chrome(chrome_driver_path, options=Options)
   driver.get("https://www.codegrepper.com/index.php")

   signup = driver.find_element_by_xpath("//*[text()='Signup']")
   signup.click()

   time.sleep(.3)
   email_input = driver.find_element_by_class_name("input1")
   email_input.send_keys(random_string, "@jub0t.com")
   
   time.sleep(.3)
   pass_input = driver.find_element_by_name("password")
   pass_input.send_keys("jub0t123")

   time.sleep(.3)
   register = driver.find_element_by_id("register_button")
   register.click()

   time.sleep(3)
   driver.get(
       "https://www.codegrepper.com/api/follow.php?follow_user_id=" + user_Id + "&follow=1")
   time.sleep(2)
   driver.get(
       "https://www.codegrepper.com/app/profile.php?id=" + user_Id)
   current_followers = driver.find_elements_by_tag_name("a")
   followers = str(len(current_followers) - 20)
   time.sleep(2)
   driver.get("https://www.codegrepper.com/api/logout.php")
   audit_log = open(
       "C:/Users/0726abja/Documents/Code-Grepper/CG BOT/emails.txt", "a")
   audit_log.writelines("\n" + random_string + "@jub0t.com:jub0t123",)

   print('\033[35m', 'Follower Update:', '\033[32m',
         "Success =========>", '\033[34m', "Current Aproximate Followers:", followers)
   driver.quit()
