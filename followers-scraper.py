from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
import time
import os
import datetime
from webdriver_manager.chrome import ChromeDriverManager

count = 100  # number of profiles you want to get
account = "therock"  # account from
page = "followers"  # from following or followers

yourusername = "*********" #your IG username
yourpassword = "*********"  #your IG password


#for proxy i recommend 4G mobile proxy: http://www.virtnumber.com/mobile-proxy-4g.php
#PROXY = "http://84.52.54.2:8011" # IP:PORT or HOST:PORT
#options.add_argument('--proxy-server=%s' % PROXY)

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--user-agent="Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16D57"')

driver = webdriver.Chrome(ChromeDriverManager().install())


driver.get('https://www.instagram.com/accounts/login/')
sleep(3)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Accept')]"))).click()
sleep(1)
username_input = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
password_input = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
username_input.send_keys(yourusername)
password_input.send_keys(yourpassword)
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Not Now')]"))).click()
sleep(3)
          
driver.get('https://www.instagram.com/%s' % account)
sleep(2) 
driver.find_element(By.XPATH, '//a[contains(@href, "%s")]' % page).click()
scr2 = driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
sleep(2)
text1 = scr2.text
print(text1)
x = datetime.datetime.now()
print(x)

for i in range(1,count):
          if page == "followers":
                    scr1 = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]/ul/div/li[%s]' % i)
          elif page == "following":
                    scr1 = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div[3]/ul/div/li[%s]' % i)
          else:
                    print("Var page ERROR")   
                    
          driver.execute_script("arguments[0].scrollIntoView();", scr1)
          sleep(1)
          text = scr1.text
          list = text.encode('utf-8').split()
          dirname = os.path.dirname(os.path.abspath(__file__))
          csvfilename = os.path.join(dirname, account + "-" + page + ".txt")
          file_exists = os.path.isfile(csvfilename)
          f = open(csvfilename,'a')
          f.write(str(list[0]) + "\r\n")
          f.close()
          print('{};{}'.format(i, list[0]))
          #print(i + ";" + list[0])
          if i == (count-1):
                    print(x)
