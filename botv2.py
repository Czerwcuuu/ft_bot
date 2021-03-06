from PyQt5.QtWidgets import QApplication, QWidget,QLabel,QGridLayout,QLineEdit,QPushButton,QHBoxLayout
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt, QThread
from PyQt5.QtGui import QIcon
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

class StartBotThread(QThread):

    def __init__(self,login,password,a,b):
        QThread.__init__(self)
        self.login = login
        self.password = password
        self.a = a
        self.b = b
        self.go = 0

    def __del__(self):
        self.wait()

    def stop(self):
        if self.go == 1:
            print("Moge")
            self.terminate()
            self.driver.quit()
        else:
            print("Nie moge")
            pass
        
    def run(self):
        self.driver = webdriver.Chrome()
        self.go =1
        self.driver.get("https://footballteam.pl/")
        ele = self.driver.find_elements_by_xpath("/html/body/main/section[1]/div/div[5]/div/button[1]")[0]
        ele.click()
        ele = self.driver.find_elements_by_xpath("/html/body/div[1]/div/div/div[1]/div[1]/h5")[0]
        ele.click()
        ele = self.driver.find_elements_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/form/div[1]/input")[0]
        ele.send_keys(self.login)
        ele = self.driver.find_elements_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/form/div[2]/input")[0]
        ele.send_keys(self.password)
        ele = self.driver.find_elements_by_xpath("//*[@id='btn-login']")[0]
        ele.click()
        time.sleep(5)
        self.driver.get("https://game.footballteam.pl/training")
        time.sleep(5)
        how_much_wait = 0
        count = 0
        while 1:
            try:
                finallmoney = "";
                money = self.driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/header[1]/div[2]/ul[1]/li[3]/p[1]")
                text = self.driver.find_element_by_xpath(f"/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[{self.a}]/div[1]/div[2]/div[3]/div[2]/span[1]")
                text2 = self.driver.find_element_by_xpath(f"/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[{self.b}]/div[1]/div[2]/div[3]/div[2]/span[1]")
                cost1 = self.driver.find_element_by_xpath(f"//div[{self.a}]//div[1]//div[2]//div[3]//div[1]//span[1]")
                cost2 = self.driver.find_element_by_xpath(f"//div[{self.b}]//div[1]//div[2]//div[3]//div[1]//span[1]")
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
                
                wheretomove =  self.driver.find_element_by_xpath(f"/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[{self.a}]")
                hover = ActionChains(self.driver).move_to_element(wheretomove)
                hover.perform()
                ele = self.driver.find_element_by_xpath(f"/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[{self.a}]/div[1]/div[2]/button[1]")
                ele.click()

                wheretomove =  self.driver.find_element_by_xpath(f"/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[{self.b}]")
                hover = ActionChains(self.driver).move_to_element(wheretomove)
                hover.perform()
                ele = self.driver.find_element_by_xpath(f"//div[{self.b}]//div[1]//div[2]//button[1]")
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

class Bot(QWidget):

    def __init__(self,parent=None):
        super().__init__(parent)
        self.interfejs()
        self.running = False
        self.a = 2
        self.b = 3
        self.login = "email@mail.com" #Tu wpisz wybrany login
        self.password = "password"    #Tu wpisz wybrany haslo
        self.StartBotThread=StartBotThread(self.login,self.password,self.a,self.b)
        

    def interfejs(self):
        #etykiety
        et_FT = QLabel("<b>FOOTBALLTEAM BOT 1.5<b>",self)
        et_trening = QLabel("TRENUJESZ:",self)
        atakTxt = QLabel("<b>ATAK<b> - 2:",self)
        obronaTxt = QLabel("<b>OBRONA<b> - 3:",self)
        rogrywanieTxt = QLabel("<b>ROZGRYWANIE<b> - 4:",self)
        kondycjaTxt = QLabel("<b>KONDYCJA<b> - 5:",self)
        czytaniegryTxt = QLabel("<b>CZYTANIE GRY<b> - 6:",self)
        pressingTxt = QLabel("<b>PRESSING<b> - 7:",self)
        stalefragmentyTxt = QLabel("<b>STALE FRAGMENTY<b> - 8:",self)
        skutecznoscTxt = QLabel("<b>SKUTECZNOSC<b> - 9:",self)

        #uklad tabelaryczny
        ukladT = QGridLayout()
        ukladT.addWidget(et_FT,0,0)
        ukladT.addWidget(et_trening,2,0)
        self.aktualnie_trenowane = QLineEdit()
        self.aktualnie_trenowane2 = QLineEdit()
        self.login_TB = QLineEdit()
        self.password_TB = QLineEdit()

        ukladT.addWidget(self.login_TB,1,0)
        ukladT.addWidget(self.password_TB,1,1)
        
        ukladT.addWidget(atakTxt,3,0,1,3)
        ukladT.addWidget(obronaTxt,4,0,1,3)
        ukladT.addWidget(rogrywanieTxt,5,0,1,3)
        ukladT.addWidget(kondycjaTxt,6,0,1,3)
        ukladT.addWidget(czytaniegryTxt,7,0,1,3)
        ukladT.addWidget(pressingTxt,8,0,1,3)
        ukladT.addWidget(stalefragmentyTxt,9,0,1,3)
        ukladT.addWidget(skutecznoscTxt,10,0,1,3)

        ukladT.addWidget(self.aktualnie_trenowane,11,0)
        ukladT.addWidget(self.aktualnie_trenowane2,11,1)

        startBtn = QPushButton("&START",self)
        stopBtn = QPushButton("&STOP",self)
        exitBtn = QPushButton("&WYJSCIE",self)

        ukladH1 = QHBoxLayout()
        ukladH1.addWidget(startBtn)
        ukladH1.addWidget(stopBtn)

        ukladT.addLayout(ukladH1,12,0,1,3)
        ukladT.addWidget(exitBtn,13,0,1,3)

        self.setLayout(ukladT)

        exitBtn.clicked.connect(self.koniec)
        startBtn.clicked.connect(self.wybor)
        stopBtn.clicked.connect(self.stop_btn)

        self.setGeometry(20,20,300,100)
        self.setWindowTitle("Football Team Bot")
        self.show()

    def koniec(self):
        self.StartBotThread.stop()
        self.close()

    def wybor(self):
        if self.running == 0:
            self.login = self.login_TB.text()
            self.password = self.password_TB.text()
            self.StartBotThread = StartBotThread(self.login,self.password,self.a,self.b)
            nadawca = self.sender()
            try:
                if nadawca.text() == "&START":
                    if int(self.aktualnie_trenowane.text())>1 and int(self.aktualnie_trenowane.text()) < 10 and int(self.aktualnie_trenowane2.text()) < 10 and int(self.aktualnie_trenowane2.text()) > 1:
                        self.a = int(self.aktualnie_trenowane.text())
                        self.b = int(self.aktualnie_trenowane2.text())
                        self.running = 1
                        self.StartBotThread.start()
                    else:
                        print("Nie ma takiej opcji")
            except ValueError:
                print("Zla wartosc")
        else:
            print("Maksymalnie mozesz miec wlaczony jeden bot")

    def stop_btn(self):
        print("Jesteeem")
        self.StartBotThread.stop()
        self.running = 0
        
        
        
if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = Bot()
    sys.exit(app.exec_())
        

        
        
        
