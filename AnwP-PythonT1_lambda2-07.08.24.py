# TODO: Eine Lambda-Funktion hat die Parameter Vorname und Nachname und soll beide verkettet auf der Konsole ausgeben; wobei
#  vorher und nachher jeweils Sterne in der Länge der Verkettung aufzubereiten sind.

merge_str = lambda first_name, last_name: first_name + last_name

# erfassen des Vornamens
first_name = input("Wie ist Ihr Vorname? ")
# erfassen des Nachnamens
last_name = input("Wie ist Ihr Nachname? ")
# ermitteln der Sternanzahl
count_star = len(merge_str(first_name, last_name)) * "*"

# ergebnis
print(f"{count_star}\n{merge_str(first_name, last_name)}\n{count_star}")
