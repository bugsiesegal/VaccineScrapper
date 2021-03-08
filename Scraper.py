from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import os
import time

from flask import Flask

options = webdriver.ChromeOptions()
ChromeDriverLocation = os.getcwd() + "/Driver/chromedriver.exe"
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(ChromeDriverLocation, options=options)
driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Chrome/88.0.4324.192'})
driver.get("https://www.kroger.com/i/coronavirus-update/vaccine")


