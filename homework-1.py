# prime number thing

# num_x = ''
# while 1:
#     num_x = int(input("Zahl x >= 10: "))
#     if num_x >= 10:
#         break
#
#
# def prime1(p):
#     for i in range(2, p):
#         if p % i == 0:
#             return False
#     return True
#
#
# while 1:
#     if prime1(num_x):
#         print(f"Zahl p: {num_x}")
#         break
#     num_x += 1


# Schreiben Sie ein Skript, welches vom Benutzer eine Zahl x >= 10 entgegennimmt
# und daraus zwei Fibonacci-Zahlen f1 und f2 berechnet.
#
# Dabei soll f1 kleiner oder gleich x und f2 grösser x sein.
#
# Falls der Benutzer keine gültige Zahl eingibt, soll die Eingabeaufforderung wiederholt werden.
#
# Zum Beispiel:
# Eingabe	Resultat
# 1         Zahl x >= 10: 1
# 10        Zahl x >= 10: 10
#           Zahl f1: 8
#           Zahl f2: 13

###############################

# input_num = ''
# while 1:
#     input_num = int(input("Zahl x >= 10: "))
#     if input_num >= 10:
#         break
#
#
# n1, n2 = 0, 1
# while 1:
#     n1, n2 = n2, n1 + n2
#     if n1 <= input_num <= n2:
#         print(f"Zahl f1: {n1}")
#         print(f"Zahl f2: {n2}")
#         break


###############################

# Das untenstehende Programm soll eine Tabelle mit den Grossbuchstaben A bis J und den Unicodes dieser Zeichen ausgeben.
# Das Programm enthält drei Fehler. Korrigieren Sie diese.

# print(f"{'Zeichen': ^8}{'Unicode': ^8}")
# for code in range(ord('A'), ord('K')):
#     print(f"{chr(code):^8}{code:^8}")


###############################

# Schreiben Sie Auto, welche die folgenden Attribute hat:
# marke (Hersteller, z.B. "Toyota")
# jahr (Baujahr)
# geschwindigkeit (momentane Geschwindigkeit in km/h)
#
# Die Initialisierungsmethode der Klasse sollte die Parameter Marke, Jahr und Geschwindikeit akzeptieren
# und  deren Werte den entsprechenden Attributen zuweisen. Falls keine Geschwindigkeit angageben wird,
# soll die Geschwindigkeit auf 0 gesetzt werden.
#
# Die Klasse sollte ausserdem die folgenden Methoden haben:
# beschleunige() erhöht die Geschwindigkeit umd 5
# bremse() verringert die Geschwindigkeit um 5 km/h, und setzt sie sonst auf 0
# hupe() druckt  "{marke} hupt", wobei {marke} der Wert des Attributs marke ist.

# class Auto:
#     speed = 0
#
#     def __init__(self, label, year, speed=5):
#         self.marke = label
#         self.jahr = year
#         self.geschwindigkeit = int(speed)
#
#     def beschleunige(self):
#         self.geschwindigkeit += 5
#
#     def bremse(self):
#         if self.geschwindigkeit <= 5:
#             self.geschwindigkeit = 0
#         else:
#             self.geschwindigkeit -= 5
#
#     def hupe(self):
#         print(f"{self.marke} hupt")


######################################

# Schreiben Sie eine Funktion querSumme(zahl),
# welche die Summe der Ziffern des Parameters zahl berechnet und zurückgibt.

# def querSumme(num):
#     result = 0
#     for i in str(num):
#         try:
#             result += int(i)
#         except:
#             continue
#     return result
#
#
# print(querSumme(2903))


#####################################

# Schreiben Sie eine Funktion zeugnis(notenliste), welche ein Dictionary mit Fächern
# und ungerundeten Noten als Parameter notenliste entegennimmt und dafür sorgt,
# dass die Noten zwischen 1.0 und 6.0 liegen und auf halbe Zahlen gerundet sind.
# Die Funktion soll die so verarbeitete Notenliste als Dictionary zurückgeben.


# def zeugnis(ranks):
#     def my_round(val):
#         x = round(val * 2) / 2
#         if x < 1:
#             x = 1.0
#         elif x > 6:
#             x = 6.0
#         return x
#
#     return {k: my_round(v) for k, v in ranks.items()}
#
# print(zeugnis({"Deutsch": 0.4, "Englisch": 6.2, "Französisch": 3.9}))


#######################################

# def schreiben():
#     with open("hallo.txt", 'w') as file:
#         file.write("Hallo Welt")
#
#
# def lesen():
#     with open("hallo.txt", "r") as file:
#         print(file.read())


#######################################
# Schreiben Sie ein Skript, welches vom Benutzer eine Zeitangabe in
# der Form HH:MM (Stunden im Bereich 0 bis 23 und Minuten im Bereich 0 bis 59)
# entgegennimmt und diese in Minuten umrechnet.
# Falls der Benutzer keine gültige Zeit eingibt, soll die Eingabeaufforderung wiederholt werden.

# import time
#
# user_time = ""
#
# while 1:
#     user_time = input("Zeit (HH:MM): ")
#     try:
#         time.strptime(user_time, "%H:%M")
#         break
#     except ValueError:
#         continue
#
# time_in_minutes = int(user_time[0:2]) * 60 + int(user_time[3:5])
#
# print(f"Minuten: {time_in_minutes}")

#######################################
# Das unvollständige Programm im Antwortfeld erstellt eine SQLite-Tabelle "stadt" (in der Datei "geographie.db").
# Ergänzen Sie dieses Programm so, dass es in diese Tabelle einen Datensatz
# mit den Werten 'Shanghai', '2021' und '27.8' einfügt.
# Die Datenbank soll sich bei einer Abfrage so verhalten, wie im Beispiel angegeben.

import os, sqlite3

if os.path.exists("geographie.db"):
    try:
        os.remove("geographie.db")
    except:
        print("Fehler beim Löschen")

connection = sqlite3.connect("geographie.db")
cursor = connection.cursor()

sql = "CREATE TABLE stadt(name TEXT, jahr INTEGER, einwohner_mio REAL)"
cursor.execute(sql)

sql_new = "INSERT INTO STADT VALUES ('Shanghai', 2021, 27.8)"
cursor.execute(sql_new)
connection.commit()


connection.close()
