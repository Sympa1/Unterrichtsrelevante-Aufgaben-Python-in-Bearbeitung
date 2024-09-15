# TODO: 1. Es ist eine Liste mit 100 zufälligen ganzzahligen Werten im Bereich von 1 bis 1000 zu füllen.
# TODO: 2. Die nächsten Lottozahlen sind zu „ermitteln“. Es ist eine Liste mit 6 zufälligen Ganzzahlen aus dem Bereich von 1 bis 49 zu
#  füllen; bei den ermittelten Ganzzahlen sollte es keine Duplikate geben.
# TODO: 3. Es ist ein 16-stelliges Passwort zu generieren; es dürfen alle druckbaren Zeichen, also Groß- und Kleinbuchstaben,
#  Ziffern und die Sonderzeichen vorhanden sein.
# TODO: 4. Die Karten eines Skatspieles sind in einer Liste sortiert einzutragen; beginnend bei Karo7, Karo8, Karo9, Karo10, KaroBube,
#  KaroDame, KaroKönig und KaroAs und dann folgend die jeweiligen Kartenwerte für Herz, Pik und Kreuz. Diese Liste ist auf der Konsole
#  auszugeben. Anschließend ist die Liste mit den 32 Karten zu mischen und so wieder auf der Konsole auszugeben.

from random import *


def aufgabe1():
	number = 100
	i = 0
	list = []

	while i < number:
		value = randint(1, 1000)
		list.append(value)
		i += 1

	return list


def aufgabe2():
	lottery_numbers = sample(range(1, 50), 6)

	formatted_lottery_numbers = f"Die kommenden Lottozahlen sind: {lottery_numbers[0]}, " \
								f"{lottery_numbers[1]}, {lottery_numbers[2]}, {lottery_numbers[3]}, {lottery_numbers[4]} & die" \
								f" {lottery_numbers[5]}!"

	return formatted_lottery_numbers


def aufgabe3():
	# Symbolliste
	password_elements = ["a", "b", "c", "ä", "ö", "ü", "!", "@", "#", "$", "%", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
						 "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
						 "U", "V", "W", "X", "Y", "Z", "Ä", "Ö", "Ü", "&", "*", "(", ")", "-", "_", "+", "=", "[", "]", "{",
						 "}", ";", ":", "<", ">", ",", ".", "?", "/", "|", "\\", "'", '"', "`", "~"]

	# Deklaration (ohne Wertzuweisung) der Liste für das zu generierendes Passwort
	final_password = []

	# Begrüßung
	print("Hallo ich bin \"PG\" Dein freundlicher Passwortgenerator :)\n")

	# Deklaration der Variable zur bestimmung der maximalen Passwortlänge
	max_length = 255

	while True:
		try:
			# Erfassung der Nutzeingaben als "Integer" für die Passwortspezifikationen
			password_length = int(input("Geben Sie die Passwortlänge an (max. 255 Zeichen): "))
			# Kontrolle, ob die maximalen Zeichen eingehalten wurden
			if password_length > max_length:
				print("\n Ihre gewünschte Passwortlänge entspricht nicht der Maximal zulässigen Passwortlänge!\n")
			else:
				# Generieren des Passwortes
				for i in range(password_length):
					element = choice(password_elements)
					final_password.append(element)

				break
		except ValueError:
			print("Bitte geben Sie nur Ganzzahlen an!")

	# .join() macht das Komme weg & wandelt die Liste in einen String
	password = "".join(final_password)

	return password


def aufgabe4():
	card_game = ["Karo7", "Karo8", "Karo9", "Karo10", "KaroBube", "KaroDame", "KaroKönig", "KaroAs", "Herz7", "Herz8", "Herz9",
				 "Herz10", "HerzBube", "HerzDame", "HerzKönig", "HerzAs", "Pik7", "Pik8", "Pik9", "Pik10", "PikBube",
				 "PikDame", "PikKönig", "PikAs", "Kreuz7", "Kreuz8", "Kreuz9", "Kreuz10", "KreuzBube", "KreuzDame",
				 "KreuzKönig", "KreuzAs"]

	print(f"SpeicherID vor \"shuffle\": {id(card_game)}")
	shuffle(card_game)
	print(f"SpeicherID nach \"shuffle\": {id(card_game)}")

	return card_game


# Aufruf der Funktionen
print(aufgabe1(), "\nBeweis der Länge:", len(aufgabe1()))
print(100 * "=")
print(aufgabe2())
print(100 * "=")
print(f" Dein neues Passort lautet:		{aufgabe3()}")
print(100 * "=")
print(f"Das gemischte Kartenspiel:\n{aufgabe4()}")
