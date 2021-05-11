import tkinter as tk

# NOM_ELEVE = "LARA ESPINASSE"

def rang(lettre):
    return ord(lettre)-96

def decalage(lettre1,lettre2):
    if  ord(lettre1) < 97 or ord(lettre1) > 122:
        return lettre1
    return chr((((rang(lettre1)+rang(lettre2))%26)+97))

def dec_texte(texte,cle):
    taille_cle=len(cle)
    res = ""
    i = 0
    j = 0
    while (i < len(texte)):
        res += decalage(texte[i], cle[i%taille_cle])
        i += 1
        j += 1
        if j == len(cle):
            j = 0
    return res

def chiffre():
    resultat.delete(0, tk.END)
    if (entree_texte.get() == "" + entree_cle.get() == ""):
        resultat.insert(0, "Il manque des arguments")
    else:
        resultat.insert(0,  dec_texte(entree_texte.get(), entree_cle.get()))


racine = tk.Tk()
racine.title("Cryptographie")

entree_texte = tk.Entry(racine, width = 50, font = ("helvetica", "20"))
entree_texte.grid(row = 0, column = 0)

entree_cle = tk.Entry(racine, width = 50, font = ("helvetica", "20"))
entree_cle.grid(row = 1, column = 0)

label_texte = tk.Label(racine,font = ("helvetica", "20"), text = "Entrer le message ici.")
label_texte.grid(row = 0, column = 1)

label_cle = tk.Label(racine,font = ("helvetica", "20"), text = "Entrer la clé ici.")
label_cle.grid(row = 1, column = 1)

bouton_coder=tk.Button(racine, text="Chiffrer texte",fg="black", width=15, command=chiffre)
bouton_coder.grid(row=2, column=0)

#bouton_decoder=tk.Button(racine,text="Déchiffrer texte",fg="black",  width=15,command=dechiffre)
#bouton_decoder.grid(row=2, column=1)

resultat=tk.Entry(racine,width = 50, font = ("helvetica", "20"))
resultat.grid(row=3,column=0)

label_res = tk.Label(racine, font = ("helvetica", "20"), text = "Déchiffrement ici")
label_res.grid(row = 3, column = 1)

racine.mainloop()