import selenium
from selenium import webdriver
# Using Chrome to access web
driver = webdriver.Chrome()
# Open the website
driver.get('https://www.truecaller.com/search/in/7200444471')

# Select the id box
signin = driver.find_element_by_class('TopNav__SignIn')
signin.click()


clickTo = driver.find_element_by_class('sign-in-dialog-provider')
clickTo.click()
