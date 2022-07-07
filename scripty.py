from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.firefox.options import Options
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
#from selenium.webdriver.firefox.service import Service



var_ip = '192.168.1.1'

time = 60
#options = Options()
#options.add_argument("--headless")
#options.add_argument("start-maximized")
#serv = Service(path)
#driver = webdriver.Firefox(service=serv, options=options)
driver = webdriver.Firefox(executable_path="./drivers/geckodriver")
#driver.implicitly_wait(time)
driver.get('http://'+var_ip)
print ("Alert shows following message: ")
driver.implicitly_wait(time)
username = driver.find_element('name','loginUsername')
driver.implicitly_wait(time)
username.send_keys('admin')
driver.implicitly_wait(time)
password = driver.find_element('name','loginPassword')
driver.implicitly_wait(time)
password.send_keys('admin')
driver.implicitly_wait(time)
password.submit()

driver.implicitly_wait(time)


driver.find_element("link text","Basic").click()


driver.implicitly_wait(time)

NEXT_BUTTON_XPATH = '//input[@type="submit" and @value="Reboot"]'

#button = driver.find_element("xpath",NEXT_BUTTON_XPATH)
#button.click()

driver.implicitly_wait(time)

#Close browser
driver.close()

# Quit Browser
#driver.quit()
