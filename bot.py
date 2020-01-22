import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
'''

ATAK:2
OBRONA:3
ROZGRYWANIE:4
KONDYCJA:5
CZYTANIE GRY:6
PRESSING:7
STALE FRAGMENTY:8
SKUTECZNOSC:9

'''
trening1=2
trening2=7
login = "login@gmail.com"
password = "password"

#doubleclicker gdy chcesz ulepszac dwie umiejetnosci na raz
def doubleclicker(a,b):
    count = 0
    while(1):
        text = driver.find_element_by_xpath(f"/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[{a}]/div[1]/div[2]/div[3]/div[2]/span[1]")
        text2 = driver.find_element_by_xpath(f"/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[{b}]/div[1]/div[2]/div[3]/div[2]/span[1]")
        how_much_wait = int(re.search(r'\d+', text.text).group())
        how_much_wait2 = int(re.search(r'\d+', text2.text).group())
        if how_much_wait2 > how_much_wait:
            how_much_wait = how_much_wait2
        
        print(f"Na koniec treningu 1 umiejetnosci trzeba czekac:{how_much_wait}")
        print(f"Na koniec treningu 2 umiejetnosci trzeba czekac:{how_much_wait2}")
        print(f"BOT wykonał już {count} treningow!")
        
        wheretomove =  driver.find_element_by_xpath(f"/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[{a}]")
        hover = ActionChains(driver).move_to_element(wheretomove)
        hover.perform()
        ele = driver.find_element_by_xpath(f"/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[{a}]/div[1]/div[2]/button[1]")
        ele.click()

        wheretomove =  driver.find_element_by_xpath(f"/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[{b}]")
        hover = ActionChains(driver).move_to_element(wheretomove)
        hover.perform()
        ele = driver.find_element_by_xpath(f"//div[{b}]//div[1]//div[2]//button[1]")
        ele.click()
        
        time.sleep(how_much_wait+2)
        count = count + 2
        #GDY WYWALA PRZEZ KOMuNIKATY UKONCZONEGO TRENINGU
        '''if count == 6:
            count = 0
            time.sleep(10)'''
    return

driver = webdriver.Chrome()
driver.get("https://footballteam.pl/")
ele = driver.find_elements_by_xpath("/html/body/main/section[1]/div/div[5]/div/button[1]")[0]
ele.click()
ele = driver.find_elements_by_xpath("/html/body/div[1]/div/div/div[1]/div[1]/h5")[0]
ele.click()
ele = driver.find_elements_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/form/div[1]/input")[0]
ele.send_keys(login)
ele = driver.find_elements_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/form/div[2]/input")[0]
ele.send_keys(password)
ele = driver.find_elements_by_xpath("//*[@id='btn-login']")[0]
ele.click()
time.sleep(5)
driver.get("https://game.footballteam.pl/training")
time.sleep(5)
how_much_wait = 0
#tutaj zmien argumenty
doubleclicker(trening1,trening2)

