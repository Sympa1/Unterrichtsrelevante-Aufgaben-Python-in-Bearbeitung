# TODO: LKW-Maut
#  Ein Programm soll für erfasste LKW die entsprechende LKW-Mautgebühr nach der folgenden
#  Tabelle berechnen.

# deklaration der Dictionary's mit dem Inhalt der Abrechnungstabellen (Schadstoffklasse (Key)-ct/km (value))
# bis 3 Achsen
THREE_AXES = {"A": 12.50, "B": 14.60, "C": 15.70, "D": 18.80, "E": 19.80, "F": 20.80}
# ab 4 Achsen
FOUR_AXES = {"A": 13.10, "B": 15.20, "C": 16.30, "D": 19.40, "E": 20.40, "F": 21.40}


def convert_input(input_string):
	"""
	Diese Funktion wandelt einen String in einen Float & tauscht "," und "."
	:param input_string:
	:return: output_float
	"""
	output_float = float(input_string.replace(",", "."))
	return output_float


def calculate_truck_toll(emission_class, travel_distance, count_axes):
	travel_distance = convert_input(travel_distance)

	# ich greife mit der Variable "emission_class" als Key auf den passen Value zu
	if int(count_axes) == 3:
		calculate = THREE_AXES[emission_class] * travel_distance
	elif int(count_axes) == 4:
		calculate = FOUR_AXES[emission_class] * travel_distance

	return calculate


# erfassen der Schadstoffklasse und der Anzahl der gefahrenen KM
emission_class = input("Bitte geben Sie die Schadstoffklasse an (A, B, C, D, E, F): ")

travel_distance = input("Bitte geben Sie die Anzahl der gefahrenen Kilometer an: ")

count_axes = input("Bitte geben Sie die an ob Sie 3 (oder weniger) oder 4 (oder mehr) Achsen haben (3, 4): ")

# Test Dictionary Zugriff
print(f"Sie müssen für Ihre Fahrt {calculate_truck_toll(emission_class, travel_distance, count_axes)} ct bezahlen!")
