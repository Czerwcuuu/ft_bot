import time
import re
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import InvalidElementStateException,ElementClickInterceptedException,NoSuchElementException

#USTAWIENIA ====================================================================
trening1=6 #Tu wpisz wybrany trening1
trening2=3 #Tu wpisz wybrany trening2
login = "fortepiany9@interia.pl" #Tu wpisz wybrany login
password = "aiqu4voh123"    #Tu wpisz wybrany haslo
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
#USTAWIENIA ====================================================================

#doubleclicker gdy chcesz ulepszac dwie umiejetnosci na raz
def doubleclicker(a,b):
    count = 0
    while(1):
        try:
            finallmoney = "";
            money = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/header[1]/div[2]/ul[1]/li[3]/p[1]")
            text = driver.find_element_by_xpath(f"/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[{a}]/div[1]/div[2]/div[3]/div[2]/span[1]")
            text2 = driver.find_element_by_xpath(f"/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[{b}]/div[1]/div[2]/div[3]/div[2]/span[1]")
            cost1 = driver.find_element_by_xpath(f"//div[{a}]//div[1]//div[2]//div[3]//div[1]//span[1]")
            cost2 = driver.find_element_by_xpath(f"//div[{b}]//div[1]//div[2]//div[3]//div[1]//span[1]")
            how_much_wait = int(re.search(r'\d+', text.text).group())
            how_much_wait2 = int(re.search(r'\d+', text2.text).group())
            price1=int(re.search(r'\d+', cost1.text).group())
            price2=int(re.search(r'\d+', cost2.text).group())
            money = re.findall(r'\d+', money.text)
            for x in money:
                finallmoney +=x
            money = int(finallmoney)
            print(f"Na koniec treningu 1 umiejetnosci trzeba czekac:{how_much_wait}, cena treningu:{price1}")
            print(f"Na koniec treningu 2 umiejetnosci trzeba czekac:{how_much_wait2}, cena treningu:{price2}")
            if price2 > price1:
                price1 = price2
            if how_much_wait2 > how_much_wait:
                how_much_wait = how_much_wait2
            if price1>money:
                print("Koniec pieniedzy na koncie w grze, koncze dzialanie bota")
                sys.exit(0)
            print(f"Ilosc pieniedzy na koncie:{money}")
            count = count + 2
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
        except InvalidElementStateException as e:
            print("===BOT nie moze wcisnac guzika! Ponizej wiecej szczegolow!===")
            print(e)
        except NoSuchElementException as e:
            print("===BOT nie moze znalezc guzika! Ponizej wiecej info!===")
            print(e)
        except ElementClickInterceptedException as e:
            print("===BOT nie moze wcisnac guzika, poniewaz jest czyms zakryty!===")
            print(e)
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
doubleclicker(trening1,trening2)

