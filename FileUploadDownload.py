from selenium import webdriver
import time
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service

def websitestatus():
    try:
        service = Service(executable_path='/usr/bin/chromedriver')
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
        # driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver/")   #/usr/bin/chromedriver/     /usr/lib/chromium-browser/
        driver.get("https://www.ilovepdf.com/pdf_to_word")
        time.sleep(10)
        #submit_button = driver.find_element(By.ID, "submit-button-id")  # Change to button's ID
        input_element = driver.find_element(By.ID, "uploader")#select the uploadbutton
        input_element.click()
        time.sleep(10)
        #file_path = "/home/mrnby/Desktop/vachana/Test_Upload.pdf"   # Make this as an ENV VAR
        pyautogui.write("/home/mrnby/Desktop/vachana/Test_Upload.pdf",interval=0.25)#search for file
        pyautogui.press('enter')
        time.sleep(5)
        upload_element = driver.find_element(By.ID, "processTask")#uploads the file
        upload_element.click()
        time.sleep(10)
        download_element = driver.find_element(By.CLASS_NAME, "downloader")#download the file
        download_element.click()
        time.sleep(20)
        driver.get("chrome://downloads/")
        time.sleep(30)
        #dn_element = driver.find_element(By.XPATH, "(//div[@id='title-area'])[1]")#to access first-element in the download page
        dn_element = driver.find_element(By.XPATH, "(//div[@id='maincontainer']//div[@id='content']//div[@id='main-content']//div[@id='details']//div[@id='title-area'])[1]")
        text=dn_element.text
        time.sleep(10)
        print(f"The {text} was downloaded successfully")
        driver.quit()
        
        
    except Exception as e:
        print("Unable to open the driver and make a request due to following execption")
        print(e)
    # finally:
    #     driver.close()
    

websitestatus()


#"(//div[@id='maincontainer']//div[@id='content']//div[@id='main-content']//div[@id='details']//div[@id='title-area'])[1]")
