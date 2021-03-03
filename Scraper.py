from selenium import webdriver
import os

ChromeDriverLocation = os.getcwd() + "/Driver/chromedriver.exe"
driver = webdriver.Chrome(ChromeDriverLocation)
driver.get("https://vaccinefinder.org/search/")

ZipCodeInput = '//*[@id="zipCode"]'
SearchButton = '//*[@id="split-screen-content"]/form/div[2]/button'

ZipCode = "10002"

driver.find_element_by_xpath(ZipCodeInput).send_keys(ZipCode)
driver.find_element_by_xpath(SearchButton).click()
VaccinationSites = driver.find_elements_by_class_name("sc-dkQUut TREMO")

avalibility = []

implimentation = ["walgreens"]

def findsite(VaccinationSites):
    for Site in VaccinationSites:
        print(Site.find_element_by_class_name("sc-gsWdvU cGnDyB"))
        if Site.find_element_by_class_name("sc-WZYaI exHCwL").text == "In Stock" and implimentation in Site.find_element_by_class_name("sc-gsWdvU cGnDyB").lower:
            avalibility.append(
                {
                    "Distance": Site.find_element_by_class_name("sc-bXevSJ doIxg").text,
                    "Location": Site.find_element_by_class_name("sc-gsWdvU cGnDyB").text
                }
            )
            Site.find_element_by_class_name("fas fa-arrow-right").click()
            return None


findsite(VaccinationSites)
#
# driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div/div/div/div/div/div/div[1]/div[1]/a')

print(avalibility)