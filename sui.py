from typing import KeysView
import requests, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from termcolor import cprint
import pyperclip


def main(zero, ads_id, seed, password):
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

        
        driver.get('chrome-extension://mjifmheobamicmgkmdiiolilgebnbmpjijpehbao/ui.html')
        driver.switch_to.window(driver.window_handles[-1])
        
        try:
            # только беру и копирую адрес кошелька, если уже зареган. И пытаюсь получить тест токены

            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/form/label/input')))
            pyperclip.copy(password)
            driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/main/div/form/label/input').click()
            ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
            
            done_passBTN = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/main/div/form/button').click()
            time.sleep(5)
            addr1 = ''
            WebDriverWait(driver, 6).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/span/span/span')))
            copy_addr = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/main/div/span/span/i').click()  
            time.sleep(1)
            addr1 = pyperclip.paste()
            addr = ads_id + ":" + addr1 + "\n"
            cprint(addr)
            MyFile.write(addr) # add item to the list places.append(currentPlace)

           # Код для запроса тестовых токенов. Если вдруг кнопку убрали или перенесли, то закоментите или удалите
            
            try:
                WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div[4]/button')))
                want_tokens = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/main/div/div[4]/button').click()
                time.sleep(2)  
                
                
                driver.quit()
                requests.get(close_url)

                cprint(f'{zero+1}. {ads_id} = записал адрес, тест токен получил', 'green')
            except Exception as ex:
                driver.quit()
                requests.get(close_url)

                cprint(f'{zero+1}. {ads_id} = записал адрес', 'yellow')
            
            driver.quit()
            requests.get(close_url)

        except Exception as ex:

            # Если кошелек импортируем, то выполняется это условие

            WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div/div/div[2]/a')))
            driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div[2]/a').click()

            WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/a')))
            driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/a').click()

            pyperclip.copy(seed)
            WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/form/label/textarea')))
            phrase = driver.find_element(By.XPATH, '/html/body/div/div/div/form/label/textarea').click()
            ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
            driver.find_element(By.XPATH, '/html/body/div/div/div/form/div[2]/button').click()

            pyperclip.copy(password)
            WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/form/label[1]/input')))
            new_password = driver.find_element(By.XPATH, '/html/body/div/div/div/form/label[1]/input').click()
            ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
            pyperclip.copy(password)
            copy_password = driver.find_element(By.XPATH, '/html/body/div/div/div/form/label[2]/input').click()
            ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()


            nextBtn = driver.find_element(By.XPATH, '/html/body/div/div/div/form/div[2]/button[2]').click()

            WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/button')))
            succBtn = driver.find_element(By.XPATH, '/html/body/div/div/div/button').click()        

            time.sleep(5)
            addr1 = ''
            WebDriverWait(driver, 6).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/span/span/i')))
            
            copy_addr = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/main/div/span/span/i').click()  
            time.sleep(1)
            
            addr1 = pyperclip.paste()
            addr = ads_id + ":" + addr1 + "\n"
            cprint(addr)
            MyFile.write(addr) # add item to the list places.append(currentPlace)

            # Код для запроса тестовых токенов. Если вдруг кнопку убрали или перенесли, то закоментите или удалите
            
            try:  
                WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div[4]/button')))
                want_tokens = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/main/div/div[4]/button').click()
                time.sleep(2)  
                                
                driver.quit()
                requests.get(close_url)

                cprint(f'{zero+1}. {ads_id} = Зарегал, записал адрес, тест токен получил', 'green')
            except Exception as ex:
                driver.quit()
                requests.get(close_url)

                cprint(f'{zero+1}. {ads_id} = Зарегал, записал адрес', 'yellow')
            

with open("E:\Work\Crypto\dolphin-import-metamask-WIN\id_users.txt", "r") as f:
    id_users = [row.strip() for row in f]

with open("E:\Work\Crypto\dolphin-import-metamask-WIN\seeds.txt", "r") as f:
    seeds = [row.strip() for row in f]

MyFile = open("E:\Work\Crypto\dolphin-import-metamask-WIN\Addreses.txt", "w")


zero = -1
for ads_id in id_users:
    zero = zero + 1
    seed = seeds[zero]
    password = 'password123' # password for Sui
    
    main(zero, ads_id, seed, password)

