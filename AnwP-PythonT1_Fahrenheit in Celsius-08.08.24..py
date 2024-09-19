# TODO: Umrechnung Fahrenheit in Celsius
#  Für die Umrechnung von Fahrenheit in Celsius gilt: 𝐂 = (°𝐅 − 32) ∗ 5/9 -als Bruch- Für die Programmierung in Python soll ein
#  Lambda-Ausdruck definiert werden. Die Temperaturwerte [°F] als Elemente in einer Liste sollen über eine Schleife
#  abgearbeitet und die Temperaturwerte in °C ermittelt und auf die Konsole ausgegeben werden.

from fractions import Fraction

fahrenheit_liste = [52.5, 60, 27.5, 217]
celsius_liste = []

# mit Fraction(Zähler, Nenner) kann simpel mit Brüchen rechnen "...* 5 / 9..." würde das gleiche ergebnis brignen
for fahrenheit in fahrenheit_liste:
	celsius = (lambda fa: (fa - 32) * Fraction(5, 9))(fahrenheit)
	# Python hatte wohl Probleme Integer und Float Zahlen gleichermaßen zu behandeln und hat nicht alles so wie es soll in die
	# Liste eingefügt
	celsius_liste.append(round(float(celsius), 2))

# Ergebnis
print(f"Liste 1 -> {celsius_liste}")

print(100 * "-")

# TODO: Aufgabe 1 mit Listenabstraktion (List Comprehension) lösen

celsius_liste2 = [round(float((fa - 32) * Fraction(5, 9)), 2) for fa in fahrenheit_liste]

print(f"Liste 2 -> {celsius_liste2}")

a = 10 / 3
print(a)

b = Fraction(10, 3)
print(b)
print(type(b))
