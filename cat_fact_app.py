import tkinter as tk
import requests

window = tk.Tk()

def show_cat_fact():
    try:
        cat_fact = requests.get("https://catfact.ninja/fact").json()['fact']
        fact_label.config(text=cat_fact)  # Update the label
    except requests.exceptions.RequestException as e:
        fact_label.config(text="Error fetching fact: " + str(e))


fact_label=tk.Label(window, text="")
fact_label.pack()

button = tk.Button(window, text="Cat Fact", command=show_cat_fact)
button.pack()



window.mainloop()