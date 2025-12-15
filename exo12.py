# Exo1
# Créer un script python écrivant 5 entiers aléatoires entre 0 et 100 dans un fichier .txt dans votre dossier 'Documents'
# Le résultat doit apparaître comme ceci: "Voici mes 5 nombres aléatoires: X, X, X, X et X"
import random as rd;
a = rd.randint(0, 100)
b = rd.randint(0, 100)
c = rd.randint(0, 100)
d = rd.randint(0, 100)
e = rd.randint(0, 100)

from pathlib import Path

chemin = "/home/laynaria-wsl/tests/tests.txt"

p = Path(chemin)
p.touch(exist_ok=True)
p.write_text(f"Voici mes 5 nombres aléatoires: {a}, {b}, {c}, {d} et {e}")

# Printer le contenu du document
print(p.read_text()) 
# Supprimer le fichier
p.unlink()

# Exo2
# Avec l'aide du module datetime, printer l'âge de la personne possédant la date de naissance suivante
date_naissance = "1998-04-23"

from datetime import date
date_naissance = date.fromisoformat(date_naissance)
today = date.today()

result = today.year - date_naissance.year - ((today.month, today.day) < (date_naissance.month, date_naissance.day))
print(result)

# Exo3
# A l'aide du module zipfile, extraire l'archives source.zip situé dans le dossier "Annexes"
# A l'aide du module pathlib, ou os, et d'une boucle, créer un trieur de fichier qui va répartir les fichiers extraits en 5 dossiers (Musique, Videos, Images, 
# Documents, Divers) selon les règles suivantes
# 1. mp3, wav, flac : Musique
# 2. avi, mp4, gif : Videos
# 3. bmp, png, jpg : Images
# 4. txt, pptx, csv, xls, odp, pages : Documents
# 5. autres : Divers