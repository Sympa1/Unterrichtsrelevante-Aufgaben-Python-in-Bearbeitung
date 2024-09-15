# TODO: 1. Es sind Datumsdifferenzen zu berechnen:
#  - 01.01.2020 bis heute
#  - 01.07.2022 bis 30.09.2022
#  Beide Datumsangaben über die Konsole einlesen und die Differenz ermitteln.
# TODO: 2. Die Laufzeit für die Ausführung einer Schleife ist zu ermitteln:
#  - Es ist eine Schleife zu programmieren, die alle Zahlen von 1 bis 1000 addiert, deren Ausführungszeit ist zu ermitteln.
#  - Eine weitere Schleife soll programmiert werden und die Zahlen von 1 bis 1.000.000 addiert werden, wieder ist die Ausführungszeit zu
#  ermitteln.
# TODO: 3. Für die Erfassung von Artikeln (z.B. Banane, Orange, Zitrone usw.) und deren Einzelpreis ist eine Endlosschleife zu
#  programmieren; als Abbruchkriterium wird die Eingabe von „q“ bei der Artikeleingabe vorgeschlagen. Die Artikelbezeichnungen und die
#  Einzelpreise sind zusammen mit einem Zeitstempel in einer Textdatei abzuspeichern.
# TODO: 4. Mit einem weiteren Programm ist diese Datei einzulesen: Für alle Artikel ist die gewünschte Menge über die Konsol-Eingabe
#  anzufordern. Es ist die Summe für jeden Artikel zu bilden (Einzelpreis * Menge) und der Gesamtbetrag zu errechnen und auf der Konsole
#  auszugeben.

from datetime import timedelta, datetime, date
import csv

# Deklaration notwendiger Variablen
termination = "q"
article_price_dict = {}
header = ["Artikel", "Einzelpreis"]
data_list = []


def aufgabe1():
	# Deklaration der Daten
	dat1 = date(2020, 1, 1)
	dat2 = date.today()
	dat3 = date(2022, 7, 1)
	dat4 = date(2022, 9, 30)
	dif1 = dat2 - dat1
	dif2 = dat4 - dat3
	print(dif1)
	print(dif2)


def aufgabe2():
	# Erste Aufgabe
	start_time = datetime.now()
	summe = 0
	for i in range(1, 1001):
		summe += i
	end_time = datetime.now()
	duration = end_time - start_time
	print(start_time)
	print(end_time)
	print(f"Die schleife braucht für einen Durchlauf {duration.microseconds} Mikrosekunden")

	# Zweite Aufgabe
	start_time = datetime.now()
	summe = 0
	for i in range(1, 1000001):
		summe += i
	end_time = datetime.now()
	duration = end_time - start_time
	print(start_time)
	print(end_time)
	print(f"Die schleife braucht für einen Durchlauf {duration.microseconds} Mikrosekunden")


def aufgabe3_save(dict, article, price):
	try:  # → Ich dachte erst, es sei unnötig, in dieser Konstellation ist es das sicher auch. Jedoch liegt die Datei auf einen
		# Server, welcher nicht erreichbar ist, sieht das schon anders aus.
		with open("AnwP-PythonT1_Modul datetime-27.06.24.csv", "a", newline="") as save_file:
			csv_writer = csv.DictWriter(save_file, header)  # →Ist das mit, wie bei SQL der sg., "Cursor"
			# gleichzustellen?→Vermittler?
			csv_writer.writerow(dict)
			return_message = (f"Die Nutzereingaben (Artikel: {article} mit dem Einzelpreis: {price}) wurde erfolgreich "
							  f"gespeichert!")

		return return_message
	except:
		print("Dateifehler")


def aufgabe3_csv_clear():
	try:  # → Ich dachte erst, es sei unnötig, in dieser Konstellation ist es das sicher auch. Jedoch liegt die Datei auf einen
		# Server, welcher nicht erreichbar ist, sieht das schon anders aus.
		with open("AnwP-PythonT1_Modul datetime-27.06.24.csv", "w", newline="") as save_file:
			csv_writer = csv.DictWriter(save_file, fieldnames=header)
			csv_writer.writeheader()
	except:
		print("Dateifehler")


def aufgabe3():
	# Zurücksetzen der CSV Datei
	aufgabe3_csv_clear()

	# Nutzerabfrage
	while True:
		# Dictionary zurücksetzen
		article_price_dict = {}

		# Nutzereingaben erfassen und speichern. Ebenfalls wird das Abbruchkriterium überprüft
		user_input_article = input("Artikeleingabe: ")
		if user_input_article == termination:
			break

		user_input_price = input("Einzelpreiseingabe (in €): ")
		if user_input_price == termination:
			break

		# Umwandeln des Preises in einen Float mit "Komma/Punkt" tausch
		user_input_price = float(user_input_price.replace(",", "."))

		# Schreiben der Nutzereingaben in das Dictionary
		article_price_dict["Artikel"] = user_input_article
		article_price_dict["Einzelpreis"] = user_input_price

		print(aufgabe3_save(article_price_dict, user_input_article, user_input_price))


def aufgabe4_read_data():
	try:
		with open("AnwP-PythonT1_Modul datetime-27.06.24.csv", "r") as file:
			csv_reader = csv.reader(file)
			csv_reader = list(csv_reader)
	except FileNotFoundError as error:
		print(f"Error: {error}. Datei nicht gefunden!")
	except:
		exit(42)

	return csv_reader


def aufgabe4():
	# Öffnen, einlesen & schließen der CSV Datei
	data_list = aufgabe4_read_data()
	print(type(data_list))
	print(len(data_list))

	# Kontrolle ob Daten vorhanden sind
	if len(data_list) > 1:
		del data_list[0]
		# Nicht len()+1 weil am End eine Leerzeile steht
		for line in data_list:  # ich muss iwie ab zeile 2 starten
			article = line[0]
			price = float(line[1])
			print(price)
			print(type(price))
			print(f"Artikel: {article}\nEinzelpreis: {price}")
			number = int(input(f"Bitte geben Sie die Menge des Artikels {article} an: ").replace(",", "."))
			total_price = price * number
			print(f"Bei einer Anzahl von {number} beträgt der Gesamtpreis für alle {article} {total_price} €")

	else:
		print("Es wurden keine Nutzereingaben getätigt!")
		while True:
			input_yes_no = input("Möchten Sie Artikel hinzufügen? (y/n)")
			if input_yes_no == "y":
				aufgabe3()
				break
			if input_yes_no == "n":
				print(f"Das Programm ist beendet! {exit(42)}")
				break
			else:
				print("Bitte antworten Sie mit \"y\" für \"Yes\" & \"n\" für \"No\"!")


# Aufruf der Funktionen
aufgabe1()
aufgabe2()
aufgabe3()
aufgabe4()
