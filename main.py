import tkinter as tk
from tkinter import ttk

# Créer la fenetre principale
root = tk.Tk()
root.title("Interface de modification sonore")
root.geometry("500x600")

# Fonction pour mettre à jour la valeur affichée du slider
def update_value(slider_id):
    def update(value):
        labels[slider_id].config(text=f"Valeur {slider_id + 1}: {int(float(value))}")
    return update

def affichageSliders():
    for i, slider in enumerate(sliders):
        print(f"Valeur du slider {i + 1}: {slider.get()}")

# Créer un cadre pour contenir les sliders
frame = ttk.Frame(root)
frame.pack(expand=True, fill='both', padx=20, pady=20)

# Créer 5 sliders avec leurs labels
sliders = []
labels = []

for i in range(5):
    # Créer un label pour afficher la valeur du slider
    label = ttk.Label(frame, text=f"Valeur {i + 1}: 50")
    label.grid(row=0, column=i, pady=10, padx=10)
    labels.append(label)

    # Créer un slider vertical
    slider = ttk.Scale(
        frame,
        from_=0,
        to=100,
        orient='vertical',
        length=300,
        command=update_value(i)
    )
    slider.set(0)
    slider.grid(row=1, column=i, pady=20, padx=10)
    sliders.append(slider)

# Créer un bouton
button = ttk.Button(root, text="Afficher les valeurs", command=affichageSliders)
button.pack(pady=20)

button = ttk.Button(root, text="Selectionner un son (.wav)", command=affichageSliders)
button.pack(pady=20)

# Lancement
root.mainloop()