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
import zipfile

root = zipfile.ZipFile("sources.zip", "r")
root.extractall()
# A l'aide du module pathlib, ou os, et d'une boucle, créer un trieur de fichier qui va répartir les fichiers extraits en 5 dossiers (Musique, Videos, Images, 
# Documents, Divers) selon les règles suivantes
root = Path("data") # importé de l'exo 1

musique = root.joinpath("Musique")
videos = root.joinpath("Videos")
images = root.joinpath("Images")
documents = root.joinpath("Documents")
divers = root.joinpath("Divers")
# 1. mp3, wav, flac : Musique
# 2. avi, mp4, gif : Videos
# 3. bmp, png, jpg : Images
# 4. txt, pptx, csv, xls, odp, pages : Documents
# 5. autres : Divers

for file in root.iterdir():
    if file.is_file():
        match file.suffix:
            case ".mp3" | ".wav" | ".flac":
                musique.mkdir(exist_ok=True)
                file.rename(musique / file.name)
            case ".avi" | ".mp4" | ".gif":
                videos.mkdir(exist_ok=True)
                file.rename(videos / file.name)
            case ".bmp" | ".jpg" | ".png":
                images.mkdir(exist_ok=True)
                file.rename(images / file.name)
            case ".txt" | ".pptx" | ".csv" | ".xls" | ".odp" | ".pages":
                documents.mkdir(exist_ok=True)
                file.rename(documents / file.name)
            case _:
                divers.mkdir(exist_ok=True)
                file.rename(divers / file.name)