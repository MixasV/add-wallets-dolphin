from typing import KeysView
import requests, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from termcolor import cprint
import pyperclip


def main(zero, ads_id, seed, password):
    try:
        # http://localhost:3001/v1.0/browser_profiles/PROFILE_ID/start?automation=1
        open_url = "http://localhost:3001/v1.0/browser_profiles/" + ads_id + "/start?automation=1"
        close_url = "http://localhost:3001/v1.0/browser_profiles/" + ads_id + "/stop"        

        resp = requests.get(open_url).json()

        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        debuggerAddress = "127.0.0.1:" + str(resp["automation"]["port"])
        chrome_options.add_experimental_option("debuggerAddress", debuggerAddress)
        #Change chrome driver path accordingly
        #chrome_driver = "C:\chromedriver.exe"
        chrome_driver = "E:\Work\Crypto\Abuse-pack-main\chromedriver.exe"
        driver = webdriver.Chrome(chrome_driver, options=chrome_options)


        driver.get('chrome-extension://dknmkicibefebojkkmnaoookdpnikcmlffamfkoe/popup.html#/register')
        driver.switch_to.window(driver.window_handles[-1])
        wait_elem = WebDriverWait(driver, 12).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[3]/button[3]')))
        get_started = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/button[3]').click()
        # wait_elem = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@class="button btn--rounded btn-secondary page-container__footer-button"]')))
        # get_started2 = driver.find_element(By.XPATH, '//*[@class="button btn--rounded btn-secondary page-container__footer-button"]').click()        
        # wait_elem = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@class="button btn--rounded btn-primary first-time-flow__button"]')))
        # import_wallet = driver.find_element(By.XPATH, '//*[@class="button btn--rounded btn-primary first-time-flow__button"]').click()
        
        
        wait_elem = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[3]/div/form/div[1]/div[1]/div[2]/div/input')))
        pyperclip.copy(seed)
        phrase = driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div/form/div[1]/div[1]/div[2]/div/input').click()
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

       
        pyperclip.copy(accName)
        acc_name = driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div/form/div[2]/div[1]/div/input').click()
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

        
        pyperclip.copy(password)
        new_password = driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div/form/div[2]/div[2]/div/input').click()
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

        password_confirm = driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div/form/div[2]/div[3]/div/input').click()
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
        nextBtn = driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div/form/div[2]/button[2]').click()



        wait_elem = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[4]/button')))
        done_import = driver.find_element(By.XPATH, '/html/body/div/div/div[4]/button').click()

      
        driver.quit()
        requests.get(close_url)

        cprint(f'{zero+1}. {ads_id} = done', 'green')

    except Exception as ex:
        cprint(f'{zero+1}. {ads_id} = already done', 'yellow')
        driver.quit()
        requests.get(close_url)


with open("E:\Work\Crypto\dolphin-import-metamask-WIN\id_users.txt", "r") as f:
    id_users = [row.strip() for row in f]

with open("E:\Work\Crypto\dolphin-import-metamask-WIN\seeds.txt", "r") as f:
    seeds = [row.strip() for row in f]
        

zero = -1
for ads_id in id_users:
    zero = zero + 1
    seed = seeds[zero]
    accName = 'Your name'
    password = 'Password' # password for metamask
    
    main(zero, ads_id, seed, password)

