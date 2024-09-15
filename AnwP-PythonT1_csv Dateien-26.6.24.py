# TODO: 1. In einer CSV-Datei ist eine Adressübersicht abzuspeichern. In dieser Datei sind Name, Vorname, Strasse, PLZ, Wohnort,
#  Geburtsdatum und die Telefonnr von 5 Personen abzuspeichern.
# TODO: 2. Diese CSV-Datei ist über den „Basiszugriff auf eine Textdatei“ einzulesen und die Einträge formatiert auf der Konsole
#  auszugeben.
# TODO: 3. Diese CSV-Datei ist über ein „reader-Objekt“ aus dem csv-Modul einzulesen und die Einträge formatiert auf der Konsole
#  auszugeben.
# TODO: 4. Diese CSV-Datei ist über ein „readerDict-Objekt“ aus dem csv-Modul einzulesen und die Einträge formatiert auf der Konsole
#  auszugeben.
# TODO: 5. Die CSV-Datei ist um die Daten von zwei weiteren Personen zu ergänzen und über eines der Lesemodule (siehe Aufgabe 2 oder
#  Aufgabe 3 oder Aufgabe 4) zu protokollieren

import csv

# Deklaration der Listen
header = ["Nr.", "Name", "Vorname", "Strasse", "PLZ", "Wohnort", "Geburtsdatum", "Tel."]

daten_dict_liste = [{"Nr.": "1", "Name": "Peter", "Vorname": "Hans", "Strasse": "musterweg 1", "PLZ": "0815", "Wohnort":
						"Musterdorf", "Geburtsdatum": "24.12.1900", "Tel.": "010 / 987321"},
					{"Nr.": "2", "Name": "Peter", "Vorname": "Hans", "Strasse": "musterweg 1", "PLZ": "0815", "Wohnort":
						"Musterdorf", "Geburtsdatum": "24.12.1900", "Tel.": "010 / 987321"},
					{"Nr.": "3", "Name": "Peter", "Vorname": "Hans", "Strasse": "musterweg 1", "PLZ": "0815", "Wohnort":
						"Musterdorf", "Geburtsdatum": "24.12.1900", "Tel.": "010 / 987321"},
					{"Nr.": "4", "Name": "Peter", "Vorname": "Hans", "Strasse": "musterweg 1", "PLZ": "0815", "Wohnort":
						"Musterdorf", "Geburtsdatum": "24.12.1900", "Tel.": "010 / 987321"},
					{"Nr.": "5", "Name": "Peter", "Vorname": "Hans", "Strasse": "musterweg 1", "PLZ": "0815", "Wohnort":
						"Musterdorf", "Geburtsdatum": "24.12.1900", "Tel.": "010 / 987321"}]


# Deklaration der Funktion für die Aufgaben
def aufgabe1():
	try:
		with open("AnwP-PythonT1_csv Dateien-26.6.24.csv", "w", newline="") as datei_ausgabe:
			csv_writer = csv.DictWriter(datei_ausgabe, header)
			csv_writer.writeheader()
			csv_writer.writerows(daten_dict_liste)
	except:
		print("unbekannter Dateifehler")


def aufgabe2():
	try:
		datei_eingabe = open("AnwP-PythonT1_csv Dateien-26.6.24.csv", "r")
		zeilen = datei_eingabe.readlines()
		datei_eingabe.close()
		for zeile in zeilen:
			print(zeile, end="")
	except:
		print("Datei unbekannt")


def aufgabe3():
	try:
		with open("AnwP-PythonT1_csv Dateien-26.6.24.csv", "r") as datei_eingabe:
			datei_zeilen = csv.reader(datei_eingabe)
			for zeile in datei_zeilen:
				print(zeile)
	except:
		print("Datei unbekannt")


def aufgabe4():
	with open("AnwP-PythonT1_csv Dateien-26.6.24.csv", "r") as datei_eingabe:
		csv_reader_dict = csv.DictReader(datei_eingabe)
		for zeile in csv_reader_dict:
			print(zeile)


def aufgabe5():
	# Deklaration der neuen Dateien
	neue_daten = [{"Nr.": "6", "Name": "Peter", "Vorname": "Hans", "Strasse": "musterweg 1", "PLZ": "0815", "Wohnort":
		"Musterdorf", "Geburtsdatum": "24.12.1900", "Tel.": "010 / 987321"},
				  {"Nr.": "7", "Name": "Peter", "Vorname": "Hans", "Strasse": "musterweg 1", "PLZ": "0815", "Wohnort":
					  "Musterdorf", "Geburtsdatum": "24.12.1900", "Tel.": "010 / 987321"}]

	try:
		with open("AnwP-PythonT1_csv Dateien-26.6.24.csv", "a") as datei_ausgabe:
			csv_writer = csv.DictWriter(datei_ausgabe, header)
			csv_writer.writerows(neue_daten)
	except:
		print("unbekannter Dateifehler")

	# Kontrolle der neuen Daten
	aufgabe4()


# Aufruf der Funktionen
aufgabe1()
aufgabe2()
aufgabe3()
aufgabe4()
aufgabe5()
