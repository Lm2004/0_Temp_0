from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
#firefox_binary=binary
#binary = FirefoxBinary('C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe')
driver = webdriver.Firefox()

driver.get('http://google.com')
print("done")
input("Press any key to exit:")
driver.quit()
