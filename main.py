import random
import socket
import sys
import threading
from PySide6 import QtWidgets, QtGui, QtCore
import os
import ctypes
import wget

########################################################################################################################

# # Funkció az üzenetek fogadására a szervertől
# def receive_messages(client_socket):
#     while True:
#         try:
#             message = client_socket.recv(1024).decode('utf-8')
#             if not message:
#                 break
#             print(f"\nBarátod: {message}")
#         except:
#             break
#
#
# # Kliens indítása
# def start_client():
#     host = '188.36.17.24'  # Szerver IP címe
#     port = 9600  # Szerver portja
#
#     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client_socket.connect((host, port))
#
#     print(f"Kapcsolódva a szerverhez: {host}:{port}")
#
#     # Üzenetek fogadására külön szálat indítunk
#     receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
#     receive_thread.start()
#
#     # Üzenetek küldése a szervernek
#     while True:
#         message = input("Te: ")
#         if message.lower() in ['exit', 'kilépés']:
#             print("Kilépés...")
#             client_socket.send(message.encode('utf-8'))
#             break
#         client_socket.send(message.encode('utf-8'))
#
#     client_socket.close()
#
#
# start_client()


########################################################################################################################

if not os.path.exists(f"C:/Users/{os.getlogin()}/Appdata/Roaming/myDiscord"):
    os.makedirs(f"C:/Users/{os.getlogin()}/Appdata/Roaming/myDiscord/Fonts")
    os.makedirs(f"C:/Users/{os.getlogin()}/Appdata/Roaming/myDiscord/Images")
    wget.download("https://mega.nz/file/yRpBQZSI#b_xTM85mjawfuNrLbXzTgqCFg5jAYJR7VSo__toX7Ow", f"C:/Users/{os.getlogin()}/Appdata/Roaming/myDiscord/Fonts")


class Bejelentkezes(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()




class Regisztracio(QtWidgets.QWidget):
    def reg_adattarolas(self):
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
        print(mappakszama)

        global egyezik
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
                    if runame == username:
                        ctypes.windll.user32.MessageBoxW(0, "Ezzel a felhasználónévvel rendelkező fiók már létezik", "Hiba")
                        egyezik = True
                    else:
                        if not egyezik:
                            os.makedirs(os.path.dirname(
                                f"C:/Users/{os.getlogin()}/Appdata/Roaming/myDiscord/Users/USER_0{mappakszama}/userdata.txt"), exist_ok=True)
                            f = open(f"C:/Users/{os.getlogin()}/Appdata/Roaming/myDiscord/Users/USER_0{mappakszama}/userdata.txt", "w")
                            f.write(f"usn:{full_encstr}\npass:{full_encpss}")
                            f.close()
            else:
                os.makedirs(os.path.dirname(f"C:/Users/{os.getlogin()}/Appdata/Roaming/myDiscord/Users/USER_0{mappakszama}/userdata.txt"), exist_ok=True)
                f = open(f"C:/Users/{os.getlogin()}/Appdata/Roaming/myDiscord/Users/USER_0{mappakszama}/userdata.txt", "w")
                f.write(f"usn:{full_encstr}\npass:{full_encpss}")
                f.close()
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
                    print(runame)
                    print(username)
                    if runame == username:
                        ctypes.windll.user32.MessageBoxW(0, "Ezzel a felhasználónévvel rendelkező fiók már létezik", "Hiba")
                        egyezik = True
                    else:
                        if not egyezik:
                            os.makedirs(os.path.dirname(f"C:/Users/{os.getlogin()}/Appdata/Roaming/myDiscord/Users/USER_{mappakszama}/userdata.txt"), exist_ok=True)
                            f = open(f"C:/Users/{os.getlogin()}/Appdata/Roaming/myDiscord/Users/USER_{mappakszama}/userdata.txt", "w")
                            f.write(f"usn:{full_encstr}\npass:{full_encpss}")
                            f.close()
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
                    print(runame)
                    print(username)
                    if runame == username:
                        ctypes.windll.user32.MessageBoxW(0, "Ezzel a felhasználónévvel rendelkező fiók már létezik", "Hiba")
                        egyezik = True
                    else:
                        if not egyezik:
                            os.makedirs(os.path.dirname(f"C:/Users/{os.getlogin()}/Appdata/Roaming/myDiscord/Users/USER_{mappakszama}/userdata.txt"), exist_ok=True)
                            f = open(f"C:/Users/{os.getlogin()}/Appdata/Roaming/myDiscord/Users/USER_{mappakszama}/userdata.txt", "w")
                            f.write(f"usn:{full_encstr}\npass:{full_encpss}")
                            f.close()



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
            if self.y is None:
                self.y = Bejelentkezes()
            self.y.show()

    def regablak(self):
        if self.w is None:
            self.w = Regisztracio()
        self.w.show()

    def __init__(self):
        super().__init__()
        global betutipus, betutipus_csalad

        self.w = None

        self.y = None

        self.setStyleSheet("background-color: #292929")

        betutipus = QtGui.QFontDatabase.addApplicationFont(f"C:/Users/{os.getlogin()}/Appdata/Roaming/myDiscord/Fonts"
                                                           f"/AfacadFlux-Regular.ttf")
        if betutipus < 0:
            print("Hiba")

        betutipus_csalad = QtGui.QFontDatabase.applicationFontFamilies(betutipus)

        self.logolabel = QtWidgets.QLabel()
        self.pxmp = QtGui.QPixmap(f"C:/Users/{os.getlogin()}/Appdata/Roaming/myDiscord/Images/logo2.png")
        self.pxmp = self.pxmp.scaled(150, 150, aspectMode=QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.logolabel.setPixmap(self.pxmp)
        self.logolabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.udvozlo_szoveg = QtWidgets.QLabel("Üdvözöllek!")
        self.udvozlo_szoveg.setFont(QtGui.QFont(betutipus_csalad[0], 24))
        self.udvozlo_szoveg.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.udvozlo_szoveg.setStyleSheet("margin-bottom: 30px; color: white")

        self.regisztralas_szoveg = QtWidgets.QLabel("Új felhasználó vagy?\nHa igen, akkor kérlek regisztrálj egy "
                                                    "fiókot!\nHa nem, jelentkezz be!\n")
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

        self.verzio = QtWidgets.QLabel("v.a.0.0.1")
        self.verzio.setStyleSheet("color: white; margin-top: 200px")
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

        # print(QtGui.QFontDatabase.families())


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    fooldal = Fooldal()
    fooldal.resize(800, 600)
    fooldal.setWindowTitle("myDiscord")
    fooldal.show()

    sys.exit(app.exec())
