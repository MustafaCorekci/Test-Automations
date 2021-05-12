from selenium import webdriver
from SeleniumAmazonTest.loginPage import LoginPage
from SeleniumAmazonTest.searchPage import SearchPage
from SeleniumAmazonTest.productPage import ProductPage
import time

driverPath = "C:/Users/musta/OneDrive/Masaüstü/PythonRepo/chromedriver.exe"
driver = webdriver.Chrome(driverPath)
driver.maximize_window()
driver.get("https://www.amazon.com")

# Login Page
login = LoginPage(driver)
login.openLoginPage()
login.enterMail("mail")
login.clickEmailLogin()
login.enterPassword("password")
login.clickPasswordLogin()

# Search Page
search = SearchPage(driver)
search.enterSearchText("samsung")
search.clickSearch()
search.clickSecondPage()
search.productClick()

# Product Page
product = ProductPage(driver)
product.addToListClick()
product.viewListClick()
product.deleteItemClick()

time.sleep(1)
driver.quit()
