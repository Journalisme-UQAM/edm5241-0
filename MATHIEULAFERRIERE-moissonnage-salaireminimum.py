# coding utf-8

# Mathieu Laferriere script python octobre 2k16

# ecrire directement dans le terminal = virtualenv -p /usr/bin/python3 py3env
# cela crée le type d'environnement dans lequel les commandes python seront exécutées

# ecrire directement dans le terminal = source py3env/bin/activate
# cela rend le nouveau type d'environnement actif

# let the fun begin

import csv
import requests
#from bs4 import BeautifulSoup
#donc ici import API
#a ce que je comprends, bs4, avec sa fonction de parsing, est le pain
#et le beurre avec l'API de mon site. Impératifs pour moissonner les données

url = "http://www.cnt.gouv.qc.ca/salaire-paie-et-travail/salaire/historique-du-salaire-minimum/"
#url ici est une variable, on aurait pu l'appeler x aussi, comme en maths.
#elle simplifie l'écriture des commandes. url au lieu de l'adresse web complete

fichier = "histosalaires.csv"
#les données moissonnées, du tableau de la cnesst, seront accumulées ici

entetes = {
	"User-Agent":"Mathieu L - Requête envoyée dans le cadre d'un cours de journalisme informatique à l'UQAM (EDM5240)",
	"From":"laferriere.mathieu@courrier.uqam.ca"
}
#simple identification pour les hosts, les hébergeurs du site web,
#pour ne pas être pris pour une attaque


#Alors un test préalable
#commande exécutée dans le terminal en bas : 
#résulat = ImportError: No module named 'bs4'
# il ne reconnait pas bs4.
#essayons de continuer quand même

contenu = requests.get(url, headers=entetes)
#a ce que j'ai compris, le .get ici est l'action nous permettant d'aller moissonner les données,
#de nous brancher concretement aux données du site.

page = BeautifulSoup(contenu.text,"html.parser")
#opération de parsage. autrement dit, de mettre le contenu html dans le 'contenant'
# ici, le contenant est la variable 'page'

print = page

#imprimons ici la page pour voir si les informations attendues défilent convenablement
#évidemment, on bloque encore a 'error import bs4 soup'
#essayons de mettre en commentaire l'action 'from bs4 import BeautifulSoup'
#YES, LES DONNÉES APPARAISSENT. Je ne m'aurais jamais attendu a ce que
#ces données apparaissent.
#cependant erreur  :
#(Caused by <class 'socket.gaierror'>: [Errno -5] No address associated with hostname)
#pourquoi mon fichier histosalaires.csv. n'apparait pas?
#je l'ai pourtant créé!

i = 0
i = 1

#car sur les 2 premieres rangées du tableau, aucune données
#la fameuse boucle pour consulter d'une certaine façon le résultat du moissonnage

for ligne in page.find_all("tr"):
    
      if i !=  [0,1]:
          #comme je l'ai dit, on ne veut pas la premiere ni la deuxieme rangée du tableau
          #il faut 'append' maintenant, notre but après tout étant de chercher les variables
          a="type de salaire"
          b="années"
          if item.td is not None:
              salaire.append(item.td.text)
          #car certaines cellules, comme pour le salaire en industrie du 
          #vêtement avant mai 2003, sont vides, il faut faire ainsi
          else:
                salaire.append(None)
                #ainsi il n'ira pas chercher les données des cellules vides, car elles n'existent pas
                
                #si l'on exécute, plus rien ne marche, 
                #le message est le suivant :
                #Traceback (most recent call last):
  File "moissonnage-salaireminimum.py", line 45, in <module>
    page = BeautifulSoup(contenu.text,"html.parser")
NameError: name 'BeautifulSoup' is not defined

#derniere étape ici, si ça avait marché, j'aurais créé un fichier-tableau pour 
#y inscrire les salaires

                
                
          
          
