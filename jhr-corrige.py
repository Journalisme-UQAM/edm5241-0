# coding utf-8

import csv
import requests
from bs4 import BeautifulSoup

url = "http://www.cnt.gouv.qc.ca/salaire-paie-et-travail/salaire/historique-du-salaire-minimum/"
# Je salue ton effort d'avoir cherché des données ailleurs.
# Cette page est cependant trop simple pour exiger un script. Un simple copié collé peut suffire.

fichier = "histosalaires-JHR.csv"

entetes = {
	"User-Agent":"Mathieu L - Requête envoyée dans le cadre d'un cours de journalisme informatique à l'UQAM (EDM5240)",
	"From":"laferriere.mathieu@courrier.uqam.ca"
}

contenu = requests.get(url, headers=entetes)
page = BeautifulSoup(contenu.text,"html.parser")

# print = page # Ici tu as écrit «print = page», ce qui crée une variable appelée «print» et y copie le contenu de la variable «page»
# print(page)

i = 0
i = 1 # après ces deux lignes, i est égal à 1

for ligne in page.find_all("tr"):
	# if i !=  [0,1]: # Ici, cette syntaxe ne marche pas. Si tu veux dire «si i n'égale ni 0 ni 1», il faut les écrire un après l'autre, séparés par un «or» (ou), comme tu le vois sur la ligne suivante:
	# if i != 0 or i != 1:  # Cependant, ici, comme i est égal à 1, ta condition est toujours vraie (i est toujours différent de 0), puisque tu n'augmentes pas la valeur de i plus loin dans ton script
	# Ici, ce qu'il faut faire, si on veut sauter les 2 premières lignes, c'est de dire: «si i est plus grand que 2 (dans la mesure où tu as donné à i la valeur de 1 en partant)
	if i > 2:

		annee = [] # La variable que je crée, ici, je vais l'appeler «année», puisque chaque ligne représente une année

		date = ligne.th.text  # Dans la page qui t'intéresse, le texte de la première colonne est contenu dans un élément HTML <th>
		print(date)
		annee.append(date)

		for item in ligne.find_all("td"): # Les trois autres colonnes contiennent chacune un <td> dont on peut extraire le texte avec cette boucle
			print(item.text)
			annee.append(item.text)

		a="type de salaire" # Ici, je comprends ce que tu as cherché à faire avec les variables «a» et «b», mais la bonne façon de faire est décrite ci-dessus
		b="années"

		print(annee)

		lemec = open(fichier,"a")
		gino = csv.writer(lemec)
		gino.writerow(annee)

	i += 1 # Il manquait l'augmentation du compteur