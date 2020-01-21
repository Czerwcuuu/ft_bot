import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
'''
W clickerze, są 3 linijki zaczynajace sie :text,wheretomove,ele - podmien je kopiujac i wklejajac te ponizej, jezeli chcesz rozwijac dana
umiejetnosc.
Dodatkowo musisz wprowadzic swoj login i haslo w miejscu "login" i "password"

ATAK
text = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[3]/div[2]/span[1]")
wheretomove =  driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]")
ele = driver.find_element_by_xpath("//div[@class='training']//div[2]//div[1]//div[2]//button[1]")

OBRONA
text = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[2]/div[3]/div[2]/span[1]")
wheretomove =  driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]")
ele = driver.find_element_by_xpath("//div[3]//div[1]//div[2]//button[1]")

ROZGRYWANIE
text = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[2]/div[3]/div[2]/span[1]")
wheretomove =  driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[4]")
ele = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[2]/button[1]")

KONDYCJA
text = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[5]/div[1]/div[2]/div[3]/div[2]/span[1]")
wheretomove =  driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[5]")
ele = driver.find_element_by_xpath("//div[5]//div[1]//div[2]//button[1]")

CZYTANIE GRY
text = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[6]/div[1]/div[2]/div[3]/div[2]/span[1]")
wheretomove =  driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[6]")
ele = driver.find_element_by_xpath("//div[6]//div[1]//div[2]//button[1]")

PRESSING
text = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[7]/div[1]/div[2]/div[3]/div[2]/span[1]")
wheretomove =  driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[7]")
ele = driver.find_element_by_xpath("//div[7]//div[1]//div[2]//button[1]")

STALE FRAGMENTY
text = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[8]/div[1]/div[2]/div[3]/div[2]/span[1]")
wheretomove =  driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[8]")
ele = driver.find_element_by_xpath("//div[8]//div[1]//div[2]//button[1]")

SKUTECZNOSC
text = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[9]/div[1]/div[2]/div[3]/div[2]/span[1]")
wheretomove =  driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[9]")
ele = driver.find_element_by_xpath("//div[9]//div[1]//div[2]//button[1]")

'''
#clicker, gdy chcesz ulepszac tylko jedna umiejetnosc
'''
def clicker():
    count = 0
    while(1):
        text = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[8]/div[1]/div[2]/div[3]/div[2]/span[1]")
        how_much_wait = int(re.search(r'\d+', text.text).group())
        print(how_much_wait)
        print(count)
        wheretomove =  driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[8]")
        hover = ActionChains(driver).move_to_element(wheretomove)
        hover.perform()
        ele = driver.find_element_by_xpath("//div[8]//div[1]//div[2]//button[1]")
        ele.click()
        time.sleep(how_much_wait+2)
        count = count + 1
        #GDY WYWALA PRZEZ KOMuNIKATY UKONCZONEGO TRENINGU
        if count == 6:
            count = 0
            time.sleep(10)
    return'''
#doubleclicker gdy chcesz ulepszac dwie umiejetnosci na raz
def doubleclicker():
    count = 0
    while(1):
        text = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[2]/div[3]/div[2]/span[1]")
        text2 = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[2]/div[3]/div[2]/span[1]")
        how_much_wait = int(re.search(r'\d+', text.text).group())
        how_much_wait2 = int(re.search(r'\d+', text2.text).group())
        if how_much_wait2 > how_much_wait:
            how_much_wait = how_much_wait2
        
        print(how_much_wait)
        print(how_much_wait2)
        print(count)
        
        wheretomove =  driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[4]")
        hover = ActionChains(driver).move_to_element(wheretomove)
        hover.perform()
        ele = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[2]/button[1]")
        ele.click()

        wheretomove =  driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[3]")
        hover = ActionChains(driver).move_to_element(wheretomove)
        hover.perform()
        ele = driver.find_element_by_xpath("//div[3]//div[1]//div[2]//button[1]")
        ele.click()
        
        time.sleep(how_much_wait+2)
        count = count + 1
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
ele.send_keys("login@gmail.com")
ele = driver.find_elements_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/form/div[2]/input")[0]
ele.send_keys("password")
ele = driver.find_elements_by_xpath("//*[@id='btn-login']")[0]
ele.click()
time.sleep(5)
driver.get("https://game.footballteam.pl/training")
time.sleep(5)
how_much_wait = 0
doubleclicker()

