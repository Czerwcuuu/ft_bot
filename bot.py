import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome()
driver.get("https://footballteam.pl/")
ele = driver.find_elements_by_xpath("/html/body/main/section[1]/div/div[5]/div/button[1]")[0]
ele.click()
ele = driver.find_elements_by_xpath("/html/body/div[1]/div/div/div[1]/div[1]/h5")[0]
ele.click()
ele = driver.find_elements_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/form/div[1]/input")[0]
ele.send_keys("login")
ele = driver.find_elements_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/form/div[2]/input")[0]
ele.send_keys("password")
ele = driver.find_elements_by_xpath("//*[@id='btn-login']")[0]
ele.click()
time.sleep(5)
driver.get("https://game.footballteam.pl/training")
time.sleep(5)
how_much_wait = 0
while(1):
    time.sleep(how_much_wait+3)
    text = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[5]/div[1]/div[2]/div[3]/div[2]/span[1]")
    how_much_wait = int(re.search(r'\d+', text.text).group())
    wheretomove =  driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]")
    hover = ActionChains(driver).move_to_element(wheretomove)
    hover.perform()
    ele = driver.find_elements_by_xpath("/html/body/div[1]/div/main/div/div/div[2]/div[1]/div[3]/div/div[2]/button")[0]
    ele.click()



