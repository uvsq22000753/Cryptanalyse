from operator import itemgetter,attrgetter
import tkinter as tk

alphabet=[]
table_occurence_triee= []
texte_dechiffre = ""

#voyelle et consomme triés par occurence dans la langue francaise
voyelle = 'eaiou'
consonne= 'snrtdcmpgbvhfqyxjkwz'
occurrence_langue='eaisnrtoludcmpgbvhfqyxjkwz'
digramme =['es','le','en','de','re','nt','on','te','re','se']



texte1 ="gx qosvlnkd wkvlkxo xiu vscx qno yd fsu cx qniix cx unkggx kdvsddyx xu vsdukxdu g'kdckvx. gxi gxuuoxi cy fsu cx qniix qxofxuuxdu cx cxvngxo gxi gxuuoxi cy fxiinmx sokmkdng fscygs 26. ixygxi gxi gxuuoxi cx n n a isdu vlkwwoxxi."
texte_decrypte ="Le prochain fichier est code par un mot de passe de taille inconnue et contient l'indice. les lettres du mot de passe permettent de decaler les lettres du message original modulo 26. seules les lettres de a a z  sont chiffrees"

def alphabet_vide():
    for i in range(97,123):
        alphabet.append([chr(i), 0])

#fonction qui commpte le nombre d'occurence de chaque lettre dans le texte
def nbrOccur (texte) :
    vide()
    for c in texte:
        if 97 <= ord(c) <= 122 : #On verifie si c'est une lettre en minuscule
            alphabet[ord(c)-97][1] += 1 #/len(texte)
          
#fonction qui remet a zera le tableau alphabet   
def vide() :
    for x in alphabet:
        x[1]=0.0


alphabet_vide()
nbrOccur(texte1)


#print(alphabet)

#a :      b :     c : D      d : N       e :
#f : M    g : L   h :        i : S       j :
#k : I    l : H   m : G      n : A       o : R
#p :      q : P   r :        s : O       t :
#u : T    v : C   w : F      x : E       y : U

#x, u, i, g, k = c = d, n = s = o, v, y, f = q, l = w, m, a 

#fonction qui trier le tableau "alphabet" de l'occurence la plus elevée à la plus faible
def tri(alphabet):
            
    return(sorted(alphabet,key = lambda item : (item[1],item[0]), reverse =True))

table_occurence_triee= tri(alphabet)
print(table_occurence_triee)

#Fonction qui remplace dans tout le texte la lettre 1 par la lettre 2 et retour la chaine modifiée
def remplace_lettre(texte, lettre1, lettre2):
    res = ""
    i = 0
   
    while (i < len(texte)): # tant que i n'est pas equivalent à la longeur du texte
        if texte[i] == lettre1: # si la lettre est équivalent a la lettre codée
            res += lettre2 # on remplace par la lettre décodée
        else:
            res+= texte[i] #sinon on place la lette d'origine
        i+=1 #passe au caratere suivant du texte
    return(res) # retour le texte modifié avec le bon decodage



def decrypte():
    i=0
    j=0
    texte_transite = ""
    #remplacement de base de la lettre ayant le plus d'occurence par la lettre 'e'
    lettre_x = table_occurence_triee[0][0]
    texte_dechiffre = remplace_lettre(texte1,lettre_x,'e')
    #Hypothèse 1 , la lettre devant l'apostrophe est un 'l'
    texte_transite = remplace_lettre(texte_dechiffre,'g','l')
    #remplacer tout les occurences les plus importantes derrière le 'e' pour utiliser les digrammes
    texte_dechiffre = remplace_lettre(texte_transite,'u','s')
    print("\ntexte avec u en s = " + texte_dechiffre)
    texte_dechiffre = remplace_lettre(texte_transite,'i','s')
    print("\ntexte avec i en s = " + texte_dechiffre)

    #on choisi donc le i en s
    #on poursuit avec le u en t 
    texte_dechiffre = remplace_lettre(texte_dechiffre,'u','t')
    print("\ntexte avec u en t = " + texte_dechiffre)
    #le o en r
    texte_dechiffre = remplace_lettre(texte_dechiffre,'o','r')
    print("\ntexte avec o en r = " + texte_dechiffre)
    #le y en u
    texte_dechiffre = remplace_lettre(texte_dechiffre,'y','u')
    print("\ntexte avec y en u = " + texte_dechiffre)
    #le c en d
    texte_dechiffre = remplace_lettre(texte_dechiffre,'c','d')
    print("\ntexte avec c en d = " + texte_dechiffre)
    #le n en a 
    texte_dechiffre = remplace_lettre(texte_dechiffre,'n','a')
    print("\ntexte avec n en a = " + texte_dechiffre)
    #le k en i
    texte_dechiffre = remplace_lettre(texte_dechiffre,'k','i')
    print("\ntexte avec k en i = " + texte_dechiffre)
    #le f en m
    texte_dechiffre = remplace_lettre(texte_dechiffre,'f','m')
    print("\ntexte avec f en m = " + texte_dechiffre)
    #le q en p
    texte_dechiffre = remplace_lettre(texte_dechiffre,'q','p')
    print("\ntexte avec q en p = " + texte_dechiffre)
    #le v en c
    texte_dechiffre = remplace_lettre(texte_dechiffre,'v','c')
    print("\ntexte avec v en c = " + texte_dechiffre)
    #le w en f
    texte_dechiffre = remplace_lettre(texte_dechiffre,'w','f')
    print("\ntexte avec w en f = " + texte_dechiffre)

    resultat.insert(0, texte_dechiffre)

    #utilisation des occurences ==> pas possible car le texte n'est pas assez long 
    #for i in range(1,1):
    #    for j in range(1,2):
    #        lettre_x = table_occurence_triee[i][0]
    #        texte_dechiffre = remplace_lettre(texte_transite,lettre_x,occurrence_langue[j])
    #        print("\n texte dechiffré avec la lettre consonne " + str(occurrence_langue[j])+" =" +texte_dechiffre)
        #lettre_x = table_occurence_triee[2][0]
        #texte_dechiffre = remplace_lettre(texte_dechiffre,lettre_x,'i')
    #print("\n texte dechiffré ="+texte_dechiffre)

racine = tk.Tk()
racine.title("Decryptage texte 2 ")


resultat=tk.Entry(racine,width = 50, font = ("helvetica", "20"))
resultat.grid(row=3,column=0)

label_res = tk.Label(racine, font = ("helvetica", "20"), text = "Déchiffrement ici")
label_res.grid(row = 3, column = 1)


decrypte()
racine.mainloop()
