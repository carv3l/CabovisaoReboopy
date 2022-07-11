from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from datetime import datetime
#from selenium.webdriver.firefox.options import Options
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
#from selenium.webdriver.firefox.service import Service



var_ip = '192.168.1.1'

hours_to_apply_reboot = ['7:0:0','13:20:0','20:2:0']

hours_to_apply_reset = ['5:0:0','6:0:0']

delay_time = 3600

previous_timestamp = ""
#options = Options()
#options.add_argument("--headless")
#options.add_argument("start-maximized")
#serv = Service(path)
#driver = webdriver.Firefox(service=serv, options=options)

def report(action,current_time):
    f = open("logs/reboopy.log", "a")
    if action == "reboot":
        f.write("Reboot Performed at: " + str(current_time) + " - For more information on the reboot, see Geckodriver.log on parent folder \n")
    if action == "reset":
        f.write("Reset Performed at: " + str(current_time) + " - For more information on the reboot, see Geckodriver.log on parent folder \n")
    f.close()


def perform_action(action):
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

    # Goes to the basic page of the hotbox /RgSetup.asp
    driver.find_element("link text","Basic").click()

    driver.implicitly_wait(delay_time)

    # Get the html element of the button reboot of type = submit

    REBOOT_BUTTON_XPATH = '//input[@type="submit" and @value="Reboot"]'

    RADIO_BUTTON_XPATH = '//input[@type="radio" and @name="RestoreFactoryYes1" and @value="0x01"]'

    APPLY_BUTTON_XPATH = '//input[@type="submit" and @value="Apply"]'


    if(action == "reboot"):
         # Click Action of the Reboot Button on the basic page /RgSetup.asp

        button = driver.find_element("xpath",REBOOT_BUTTON_XPATH)
        button.click()

        # Handle Alert of rebooting

        WebDriverWait(driver, 10).until(EC.alert_is_present())
        driver.switch_to.alert.accept()



    if( action == "reset"):
        # Click Action of the Radio Restore Button on the basic page /RgSetup.asp

        button = driver.find_element("xpath",RADIO_BUTTON_XPATH)
        button.click()

        # Handle Message Alert of resetting

        WebDriverWait(driver, 10).until(EC.alert_is_present())
        driver.switch_to.alert.accept() 

        driver.implicitly_wait(delay_time)

        # Click Action of the Apply Button on the basic page /RgSetup.asp

        button = driver.find_element("xpath",APPLY_BUTTON_XPATH)
        button.click()

    
   
    


    driver.implicitly_wait(delay_time)
    #Close browser
    driver.quit()

    # Get current time for the log
    current_date = datetime.datetime.now()

    # action argument is either reboot or reset
    report(action,current_date)



while True:

    HOUR        = datetime.datetime.now().hour   # the current hour
    MINUTE      = datetime.datetime.now().minute # the current minute
    SECONDS     = datetime.datetime.now().second #the current second
    MILISECONDS     = datetime.datetime.now().microsecond #the current second

   # print(HOUR, MINUTE, SECONDS)

    current_timestamp = str(HOUR) + ':' + str(MINUTE) + ':'+ str(SECONDS)
    
    if current_timestamp != previous_timestamp:

        if (MINUTE in [0,15,25,30,45,55]) and (SECONDS in [0]):
            print(current_timestamp)

        if current_timestamp in hours_to_apply_reboot:
            print("Reboot time")
            perform_action("reboot")

        if current_timestamp in hours_to_apply_reset:
            print("Reset time")
            perform_action("reset")
    
    previous_timestamp = current_timestamp




# Quit Browser
#driver.quit()

d = input("Press any key to exit")
