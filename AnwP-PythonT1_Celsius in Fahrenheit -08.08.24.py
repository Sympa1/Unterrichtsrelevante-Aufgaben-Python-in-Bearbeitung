# TODO: Umrechnung Celsius in Fahrenheit für die Umrechnung von Celsius in Fahrenheit gilt: °𝐅 = 𝐂 ∗ 9/5 + 32. Für die
#  Programmierung in Python soll ein Lambda-Ausdruck definiert werden. Die Temperaturwerte [°C] als Elemente in einer Liste
#  sollen über eine Schleife abgearbeitet und die Temperaturwerte in °F ermittelt und auf die Konsole ausgegeben werden.

from fractions import Fraction

fahrenheit_liste = []
celsius_liste = [32.6, -5, 10.6, 101, 42]

# mit Fraction(Zähler, Nenner) kann simpel mit Brüchen rechnen
for celsius in celsius_liste:
	fahrenheit = (lambda ce: ce * Fraction(9, 5) + 32)(celsius)
	# Python hatte wohl Probleme Integer und Float Zahlen gleichermaßen zu behandeln und hat nicht alles so wie es soll in die
	# Liste eingefügt
	fahrenheit_liste.append(round(float(fahrenheit), 2))

# Ergebnis
print(f"Liste 1 -> {fahrenheit_liste}")

print(100 * "-")

# TODO: Aufgabe 2 mit Listenabstraktion (List Comprehension) lösen

fahrenheit_liste2 = [round(float(ce * Fraction(9, 5) + 32), 2) for ce in celsius_liste]

print(f"Liste 2 -> {fahrenheit_liste2}")
