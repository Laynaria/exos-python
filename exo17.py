from pprint import pprint
mes_sites = {
 0: {
 "nom": "Mon super site",
 "url": "https://monsupersite.com",
 "utilisateurs": [
 {
 "nom": "Germain",
 "prenom": "Philibert",
 "date_naissance": "1984-12-12",
 "nombre_abonnes": 87621
 },
 {
 "nom": "Kaas",
 "prenom": "Patricia",
 "date_naissance": "1978-03-26",
 "nombre_abonnes": 124
 },
 {
 "nom": "Pipoude",
 "prenom": "Serges",
 "date_naissance": "1999-01-03",
 "nombre_abonnes": 7761287
 }
 ]
 },
 1: {
 "nom": "Mon site génial",
 "url": "https://monsitegenial.com",
 "utilisateurs": [
 {
 "nom": "Sbai",
 "prenom": "Nadia",
 "date_naissance": "1978-04-01",
 "nombre_abonnes": 7627
 },
 {
 "nom": "Koch",
 "prenom": "Christine",
 "date_naissance": "2001-12-07",
 "nombre_abonnes": 8727193
 }
 ]
 }
}
# Contrainte : les codes proposés doivent fonctionner quelque soit le nombre de site et d'utilisateurs dans le dictionnaire.

# Exo 1 :
# Ajouter un nouvel utilisateur à "Mon super site" avec le nom, prénom, date de naissance et nombre d'abonnés de votre choix et printer le dictionnaire obtenu 
# avec pprint pour obtenir un résultat plus lisible
mes_sites[0]["utilisateurs"].append( {
 "nom": "Georgie",
 "prenom": "Grossier",
 "date_naissance": "1989-03-03",
 "nombre_abonnes": 1565651516156
 })

pprint(mes_sites)

# Exo 2 :
# Supprimer l'abonnée Patricia Kaas et printer le dictionnaire obtenu avec pprint
del mes_sites[0]["utilisateurs"][1]
pprint(mes_sites)


# Exo 3 :
# Retourner la somme du nombre d'abonnés de tous les utilisateurs de tous les sites à l'aide d'une boucle
# Printer le résultat (16583728 sans votre utilisateur créé)
total = 0
for current_site in mes_sites.values():
    for utilisateur in current_site["utilisateurs"]:
        total += utilisateur["nombre_abonnes"]

print(total, total == 16583728 + 1565651516156)
        

# Exo 4 :
# Retourner la moyenne des âges en années des utilisateurs
# Printer le résultat (~32.5 sans votre utilisateur créé)
from datetime import datetime

now = datetime.now()

moyenne = 0
nbr_utilisateurs = 0

for current_site in mes_sites.values():
    for utilisateur in current_site["utilisateurs"]:
        age = (now - datetime.fromisoformat(utilisateur["date_naissance"])).days // 365

        moyenne += age
        nbr_utilisateurs += 1

print(total / nbr_utilisateurs)