from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

ChromeDriverLocation = os.getcwd() + "/Driver/chromedriver.exe"
driver = webdriver.Chrome(ChromeDriverLocation)
driver.get("https://vaccinefinder.org/search/")

ZipCodeInput = '//*[@id="zipCode"]'
SearchButton = '//*[@id="split-screen-content"]/form/div[2]/button'

ZipCode = "10002"

driver.find_element_by_xpath(ZipCodeInput).send_keys(ZipCode)
driver.find_element_by_xpath(SearchButton).click()
time.sleep(3)
VaccinationSites = driver.find_elements_by_xpath('//div[@class="sc-dkQUut TREMO"]')

avalibility = []

implimentation = ["walgreens"]

def findsite(VaccinationSites):
    for Site in VaccinationSites:
        if Site.find_element_by_xpath('./div[2]/div[2]/div[2]/div/p').text == "In Stock" and implimentation[0] in Site.find_element_by_xpath('./div[2]/div[1]/div').text.lower():
            print(Site.find_element_by_xpath('./div[2]/div[2]/div[2]/div/p').text)
            print(Site.find_element_by_xpath('./div[2]/div[1]/div').text)
            avalibility.append(
                {
                    "Distance": Site.find_element_by_xpath('./div[2]/div[2]/div[1]').text,
                    "Location": Site.find_element_by_xpath('./div[2]/div[1]/div').text
                }
            )
            # Site.find_element_by_class_name("fas fa-arrow-right").click()
            return None


findsite(VaccinationSites)
#
# driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div/div/div/div/div/div/div[1]/div[1]/a')

print(avalibility)

driver.close()