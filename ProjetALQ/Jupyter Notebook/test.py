import pandas as pd
import random as rd
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

filename = "Commandes_clients.csv"
df = pd.read_csv(filename)

print(df.head(10))

remises = [70, 40, 20, 20, 20, 60, 40, 30, 10, 60, 80, 30]
produit = [ 6,  6,  7,  2,  8,  3,  8,  5,  1, 10,  3,  5]
client =  [75, 14, 35, 38, 75, 15,  5, 98, 87, 54, 75, 25]
df_remises = pd.DataFrame({'Remise': remises,'IdProduit': produit, 'IdClient': client})
print(df_remises.head(12))

prix =      [83, 24, 34, 95, 82,  3, 18, 29, 95, 63]
marge =     [ 3, 10, 23, 61,  8, 50,  8, 20, 11, 37]
nom =       ["Colle", "Clous", "Choux", "Café", "Craies", "Chaudron", "Clefs", "Cavalier", "Chauffeur", "Clés"]
Idproduit = [i for i in range(1, 11)]
df_produit = pd.DataFrame({'Prix': prix,'Marge': marge, 'Nom': nom}, index=Idproduit)
print(df_produit.head(10))

cost = [df["Quantite"][i]*df_produit["Prix"][df["IdProduit"][i]] for i in df.index]

df["Cost"] = cost

df_importance = df.groupby(["IdClient"]).sum().sort_values(by="Cost", ascending=False)

nomClient = ["Client n°{}".format(i) for i in range(1, 101)]
nomClient[75] = "Culturo"
nomClient[14] = "Fnic"
nomClient[35] = "Garty"
nomClient[38] = "Habitons"
nomClient[85] = "Auchun"
nomClient[15] = "Unionmarché"

NomClient_importance = [nomClient[i] for i in list(df_importance.index)]
df_importance["Nom"] = NomClient_importance

print(df_importance)

#def de la fonction qui récupère l'élément selectionné
def action(ev):
    
    select = listeCombo.get()
    print("Vous avez selectionné : '",select,"'" )
    idselect = nomClient.index(select)
    
    root2 = tk.Tk()
    
    
    
    total = df["Cost"].sum()
    explosion = [0] * df_importance.shape[0]
    explosion[list(df_importance.index).index(idselect)] = 0.15
    camLabel = []
    for i in list(df_importance.index):
        camLabel.append(nomClient[i])

    fig, axis = plt.subplots()
    axis.pie(df_importance["Cost"], labels = camLabel, explode = explosion)
    canvas = FigureCanvasTkAgg(fig,master=root2)
    canvas.draw()
    tk.mainloop()

#creation de la combobox
root = tk.Tk()
root.geometry('200x200')

choixLabel = tk.Label(root, text = "Veuillez choisir un client !")

choixLabel.pack()
#ajout de la liste des clients dans la combobox 
listeCombo = ttk.Combobox(root, values=NomClient_importance)

listeCombo.current(0)

listeCombo.pack()
listeCombo.bind("<<ComboboxSelected>>",action)

root.mainloop()

