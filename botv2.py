from PyQt5.QtWidgets import QApplication, QWidget,QLabel,QGridLayout,QLineEdit,QPushButton,QHBoxLayout
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class Bot(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.interfejs()

        self.trening1 = 2
        self.trening2 = 3

    def interfejs(self):
        #etykiety
        et_FT = QLabel("<b>FOOTBALLTEAM BOT 1.5<b>",self)
        et_trening = QLabel("TRENUJESZ:",self)

        #uklad tabelaryczny
        ukladT = QGridLayout()
        ukladT.addWidget(et_FT,0,0)
        ukladT.addWidget(et_trening,1,0)

        #pola edycyjne
        self.aktualnie_trenowane = QLineEdit()
        self.aktualnie_trenowane2 = QLineEdit()
        self.aktualnie_trenowane.readonly = True
        self.aktualnie_trenowane.readonly = True

        #pola edycyjne do ukladu tabelarczynego
        ukladT.addWidget(self.aktualnie_trenowane,2,0)
        ukladT.addWidget(self.aktualnie_trenowane2,2,1)

        #guziki
        atakBtn = QPushButton("&ATAK",self)
        obronaBtn = QPushButton("&OBRONA",self)
        rozgrywanieBtn = QPushButton("&ROZGRYWANIE",self)
        kondycjaBtn = QPushButton("&KONDYCJA",self)
        czytanie_gryBtn = QPushButton("&CZYTANIE GRY",self)
        pressingBtn = QPushButton("&PRESSING",self)
        stale_fragmentyBtn = QPushButton("&STALE FRAGMENTY",self)
        skutecznoscBtn = QPushButton("&SKUTECZNOSC",self)
        startBtn = QPushButton("&START",self)
        stopBtn = QPushButton("&STOP",self)
        exitBtn = QPushButton("&WYJSCIE",self)

        ukladH1 = QHBoxLayout()
        ukladH1.addWidget(atakBtn)
        ukladH1.addWidget(obronaBtn)
        ukladH1.addWidget(rozgrywanieBtn)
        ukladH1.addWidget(kondycjaBtn)

        ukladH2 = QHBoxLayout()
        ukladH2.addWidget(czytanie_gryBtn)
        ukladH2.addWidget(pressingBtn)
        ukladH2.addWidget(stale_fragmentyBtn)
        ukladH2.addWidget(skutecznoscBtn)

        ukladT.addLayout(ukladH1,3,0,1,3)
        ukladT.addLayout(ukladH2,4,0,1,3)
        ukladT.addWidget(startBtn,5,0,1,1)
        ukladT.addWidget(stopBtn,5,1,1,2)
        ukladT.addWidget(exitBtn,6,0,1,3)

        self.setLayout(ukladT)

        exitBtn.clicked.connect(self.koniec)
        atakBtn.clicked.connect(self.wybor)
        obronaBtn.clicked.connect(self.wybor)
        rozgrywanieBtn.clicked.connect(self.wybor)
        kondycjaBtn.clicked.connect(self.wybor)
        czytanie_gryBtn.clicked.connect(self.wybor)
        pressingBtn.clicked.connect(self.wybor)
        stale_fragmentyBtn.clicked.connect(self.wybor)
        skutecznoscBtn.clicked.connect(self.wybor)


        self.setGeometry(20,20,300,100)
        self.setWindowTitle("Football Team Bot")
        self.show()

    def koniec(self):
        self.close()

    def wybor(self):
        nadawca = self.sender()

        if nadawca.text() == "&ATAK":
            self.trening1 = 2
            self.aktualnie_trenowane.setText(str(self.trening1))
        if nadawca.text() == "&OBRONA":
            self.trening1 = 3
            self.aktualnie_trenowane.setText(str(self.trening1))
        if nadawca.text() == "&ROZGRYWANIE":
            self.trening1 = 4
            self.aktualnie_trenowane.setText(str(self.trening1))
        if nadawca.text() == "&KONDYCJA":
            self.trening1 = 5
            self.aktualnie_trenowane.setText(str(self.trening1))
        if nadawca.text() == "&CZYTANIE GRY":
            self.trening1 = 6
            self.aktualnie_trenowane.setText(str(self.trening1))
        if nadawca.text() == "&PRESSING":
            self.trening1 = 7
            self.aktualnie_trenowane.setText(str(self.trening1))
        if nadawca.text() == "&STALE FRAGMENTY":
            self.trening1 = 8
            self.aktualnie_trenowane.setText(str(self.trening1))
        if nadawca.text() == "&SKUTECZNOSC":
            self.trening1 = 9
            self.aktualnie_trenowane.setText(str(self.trening1))
        
        
if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = Bot()
    sys.exit(app.exec_())
        
        
        
        
