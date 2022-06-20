from selenium import webdriver
from selenium.webdriver.chrome.options import Options


var_ip = '192.168.1.1'

time = 120
options = Options()
#options.set_headless()
options.add_argument("start-maximized")
options.binary_location=r'C:\Users\Dário Ribeiro\AppData\Local\Vivaldi\Application\vivaldi.exe'
driver = webdriver.Chrome(executable_path=r'C:\Users\Dário Ribeiro\Downloads\chromedriver_win32\chromedriver.exe', options=options)
driver.get('http://'+var_ip)

driver.implicitly_wait(time)
username = driver.find_element_by_name('loginUsername')
driver.implicitly_wait(time)
username.send_keys('admin')
driver.implicitly_wait(time)
password = driver.find_element_by_name('loginPassword')
driver.implicitly_wait(time)
password.send_keys('admin')
driver.implicitly_wait(time)
password.submit()

driver.implicitly_wait(time)


driver.find_element_by_link_text("Basic").click()


driver.implicitly_wait(time)

NEXT_BUTTON_XPATH = '//input[@type="submit" and @value="Reboot"]'

button = driver.find_element_by_xpath(NEXT_BUTTON_XPATH)
button.click()

driver.implicitly_wait(time)

obj = driver.switch_to.alert

#Retrieve the message on the Alert window
msg=obj.text
print ("Alert shows following message: "+ msg )

driver.implicitly_wait(time)
#use the accept() method to accept the alert
obj.accept()
