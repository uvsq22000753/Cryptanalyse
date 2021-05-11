# NOM_ELEVE = "LARA ESPINASSE"

alphabet=[]
table_occurence_triee= []
texte_dechiffre = ""


texte3           = "dceuq e n ehfp cg p kyhhep uqfw cgiy citudm c gzudiq ni ezhd px c jhptv ep cggsht  kg hdtymdt xdzei gdx rzyq wir mvzxpw  cifcchdb znwd ccyw wy lkcsht  dp isgd uqfw wy ?"
#texte3_decrypte = "bravo a l'aide de l'indice vous avez reussi a casser ce code et a finir ce devoir. le dernier texte est pour les braves, regardez vous dans un miroir, en etes vous un ?"

#Fonction qui identifie les cles possibles en se basant sur la fréquence des lettre en fonction
#de la possition du rang de la clé et l'occurrence théorique du e.
def DecodeVigenereCle (texte, l_cle) :
    
    #alpha contient l'alphabet
    alpha = "abcdefghijklmnopqrstuvwxyz"
    cle = ""
    
    for i in range (0, l_cle) :

        nombre = [ 0 for a in alpha] # cree un tableau vide de la longueur de l'alphabet qui servira a compter
        sous = texte[i:len (texte):l_cle] # recupere tout les lettres en fonction de la taille de l'indice i, i+4,i+8 pour une cle de 4
        sous = ''.join([i for i in sous if i.isalpha()]); # supprime tout ce qui est pas alpha pour pas polluer
        print("\n liste des lettres de la cle "+ str(i) +"\n ="+ sous)    

        for k in sous : 
            nombre [ alpha.find (k) ] += 1 # compte les lettres
        print("\nnombre d'occurence des lettres")
        print(nombre)

        # recupere le rang de la lettre apparaissant le plus souvent
        p = 0
        for k in range (0, len (nombre)) : 
            if nombre [k] > nombre [p] :
                 p = k
        print("la 1er occurence la plus elevée p = "+str(p))

        for k in range (0, len (nombre)) :
            if nombre [k] == nombre [p] : # on recupere les lettres les plus representée
                cle += alpha [ (k + 26 - alpha.find ("e")) % 26 ] # on code ces lettres en partant de l'hypotèse que c'est un 'e'
        cle +='/' # separateur
        print("cle possible = "+str(cle))
    return cle

#decode le texte en fonction de la clé sur le principe du codage Cesar
def decode_vigenere(texte,cle):
    message_decode=""
    for i,c in enumerate(texte):
        #si la lettre n'est pas alphabétique on remet le meme caractère
        if  ord(c) < 97 or ord(c) > 122:
            message_decode += c
        #sinon on décode le caractère en fonction de la possition dans la clé
        else:
            d = cle[i%len(cle)]
            d = ord(d)-97
            d = 26 - d
            message_decode +=chr((ord(c)-97+d)%26+97)
    return(message_decode)

#fonction qui exploite la liste des clés possible
# Remarque : je n'ai ecrit la boucle , j'ai codé en dur les clés possible
def exploite_cle(texte,liste_cle):
    
    print("\non sait que la premier lettre et un 'c'")
    #il reste donc comme clé possible :
    cle_possible = ["cyez","czez","clez","cuez"]
    #essaye les clés une par une
    for i in cle_possible:
        print("\cle = " + i + "==> "+ decode_vigenere(texte,i))

#fonction qui vide le tableau alphabet   
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

#fonction qui trier le tableau "alphabet" de l'occurence la plus elevée à la plus faible
def tri(alphabet):
            
    return(sorted(alphabet,key = lambda item : (item[1],item[0]), reverse =True))

def decrypte_texte_3():
    cle_code = "clez"
    texte_decode = ""
    cle_decode_vig =""

    #calcul l'occurence des lettres dans le texte
    nbrOccur(texte3)
    table_occurence_triee= tri(alphabet)
    print("table des occurences = ")
    print(table_occurence_triee)

    #HYPOTHESE POUR LIMITER LE CODE
    #j'ai déduit la longueur de la clé en repérant les lettre seules qui correspondent
    # a un 'a' dans la langue francaise.
    # si les lettres sont les memes ==> on a identifié une lettre de la clé 
    #la difference entre les deux occurrences donne le multiple de la clé
    #ici 'c' a la 45 et 65eme position ==> 20 caractères entre ==> cle de 2,4 ou 5
    # le 'c' devient 'a'

    #Décodage de la clé de valeur 4
    cle_decode_vig = DecodeVigenereCle(texte3,4)

    #exploiation des clés pour décoder le texte 
    exploite_cle(texte3,cle_decode_vig)  
     

    #la clé est : "clez" 

    texte_decode = decode_vigenere(texte3,cle_code)
    print("\nCLE = ", str(cle_code))
    print("\nTEXTE DECODE FINAL= "+ texte_decode)
    


decrypte_texte_3()
