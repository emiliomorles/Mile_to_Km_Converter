from tkinter import *


def mile_to_km():
    miles = float(miles_input.get())
    distance_in_km = round(miles * 1.60934)
    kilometer_result.config(text=f"{distance_in_km}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)  # This creates a space between the border and the widgets inside the window.

#  Entry
miles_input = Entry(width=5)
miles_input.grid(column=1, row=0)

# Miles Label
miles_label = Label(text="Miles", font=("Arial", 12, "bold"))
miles_label.grid(column=2, row=0)

# is equal to Label
is_equal_label = Label(text="is equal to", font=("Arial", 12, "bold"))
is_equal_label.grid(column=0, row=1)

# Kilometer_result Label
kilometer_result = Label(text="0")
kilometer_result.grid(column=1, row=1)

# Km Label
km_label = Label(text="Km", font=("Arial", 12, "bold"))
km_label.grid(column=2, row=1)

#  Button
button = Button(text="Calculate", command=mile_to_km)
button.grid(column=1, row=2)


window.mainloop()