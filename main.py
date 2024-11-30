import random
import sys
import zipfile
from PySide6 import QtWidgets, QtGui, QtCore
import os
import ctypes
import requests
from datetime import datetime
import easygui

def fajltorles():
    if os.path.exists("myDiscord.zip"):
        os.remove("myDiscord.zip")


def unzip():
    try:
        with zipfile.ZipFile("myDiscord.zip", "r") as zip_ref:
            zip_ref.extractall(f"C:/Users/{os.getlogin()}/Appdata/Roaming")
    except zipfile.BadZipfile:
        ctypes.windll.user32.MessageBoxW(0, "Nem sikerült letölteni a myDiscordhoz szükséges fájlokat", "Hiba")


if not os.path.exists(f"C:/Users/{os.getlogin()}/Appdata/Roaming/myDiscord"):
    r = requests.get("https://c4227fda-4573-4d08-bf3b-07835e0f2723.filesusr.com/archives"
                     "/f7dbe2_3d979411e5f445b48c5554e7b12ce4be.zip?dn=myDiscord.zip")
    f = open("myDiscord.zip", "wb")
    f.write(r.content)
    f.close()
    unzip()
    fajltorles()

skiplogin = False

class Beallitasok(QtWidgets.QWidget):

    def usnchange(self):
        try:
            mappakszama = (len(next(os.walk(f"C:/Users/{os.getlogin()}/Appdata/Roaming/myDiscord/Users"))[1]))
        except StopIteration:
            mappakszama = 0

        jelenlegi = easygui.enterbox("Add meg a jelenlegi felhasználóneved:")

        for x in range(mappakszama):
            fj = open(f"C:/Users/{os.getlogin()}/Appdata/Roaming/myDiscord/Users/USER_0{x}/userdata.txt", "r")
            sorok = fj.readlines()
            usn = sorok[0][4:]
            nums = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58, 61, 64, 67, 70]
            username = ""
            y = 0
            while y != len(usn):
                if y in nums:
                    username += usn[y]
                y += 1
            username = username[::-1].replace("\n", "")
            fj.close()

            print(username)
            print(jelenlegi)

            if username == jelenlegi:
                ujfhn = easygui.enterbox("Add meg az új felhasználóneved:")
                usnlist = list(ujfhn)
                encstr = usnlist[::-1]
                fl_encstr = str(random.randint(0, 9))
                spccharlist = ["#", "?", "!", ".", "/", "="]
                fl = open(f"C:/Users/{os.getlogin()}/Appdata/Roaming/myDiscord/Users/USER_0{x}/userdata.txt", "r")
                flsorok = fl.readlines()
                full_encpss = flsorok[1].replace("\n", "")[5:]
                for i in encstr:
                    fl_encstr += i + str(random.randint(0, 9)) + random.choice(spccharlist)
                fl.close()
                fajl = open(f"C:/Users/{os.getlogin()}/Appdata/Roaming/myDiscord/Users/USER_0{x}/userdata.txt", "w")
                fajl.write(f"usn:{fl_encstr}\npass:{full_encpss}")
                fajl.close()

                if skiplogin:
                    sf = open(f"C:/Users/{os.getlogin()}/Appdata/Roaming/myDiscord/Settings/settings.txt", "w")
                    sf.write(f"skiplogin: 1\nuser: {ujfhn}")
                    sf.close()

                ctypes.windll.user32.MessageBoxW(0, "Az új felhasználónév életbe lépéséhez újra kell indítani a programot!", "Újraindítás szükséges")

    def __init__(self):
        super().__init__()

        self.mainvbox = QtWidgets.QVBoxLayout(self)

        self.felso_menusor_hbox = QtWidgets.QHBoxLayout(self)
        self.felso_menusor_hbox.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        self.felh_beall_gomb = QtWidgets.QPushButton("Felhasználói beállítások")
        self.felh_beall_gomb.setStyleSheet("background-color: white")
        self.felh_beall_gomb.setFont(QtGui.QFont(betutipus_csalad[0], 12))


        ############################### FELHASZNÁLÓI BEÁLLÍTÁSOK MENÜPONTJAI ###############################

        self.felh_beall_vbox = QtWidgets.QVBoxLayout(self)

        self.change_usnm_hbox = QtWidgets.QHBoxLayout(self)

        self.change_usnm_lbl = QtWidgets.QLabel("Felhasználónév megváltoztatása:")
        self.change_usnm_lbl.setFont(QtGui.QFont(betutipus_csalad[0], 12))
        self.change_usnm_lbl.setStyleSheet("color: white")

        self.change_usnm_btn = QtWidgets.QPushButton("Megváltoztatás")
        self.change_usnm_btn.setFont(QtGui.QFont(betutipus_csalad[0], 12))
        self.change_usnm_btn.setStyleSheet("background-color: white")
        self.change_usnm_btn.clicked.connect(self.usnchange)

        self.kijelentkezesgomb = QtWidgets.QPushButton("Kijelentkezés")
        self.kijelentkezesgomb.setStyleSheet("background-color: red; color: white")
        self.kijelentkezesgomb.setFont(QtGui.QFont(betutipus_csalad[0], 12))

        self.mainvbox.addLayout(self.felso_menusor_hbox)
        self.felso_menusor_hbox.addWidget(self.felh_beall_gomb)
        self.mainvbox.addLayout(self.felh_beall_vbox)
        self.felh_beall_vbox.addLayout(self.change_usnm_hbox)
        self.change_usnm_hbox.addWidget(self.change_usnm_lbl)
        self.change_usnm_hbox.addWidget(self.change_usnm_btn)
        self.felh_beall_vbox.addWidget(self.kijelentkezesgomb)

        self.setWindowTitle("Beállítások")
        self.setStyleSheet("background-color: #292929")
        self.resize(500, 500)
        self.show()

class Main(QtWidgets.QWidget):

    def konfigablak(self):
        if self.b is None:
            self.b = Beallitasok()
        self.b.show()

    def kuldes(self):
        global user
        now = datetime.now()
        dt_string = now.strftime("%Y.%m.%d. %H:%M:%S")
        uzenet = QtWidgets.QLabel()
        uzenet.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        uzenet.setStyleSheet("color: white")
        uzenet.setFont(QtGui.QFont(betutipus_csalad[0], 12))
        try:
            uzenet.setText(f"{user} ({dt_string}):\n{self.uzenetinput.text()}")
        except NameError:
            f = open(f"C:/Users/{os.getlogin()}/Appdata/Roaming/myDiscord/Settings/settings.txt", "r")
            sorok = f.readlines()
            susn = sorok[1]
            susn = susn[5:]
            user = susn.replace("\n", "")
            uzenet.setText(f"{user} ({dt_string}):\n{self.uzenetinput.text()}")
            f.close()
        self.uzenetlyt.addWidget(uzenet)
        self.uzenetinput.setText("")

    def __init__(self):
        super().__init__()

        scroll_area = QtWidgets.QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

        central_widget = QtWidgets.QWidget()
        central_widget.setStyleSheet("background-color: #292929")
        scroll_area.setWidget(central_widget)

        self.setStyleSheet("background-color: #292929")
        self.resize(ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))

        self.uzenetlyt = QtWidgets.QVBoxLayout(central_widget)
        self.uzenetlyt.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom)

        self.left_layout = QtWidgets.QVBoxLayout()
        self.left_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        self.settingsgomb = QtWidgets.QPushButton(f"Beállítások")
        self.settingsgomb.setStyleSheet("color: white; background-color: #444444;")
        self.settingsgomb.setFont(QtGui.QFont(betutipus_csalad[0], 12))
        self.settingsgomb.clicked.connect(self.konfigablak)


        self.left_layout.addWidget(self.settingsgomb)

        self.hbox_main = QtWidgets.QHBoxLayout()

        right_layout = QtWidgets.QVBoxLayout()

        right_layout.addWidget(scroll_area)

        self.uzenetinput = QtWidgets.QLineEdit()
        self.uzenetinput.setPlaceholderText("Írd be az üzenetet...")
        self.uzenetinput.setFont(QtGui.QFont(betutipus_csalad[0], 12))
        self.uzenetinput.setStyleSheet("color: white")

        self.kuldesgomb = QtWidgets.QPushButton("Küldés")
        self.kuldesgomb.setStyleSheet("QPushButton{background-color: white;} QPushButton:hover{background-color: red}")
        self.kuldesgomb.setFont(QtGui.QFont(betutipus_csalad[0], 12))
        self.kuldesgomb.clicked.connect(self.kuldes)

        self.hbox_input = QtWidgets.QHBoxLayout()
        self.hbox_input.addWidget(self.uzenetinput)
        self.hbox_input.addWidget(self.kuldesgomb)

        right_layout.addLayout(self.hbox_input)

        self.hbox_main.addLayout(self.left_layout)
        self.hbox_main.addLayout(right_layout)

        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.main_layout.addLayout(self.hbox_main)

        self.setLayout(self.main_layout)
        self.setWindowTitle("myDiscord")
        self.show()

        self.b = None

    def keyPressEvent(self, event):
        if event.key() in (QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter):  # valamiért unresolved reference, de működik
            self.kuldes()

class Bejelentkezes(QtWidgets.QWidget):

    def foablak(self):
        if self.m is None:
            self.m = Main()
        self.m.show()

    def adatcheck(self):
        global user

        beirt_fhnev = self.fhnevinput2.text()
        beirt_jszo = self.jszoinput2.text()

        if self.checkbox.isChecked():
            global skiplogin
            skiplogin = True

            os.makedirs(os.path.dirname(f"C:/Users/{os.getlogin()}/Appdata/Roaming/myDiscord/Settings/settings.txt"),
                        exist_ok=True)
            f = open(f"C:/Users/{os.getlogin()}/Appdata/Roaming/myDiscord/Settings/settings.txt", "w")
            f.write(f"skiplogin: 1\nuser: {beirt_fhnev}")
            f.close()

        sikeres = False

        mappakszama = (len(next(os.walk(f"C:/Users/{os.getlogin()}/Appdata/Roaming/myDiscord/Users"))[1]))

        for x in range(mappakszama):
            fj = open(f"C:/Users/{os.getlogin()}/Appdata/Roaming/myDiscord/Users/USER_0{x}/userdata.txt", "r")
            sorok = fj.readlines()
            usn = sorok[0]
            jsz = sorok[1]
            jjsz = jsz[5:]
            jusn = usn[4:]
            nums = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58, 61, 64, 67, 70]
            uname = ""
            pword = ""
            x = 0
            while x != len(jusn):
                if x in nums:
                    uname += jusn[x]
                x += 1
            y = 0
            while y != len(jjsz):
                if y in nums:
                    pword += jjsz[y]
                y += 1
            runame = uname[::-1]
            runame = runame.replace("\n", "")
            rpword = pword[::-1]
            rpword = rpword.replace("\n", "")
            if runame == beirt_fhnev and rpword == beirt_jszo:
                user = beirt_fhnev
                self.foablak()
                self.loginfeedbacklbl.setText("Sikeres bejelentkezés!")
                self.elrendezes.addWidget(self.loginfeedbacklbl)
                sikeres = True
                self.close()
            else:
                if not sikeres:
                    self.loginfeedbacklbl.setText(
                        "Sikertelen bejelentkezés!\nA felhasználónév vagy a jelszó nem egyezik!")
                    self.elrendezes.addWidget(self.loginfeedbacklbl)

    def __init__(self):
        super().__init__()

        self.m = None

        self.setStyleSheet("background-color: #292929")

        self.elrendezes = QtWidgets.QVBoxLayout(self)
        self.elrendezes.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.logolabel = QtWidgets.QLabel()
        self.pxmp = QtGui.QPixmap(f"C:/Users/{os.getlogin()}/Appdata/Roaming/myDiscord/Images/logo2.png")
        self.pxmp = self.pxmp.scaled(150, 150, aspectMode=QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.logolabel.setPixmap(self.pxmp)
        self.logolabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.reglabel = QtWidgets.QLabel("Bejelentkezés")
        self.reglabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.reglabel.setFont(QtGui.QFont(betutipus_csalad[0], 22))
        self.reglabel.setStyleSheet("color: white; margin-bottom: 20px")

        self.fhnevlabel = QtWidgets.QLabel("Felhasználónév:")
        self.fhnevlabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.fhnevlabel.setFont(QtGui.QFont(betutipus_csalad[0], 14))
        self.fhnevlabel.setStyleSheet("color: white")

        self.fhnevinput2 = QtWidgets.QLineEdit()
        self.fhnevinput2.setFixedWidth(250)
        self.fhnevinput2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.fhnevinput2.setStyleSheet("margin-bottom: 20px; color: white")

        self.jszolabel = QtWidgets.QLabel("Jelszó:")
        self.jszolabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.jszolabel.setFont(QtGui.QFont(betutipus_csalad[0], 14))
        self.jszolabel.setStyleSheet("color: white")

        self.jszoinput2 = QtWidgets.QLineEdit()
        self.jszoinput2.setFixedWidth(250)
        self.jszoinput2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.jszoinput2.setStyleSheet("margin-bottom: 30px; color: white")

        self.logingomb = QtWidgets.QPushButton("Bejelentkezés")
        self.logingomb.setStyleSheet("QPushButton{background-color: white;} QPushButton:hover{background-color: red}")
        self.logingomb.setFont(QtGui.QFont(betutipus_csalad[0], 12))
        self.logingomb.setFixedWidth(150)
        self.logingomb.clicked.connect(self.adatcheck)

        self.skloginlbl = QtWidgets.QLabel("Bejelentkezve maradok")
        self.skloginlbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.skloginlbl.setFont(QtGui.QFont(betutipus_csalad[0], 10))
        self.skloginlbl.setStyleSheet("color: white")
        self.checkbox = QtWidgets.QCheckBox()

        self.elrendezes.addWidget(self.logolabel)
        self.elrendezes.addWidget(self.reglabel)
        self.elrendezes.addWidget(self.fhnevlabel)
        self.layout2 = QtWidgets.QGridLayout()
        self.elrendezes.addLayout(self.layout2)
        self.layout2.addWidget(self.fhnevinput2)
        self.elrendezes.addWidget(self.jszolabel)
        self.layout3 = QtWidgets.QGridLayout()
        self.layout4 = QtWidgets.QHBoxLayout()
        self.elrendezes.addLayout(self.layout3)
        self.layout3.addWidget(self.jszoinput2)
        self.elrendezes.addLayout(self.layout4)
        self.layout4.addWidget(self.logingomb)
        self.layout5 = QtWidgets.QHBoxLayout()
        self.layout5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.elrendezes.addLayout(self.layout5)
        self.layout5.addWidget(self.skloginlbl)
        self.layout5.addWidget(self.checkbox)

        self.loginfeedbacklbl = QtWidgets.QLabel("")
        self.loginfeedbacklbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.loginfeedbacklbl.setFont(QtGui.QFont(betutipus_csalad[0], 14))
        self.loginfeedbacklbl.setStyleSheet("color: red")

        self.resize(500, 500)
        self.setWindowTitle("Bejelentkezés")


class Regisztracio(QtWidgets.QWidget):
    def reg_adattarolas(self):
        global full_encpss
        username = self.fhnevinput.text()
        password = self.jszoinput.text()

        usnlist = list(username)
        encstr = usnlist[::-1]
        full_encstr = str(random.randint(0, 9))
        spccharlist = ["#", "?", "!", ".", "/", "="]
        for i in encstr:
            full_encstr += i + str(random.randint(0, 9)) + random.choice(spccharlist)

        psslist = list(password)
        encpslst = psslist[::-1]
        full_encpss = str(random.randint(0, 9))
        for j in encpslst:
            full_encpss += j + str(random.randint(0, 9)) + random.choice(spccharlist)

        try:
            mappakszama = (len(next(os.walk(f"C:/Users/{os.getlogin()}/Appdata/Roaming/myDiscord/Users"))[1]))
        except StopIteration:
            mappakszama = 0
        egyezik = False

        if mappakszama < 10:
            if mappakszama > 0:
                for x in range(mappakszama):
                    f = open(f"C:/Users/{os.getlogin()}/Appdata/Roaming/myDiscord/Users/USER_0{x}/userdata.txt", "r")
                    sorok = f.readlines()
                    usn = sorok[0]
                    jusn = usn[4:]
                    nums = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58, 61, 64, 67, 70]
                    uname = ""
                    x = 0
                    while x != len(jusn):
                        if x in nums:
                            uname += jusn[x]
                        x += 1
                    runame = uname[::-1]
                    runame = runame.replace("\n", "")
                    f.close()
                    if runame == username:
                        self.regfeedbacklbl.setText(
                            "Sikertelen regisztráció!\nIlyen felhasználónévvel már található felhasználó.")
                        self.elrendezes.addWidget(self.regfeedbacklbl)
                        egyezik = True
                    else:
                        if not egyezik:
                            os.makedirs(os.path.dirname(
                                f"C:/Users/{os.getlogin()}/Appdata/Roaming/myDiscord/Users/USER_0{mappakszama}/userdata.txt"),
                                exist_ok=True)
                            f = open(
                                f"C:/Users/{os.getlogin()}/Appdata/Roaming/myDiscord/Users/USER_0{mappakszama}/userdata.txt",
                                "w")
                            f.write(f"usn:{full_encstr}\npass:{full_encpss}")
                            f.close()
                            self.regfeedbacklbl.setText("Sikeres regisztráció!\nMostmár bezárhatod az ablakot!")
                            self.elrendezes.addWidget(self.regfeedbacklbl)
            else:
                os.makedirs(os.path.dirname(
                    f"C:/Users/{os.getlogin()}/Appdata/Roaming/myDiscord/Users/USER_0{mappakszama}/userdata.txt"),
                            exist_ok=True)
                f = open(f"C:/Users/{os.getlogin()}/Appdata/Roaming/myDiscord/Users/USER_0{mappakszama}/userdata.txt",
                         "w")
                f.write(f"usn:{full_encstr}\npass:{full_encpss}")
                f.close()
                self.regfeedbacklbl.setText("Sikeres regisztráció!\nMostmár bezárhatod az ablakot!")
                self.elrendezes.addWidget(self.regfeedbacklbl)
        else:
            for x in range(mappakszama):
                if x < 10:
                    f = open(f"C:/Users/{os.getlogin()}/Appdata/Roaming/myDiscord/Users/USER_0{x}/userdata.txt", "r")
                    sorok = f.readlines()
                    usn = sorok[0]
                    jusn = usn[4:]
                    nums = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58, 61, 64, 67, 70]
                    uname = ""
                    x = 0
                    while x != len(jusn):
                        if x in nums:
                            uname += jusn[x]
                        x += 1
                    runame = uname[::-1]
                    runame = runame.replace("\n", "")
                    f.close()
                    if runame == username:
                        self.regfeedbacklbl.setText(
                            "Sikertelen regisztráció!\nIlyen felhasználónévvel már található felhasználó.")
                        self.elrendezes.addWidget(self.regfeedbacklbl)
                        egyezik = True
                    else:
                        if not egyezik:
                            os.makedirs(os.path.dirname(
                                f"C:/Users/{os.getlogin()}/Appdata/Roaming/myDiscord/Users/USER_{mappakszama}/userdata.txt"),
                                        exist_ok=True)
                            f = open(
                                f"C:/Users/{os.getlogin()}/Appdata/Roaming/myDiscord/Users/USER_{mappakszama}/userdata.txt",
                                "w")
                            f.write(f"usn:{full_encstr}\npass:{full_encpss}")
                            f.close()
                            self.regfeedbacklbl.setText("Sikeres regisztráció!\nMostmár bezárhatod az ablakot!")
                            self.elrendezes.addWidget(self.regfeedbacklbl)
                elif x >= 10:
                    f = open(f"C:/Users/{os.getlogin()}/Appdata/Roaming/myDiscord/Users/USER_{x}/userdata.txt", "r")
                    sorok = f.readlines()
                    usn = sorok[0]
                    jusn = usn[4:]
                    nums = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58, 61, 64, 67, 70]
                    uname = ""
                    x = 0
                    while x != len(jusn):
                        if x in nums:
                            uname += jusn[x]
                        x += 1
                    runame = uname[::-1]
                    runame = runame.replace("\n", "")
                    f.close()
                    if runame == username:
                        self.regfeedbacklbl.setText(
                            "Sikertelen regisztráció!\nIlyen felhasználónévvel már található felhasználó.")
                        self.elrendezes.addWidget(self.regfeedbacklbl)
                        egyezik = True
                    else:
                        if not egyezik:
                            os.makedirs(os.path.dirname(
                                f"C:/Users/{os.getlogin()}/Appdata/Roaming/myDiscord/Users/USER_{mappakszama}/userdata.txt"),
                                        exist_ok=True)
                            f = open(
                                f"C:/Users/{os.getlogin()}/Appdata/Roaming/myDiscord/Users/USER_{mappakszama}/userdata.txt",
                                "w")
                            f.write(f"usn:{full_encstr}\npass:{full_encpss}")
                            f.close()
                            self.regfeedbacklbl.setText("Sikeres regisztráció!\nMostmár bezárhatod az ablakot!")
                            self.elrendezes.addWidget(self.regfeedbacklbl)

    def __init__(self):
        super().__init__()

        self.setStyleSheet("background-color: #292929")

        self.elrendezes = QtWidgets.QVBoxLayout(self)
        self.elrendezes.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.logolabel = QtWidgets.QLabel()
        self.pxmp = QtGui.QPixmap(f"C:/Users/{os.getlogin()}/Appdata/Roaming/myDiscord/Images/logo2.png")
        self.pxmp = self.pxmp.scaled(150, 150, aspectMode=QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.logolabel.setPixmap(self.pxmp)
        self.logolabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.reglabel = QtWidgets.QLabel("Regisztráció")
        self.reglabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.reglabel.setFont(QtGui.QFont(betutipus_csalad[0], 22))
        self.reglabel.setStyleSheet("color: white; margin-bottom: 20px")

        self.fhnevlabel = QtWidgets.QLabel("Felhasználónév:")
        self.fhnevlabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.fhnevlabel.setFont(QtGui.QFont(betutipus_csalad[0], 14))
        self.fhnevlabel.setStyleSheet("color: white")

        self.fhnevinput = QtWidgets.QLineEdit()
        self.fhnevinput.setFixedWidth(250)
        self.fhnevinput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.fhnevinput.setStyleSheet("margin-bottom: 20px; color: white")

        self.jszolabel = QtWidgets.QLabel("Jelszó:")
        self.jszolabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.jszolabel.setFont(QtGui.QFont(betutipus_csalad[0], 14))
        self.jszolabel.setStyleSheet("color: white")

        self.jszoinput = QtWidgets.QLineEdit()
        self.jszoinput.setFixedWidth(250)
        self.jszoinput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.jszoinput.setStyleSheet("margin-bottom: 30px; color: white")

        self.reggomb = QtWidgets.QPushButton("Regisztrálok")
        self.reggomb.setStyleSheet("QPushButton{background-color: white;} QPushButton:hover{background-color: red}")
        self.reggomb.setFont(QtGui.QFont(betutipus_csalad[0], 12))
        self.reggomb.setFixedWidth(150)
        self.reggomb.clicked.connect(self.reg_adattarolas)

        self.regfeedbacklbl = QtWidgets.QLabel("")
        self.regfeedbacklbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.regfeedbacklbl.setFont(QtGui.QFont(betutipus_csalad[0], 14))
        self.regfeedbacklbl.setStyleSheet("color: red")

        self.elrendezes.addWidget(self.logolabel)
        self.elrendezes.addWidget(self.reglabel)
        self.elrendezes.addWidget(self.fhnevlabel)
        self.layout2 = QtWidgets.QGridLayout()
        self.elrendezes.addLayout(self.layout2)
        self.layout2.addWidget(self.fhnevinput)
        self.elrendezes.addWidget(self.jszolabel)
        self.layout3 = QtWidgets.QGridLayout()
        self.layout4 = QtWidgets.QHBoxLayout()
        self.elrendezes.addLayout(self.layout3)
        self.layout3.addWidget(self.jszoinput)
        self.elrendezes.addLayout(self.layout4)
        self.layout4.addWidget(self.reggomb)

        self.resize(500, 500)
        self.setWindowTitle("Regisztráció")


class Fooldal(QtWidgets.QWidget):

    def loginablak(self):
        if not os.path.exists(f"C:/Users/{os.getlogin()}/Appdata/Roaming/myDiscord/Users"):
            ctypes.windll.user32.MessageBoxW(0, "Nem található regisztrált felhasználó erről az eszközről!", "Hiba")
        else:
            if not skiplogin:
                if self.y is None:
                    self.y = Bejelentkezes()
                self.y.show()
            else:
                if self.m is None:
                    self.m = Main()
                self.m.show()

    def mainablak(self):
        if self.m is None:
            self.m = Main()
        self.m.show()

    def regablak(self):
        if self.w is None:
            self.w = Regisztracio()
        self.w.show()

    def __init__(self):
        super().__init__()
        global betutipus, betutipus_csalad

        self.w = None

        self.y = None

        self.m = None

        self.setStyleSheet("background-color: #292929")

        betutipus = QtGui.QFontDatabase.addApplicationFont(
            f"C:/Users/{os.getlogin()}/Appdata/Roaming/myDiscord/Fonts/AfacadFlux-Regular.ttf")

        betutipus_csalad = QtGui.QFontDatabase.applicationFontFamilies(betutipus)

        self.logolabel = QtWidgets.QLabel()
        self.pxmp = QtGui.QPixmap(f"C:/Users/{os.getlogin()}/Appdata/Roaming/myDiscord/Images/logo2.png")
        self.pxmp = self.pxmp.scaled(150, 150, aspectMode=QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.logolabel.setPixmap(self.pxmp)
        self.logolabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.udvozlo_szoveg = QtWidgets.QLabel("Üdvözöllek!")
        self.udvozlo_szoveg.setFont(QtGui.QFont(betutipus_csalad[0], 24))
        self.udvozlo_szoveg.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.udvozlo_szoveg.setStyleSheet("margin-bottom: 100px; color: white")

        self.regisztralas_szoveg = QtWidgets.QLabel(
            "Új felhasználó vagy?\nHa igen, akkor kérlek regisztrálj egy fiókot!\nHa nem, jelentkezz be!\n")
        self.regisztralas_szoveg.setFont(QtGui.QFont(betutipus_csalad[0], 14))
        self.regisztralas_szoveg.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.regisztralas_szoveg.setStyleSheet("color: white")

        self.regisztracios_gomb = QtWidgets.QPushButton("Regisztráció")
        self.regisztracios_gomb.setStyleSheet("background-color: #00609c; color: white")
        self.regisztracios_gomb.clicked.connect(self.regablak)
        self.regisztracios_gomb.setFont(QtGui.QFont(betutipus_csalad[0], 12))

        self.bejelentkezes_gomb = QtWidgets.QPushButton("Bejelentkezés")
        self.bejelentkezes_gomb.setStyleSheet("background-color: #009c1a; color: white")
        self.bejelentkezes_gomb.clicked.connect(self.loginablak)
        self.bejelentkezes_gomb.setFont(QtGui.QFont(betutipus_csalad[0], 12))

        self.verzio = QtWidgets.QLabel("v.a.1.2.0")
        self.verzio.setStyleSheet("color: white; margin-top: 125px")
        self.verzio.setFont(QtGui.QFont(betutipus_csalad[0], 10))
        self.verzio.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.logolabel)
        self.layout.addWidget(self.udvozlo_szoveg)
        self.layout.addWidget(self.regisztralas_szoveg)

        self.layout2 = QtWidgets.QHBoxLayout(self)
        self.layout.addLayout(self.layout2)
        self.layout2.addWidget(self.regisztracios_gomb)
        self.layout2.addWidget(self.bejelentkezes_gomb)
        self.layout.addWidget(self.verzio)

        if os.path.exists(f"C:/Users/{os.getlogin()}/Appdata/Roaming/myDiscord/Settings/settings.txt"):
            f = open(f"C:/Users/{os.getlogin()}/Appdata/Roaming/myDiscord/Settings/settings.txt", "r")
            sorok = f.readlines()
            print(sorok[0])
            sorok[0] = sorok[0].replace("\n", "")

            if str(sorok[0]) == "skiplogin: 1":
                self.mainablak()
                QtCore.QTimer.singleShot(0, self.close)

            f.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    fooldal = Fooldal()
    fooldal.resize(800, 600)
    fooldal.setWindowTitle("myDiscord")
    fooldal.show()

    sys.exit(app.exec())
