import tkinter
from tkinter import ttk, END

# TODO: Berechnung des Umfangs und der Fläche eines Rechtecks sind zwei Funktionen zu definieren. Die Funktionen sind mit verschiedenen
#  Werten zu testen.

# Funktionen
def schliessen(main_window):
	main_window.destroy()


def berechnung_umfang(laenge_input_entry, breite_input_entry):
	"""Diese Funktion berechnet gemäß User Input den Umfang eines Dreiecks."""
	# Speichern und änderung der eingaben ("," → "."), sowie änderung des Datentyps von "str" → "float"
	laenge = laenge_input_entry.get().replace(",", ".")
	breite = breite_input_entry.get().replace(",", ".")
	laenge = float(laenge)
	breite = float(breite)

	# Berechnung des Umfangs und austausch des "." → ","
	umfang = 2 * (laenge + breite)
	umfang = str(umfang)
	umfang = umfang.replace(".", ",")

	# Ausgabe das Ergebnis
	erg_output_label.configure(
		text=f"Der Umfang des Rechtecks mit einer Länge von {laenge_input_entry.get()} cm &\neiner Breite von "
			 f"{breite_input_entry.get()} cm beträgt {umfang} cm!")


def berechnung_flaeche(laenge_input_entry, breite_input_entry):
	"""Diese Funktion berechnet gemäß dem User Input eines Dreiecks"""
	# Speichern und änderung der eingaben ("," → "."), sowie änderung des Datentyps von "str" → "float"
	laenge = laenge_input_entry.get().replace(",", ".")
	breite = breite_input_entry.get().replace(",", ".")
	laenge = float(laenge)
	breite = float(breite)

	# Berechnung der Fläche und austausch des "." → ","
	flaeche = laenge * breite
	flaeche = str(flaeche)
	flaeche = flaeche.replace(".", ",")

	# Ausgabe das Ergebnis
	erg_output_label.configure(
		text=f"er Umfang des Rechtecks mit einer Länge von {laenge_input_entry.get()} cm &\neiner Breite von "
			 f"{breite_input_entry.get()} cm beträgt {flaeche} cm!")


def loeschen(laenge_input_entry, breite_input_entry, erg_output_label):
	"""Diese FUnion löscht die aktuellen Eingaben und Berechnung!"""
	laenge_input_entry.delete(0, END)
	breite_input_entry.delete(0, END)
	erg_output_label.configure(text="Bitte geben Sie die Länge und Breites des zu berechnenden Dreiecks an!")


# GUI & Nutzer Eingabe

main_window = tkinter.Tk()
main_window.title("Dreiecks Rechner")

# Erstellung des Abschnitts "User Input"
user_input_labelframe = ttk.Labelframe(main_window, text="Nutzer Eingaben:")
user_input_labelframe.grid(row=0, column=0, padx=10, pady=10)

# Erfassung der "länge" & "breite" des Rechtecks als "str"
laenge_input_label = ttk.Label(user_input_labelframe, text="Bitte geben Sie die Länge des Rechtecks in cm an:")
laenge_input_label.grid(row=1, column=0, padx=10, pady=5)
laenge_input_entry = ttk.Entry(user_input_labelframe)
laenge_input_entry.grid(row=2, column=0, padx=5, pady=(5, 10))

breite_input_label = ttk.Label(user_input_labelframe, text="Bitte geben Sie die Breite des Rechtecks in cm an:")
breite_input_label.grid(row=3, column=0, padx=10, pady=5)
breite_input_entry = ttk.Entry(user_input_labelframe)
breite_input_entry.grid(row=4, column=0, padx=10, pady=(5, 10))

# Erstellung des Abschnitts "Ergebnis"
erg_output_labelframe = ttk.Labelframe(main_window, text="Ergebnis:", width=600)
erg_output_labelframe.grid(row=1, column=0, padx=10, pady=10)

# Ausgabe des Umfangs / der Fläche des Dreiecks
erg_output_label = ttk.Label(erg_output_labelframe, text="Bitte geben Sie die Länge und Breites des zu berechnenden Dreiecks an!")
erg_output_label.pack()

# Erstellung des Abschnitts "Buttons"
btn_frame = ttk.Frame(main_window)
btn_frame.grid(row=2, column=0, padx=10, pady=10)

# Erstellung der Buttons
# "Lambda" ist eine anonyme Funktion und kann beliebig viele Argumente aufnehmen, jedoch nur einen Ausdruck. Huch verstehe ich
# nicht wirklich...
berechnen_btn = ttk.Button(btn_frame, text="Umfang berechnen", command=lambda: berechnung_umfang(laenge_input_entry,
																						   breite_input_entry))
berechnen_btn.grid(row=0, column=0, padx=10, pady=10)

berechnen_btn = ttk.Button(btn_frame, text="Fläche berechnen", command=lambda: berechnung_flaeche(laenge_input_entry,
																						   breite_input_entry))
berechnen_btn.grid(row=0, column=1, padx=10, pady=10)

loeschen_btn = ttk.Button(btn_frame, text="Löschen", command=lambda: loeschen(laenge_input_entry, breite_input_entry,
																		 erg_output_label))
loeschen_btn.grid(row=0, column=2, padx=10, pady=10)

schliessen_btn = ttk.Button(btn_frame, text="Schließen", command=lambda: schliessen(main_window))
schliessen_btn.grid(row=0, column=3, padx=10, pady=10)

# Sizegrip-Widget hinzufügen
# "relx" bedeutet: Die relative horizontale Position des Widgets innerhalb seines Elternwidgets, ausgedrückt als Bruchteil der
# Breite des Elternwidgets (0.0 bedeutet links, 1.0 bedeutet rechts)
# "rely" bedeutet: Die relative vertikale Position des Widgets innerhalb seines Elternwidgets, ausgedrückt als Bruchteil der
# Höhe des Elternwidgets (0.0 bedeutet oben, 1.0 bedeutet unten)
sizegrip = ttk.Sizegrip(main_window)
sizegrip.place(relx=1.0, rely=1.0, anchor="se")

main_window.mainloop()
