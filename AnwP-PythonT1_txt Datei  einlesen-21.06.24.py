# TODO: 1. In einer Datei stehen zeilenweise die Länder (z.B. Italien, Frankreich, Spanien und Belgien) Diese Datei ist  einzulesen und
#  auf der Konsole auszugeben.
# TODO: 2. Datei einlesen und Konsoleingabe Für alle gelesenen Länder ist in einer Schleife die Eingabe der jeweiligen Hauptstadt über
#  die Konsole anzufordern. In einer Variablen von Datentyp Dictionary sind Land und Hauptstadt anzulegen und dann auf der Konsole zu
#  protokollieren.
# TODO: 3. Weitere Ausbaustufe: Über einen Dialog sind zwei weitere Länder mit ihren Hauptstädten zum bestehenden Dictionary zu ergänzen.
#  Das Dictionary ist in einer neuen Datei auszugeben, z.B.: (Italien Rom), (Frankreich Paris), (Spanien Madrid), (Belgien Brüssel) usw.
# TODO: 4. Dateien vergleichen Die Datei der Aufgabe 1 und die neue Datei, erstellt in der Aufgabe 3, sind jeweils einzulesen. Durch
#  Abgleich der Datensätze soll ermittelt werden, welche Länder (über die Aufgabe 2) ergänzt wurden. Diese Länder sind auf der Konsole zu
#  protokollieren


def formatted(land_list):
	"""
	Diese Funktion entfernt die ausgeschriebenen Zeilen Umbrüche "\n" bei den eingelesenen Elementen einer Liste
	:param land_list: Liste
	:return: land_list_formatted - Liste
	"""
	land_list_formatted = []
	for land in land_list:
		land_list_formatted.append(land.replace("\n", ""))

	return land_list_formatted


def task1():
	"""
	Diese Funktion liest eine Datei xy ein und gibt den Inhalt als Liste zurück
	:return: formatted(read_file) - Liste
	"""
	try:
		open_file = open("AnwP-PythonT1_txt Datei  einlesen-21.06.24.txt", "r")
		read_file = open_file.readlines()
		open_file.close()
	except FileNotFoundError as error:
		print("Die Datei wurde nicht gefunden!", error.args[1])

	# return read_file
	return formatted(read_file)


def task2():
	"""
	Diese FUnion legt ein internes Dictionary an und speichert die vom Nutzer eingegebenen Hauptstädte passend zu den Ländern ab.
	Das Dictionary wird am Ende zurückgegeben
	:return: land_dict - Dictionary
	"""
	land_dict = {}
	land_list = task1()

	for land in formatted(land_list):
		while True:
			capital_city = input(f"Bitte geben Sie die Hauptstadt von {land}an: ")
			try:
				if isinstance(int(capital_city), int) or isinstance(float(capital_city), float):
					print(f"{capital_city} ist keine gültige Eingabe!")
					continue
			except:
				break

		land_dict[land] = capital_city

	return land_dict


def task3(land_dict):
	"""
	Diese Funktion erhöht die Anzahl der Dictionary Einträge auf genau 6. & speichert diese in einer neuen ".txt" Datei.
	:param land_dict: Dictionary
	:return: Nichts
	"""
	print(land_dict)
	while True:
		if len(land_dict) == 6:
			break
		else:
			input_land = input("Bitte geben Sie ein Land an: ")
			input_capital_city = input(f"Bitte geben Sie die Hauptstadt von {input_land} an: ")
			land_dict[input_land] = input_capital_city

			# Nachricht ausgeben, dass die Eingaben erfolgreich hinterlegt wurden
			if input_land in land_dict:
				print(
					f"Das Land \"{input_land}\" mit der Hauptstadt \"{input_capital_city}\" wurden erfolgreich im Dictionary "
					f"hinterlegt!")

	# Ist der "try/except" unsinnig hier? Die Datei wird doch im Zweifel erstellt. ist sinnvoll diesen Teil in eine separate
	# Funktion zu packen?
	try:
		# Neue Textdatei anlegen, falls noch nicht vorhanden und Datensätze hinzufügen
		write_file = open("AnwP-PythonT1_txt Datei  einlesen_neu-21.06.24.txt", "a")
		# Alle Elemente des Dictionary Zeile für Zeile in die Datei schreiben. Als erste Eintrag für Eintrag als String speichern
		for key, value in land_dict.items():
			element = f"{key} - {value}\n"
			write_file.write(element)
	except:
		print("unbekannter Dateifehler")
		exit(42)


def task4():
	"""
    Diese Funktion liest beide Dateien ein, entfernt bei der 2. Datei die Städte, packt diese in eine neue Liste & gleicht
    diese mit der alten Datei Liste ab. Die überschneidungen werden entfernt, sodass nur die neuen Elemente überbleiben
    :return: Nichts
    """
	try:
		list_difference = []
		open_file_old = open("AnwP-PythonT1_txt Datei  einlesen-21.06.24.txt", "r")
		save_file_old = formatted(open_file_old.readlines())
		open_file_old.close()
	except FileNotFoundError as error:
		print("Datei nicht gefunden", error.args[1])
		exit(202)
	except:
		print("sonst. Fehler")
		exit(42)

	try:
		open_file_new = open("AnwP-PythonT1_txt Datei  einlesen_neu-21.06.24.txt", "r")
		save_file_new = formatted(open_file_new.readlines())
		open_file_new.close()
	except FileNotFoundError as error:
		print("Datei nicht gefunden", error.args[1])
		exit(202)
	except:
		print("sonst. Fehler")
		exit(42)

	for citys in save_file_new:
		land, city = citys.split(' ', 1)  # Teilt den String an dem ersten Leerzeichen. Die 1 gibt Häufigkeit an,
		# wie oft also pro vorkommen das Trennelement getrennt wird
		list_difference.append(land)

	for city in save_file_old:
		if city in list_difference:
			list_difference.remove(city)  # ".remove(zu entfernendes Element)

	print(list_difference)


# Aufruf Aufgabe 1 → in 2 unterschildchen Varianten (ohne & mit Funktion "formatted")
"""for land in task1():
	print(land, end="")"""
print(task1())

# Aufruf Aufgabe 2 → Doe for Schleife damit es schön untereinander ausgegeben wird. Funktionsaufruf durch "return" in der
# Schleife möglich. ".items()" gibt KEY|VALUE Paare aus.
country_dict = task2()

for land in country_dict.items():
	print(land)

# Aufruf Aufgabe 3
task3(country_dict)

# Aufruf Aufgabe 4
task4()
