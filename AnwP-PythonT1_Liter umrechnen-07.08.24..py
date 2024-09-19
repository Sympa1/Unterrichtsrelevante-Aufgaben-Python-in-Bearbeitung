# TODO: Liter Zahl umwandeln
#  Es soll ein Programm implementiert werden, dass für beliebige Volumenangaben als Gleitpunktzahl in Liter den entsprechenden
#  Wert im ml, cl oder l ausgibt.

def convert_user_input(input):
	"""
	Die Funktion wandelt die Nutzeingabe in einen float um. Dabei wird auch ein "," mit "." getauscht
	:param input:
	:return: output
	"""
	output = float(input.replace(",", "."))
	return output


# als lambda Variante
output = lambda input: float(input.replace(",", "."))


def convert_liters(volume_str):
	"""
	Die Funktion wandelt die Volumenangabe in "l", "cl" oder "ml" um
	:param volume_str:
	:return: volume_float
	"""
	volume_float = output(volume_str)

	if volume_float >= 1.0:
		return str(volume_float).replace(".", ",") + " l"
	elif volume_float >= 0.1:  # Wenn ich die "0" hinter dem "." entferne habe ich die Musterlösung. Jedoch sind 10 ml = 1 cl?
		volume_float *= 100
		return str(volume_float).replace(".", ",") + " cl"
	elif volume_float >= 0.001:
		volume_float *= 1000
		return str(volume_float).replace(".", ",") + " ml"
	else:
		volume_float = "Wert zu klein"
		return volume_float


user_input = input("Bitte geben Sie das Volumen an: ")

print(convert_liters(user_input))
