from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
#from datetime import datetime
#from selenium.webdriver.firefox.options import Options
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
#from selenium.webdriver.firefox.service import Service



var_ip = '192.168.1.1'

hours_to_apply_reboot = ['7:0:0','13:20:0','20:2:0','16:5:0']

hours_to_apply_reset = ['5:0:0']

delay_time = 60

previous_timestamp = ""
#options = Options()
#options.add_argument("--headless")
#options.add_argument("start-maximized")
#serv = Service(path)
#driver = webdriver.Firefox(service=serv, options=options)

def report(action,timestamp):
    f = open("logs/reboopy.log", "a")
    if action == "reboot":
        f.write("Reboot Performed at:" + timestamp + " for more information, see Geckodriver.log on parent folder")
    if action == "reset":
        f.write("Reset Performed at:" + timestamp + " for more information, see Geckodriver.log on parent folder")
    f.close()


def reboot():
    driver = webdriver.Firefox(executable_path="./drivers/geckodriver")
    #driver.implicitly_wait(delay_time)
    driver.get('http://'+var_ip)
    print ("Alert shows following message: ")
    driver.implicitly_wait(delay_time)
    username = driver.find_element('name','loginUsername')
    driver.implicitly_wait(delay_time)
    username.send_keys('admin')
    driver.implicitly_wait(delay_time)
    password = driver.find_element('name','loginPassword')
    driver.implicitly_wait(delay_time)
    password.send_keys('admin')
    driver.implicitly_wait(delay_time)
    password.submit()

    driver.implicitly_wait(delay_time)
    driver.find_element("link text","Basic").click()
    driver.implicitly_wait(delay_time)

    NEXT_BUTTON_XPATH = '//input[@type="submit" and @value="Reboot"]'

    button = driver.find_element("xpath",NEXT_BUTTON_XPATH)
    button.click()
    driver.implicitly_wait(delay_time)
    #Close browser
    driver.close()
    current_date = datetime.datetime.now()
    report('reboot',current_date)






while True:

    HOUR        = datetime.datetime.now().hour   # the current hour
    MINUTE      = datetime.datetime.now().minute # the current minute
    SECONDS     = datetime.datetime.now().second #the current second
    MILISECONDS     = datetime.datetime.now().microsecond #the current second

   # print(HOUR, MINUTE, SECONDS)

    current_timestamp = str(HOUR) + ':' + str(MINUTE) + ':'+ str(SECONDS)
    
    if current_timestamp != previous_timestamp:

        if (MINUTE in [0,15,25,30,45,55]) and (SECONDS in [0,15,25,30,45,55]):
            print(current_timestamp)

        if current_timestamp in hours_to_apply_reboot:
            print("Reboot time")
            reboot()

        if current_timestamp in hours_to_apply_reset:
            print("Reset time")
           # reboot()
    
    previous_timestamp = current_timestamp




# Quit Browser
#driver.quit()

d = input("Press any key to exit")