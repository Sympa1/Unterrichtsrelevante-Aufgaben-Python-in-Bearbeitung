# TODO: Mit einer Lambda-Funktion ist ein Wert zu quadrieren und auf der Konsole auszugeben

output = lambda input: float(input.replace(",", "."))

quad = lambda num: num * num

# erfassen der zu quadrierenden Zahl
quad_input = input("Welche Zahl soll quadriert werden? ")

# input String in float umwandeln
quad_num = output(quad_input)

quad_result = str(quad(quad_num)).replace(".", ",")

# das Ergebnis
print(f"Die zu quadrierende Zahl \"{quad_input}\" hat das Ergebnis {quad_result}")
