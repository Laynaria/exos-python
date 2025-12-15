# Exo 1
# Demander à l'utilisateur de taper un nombre
nombre = input("Tappez un nombre ")
try :
    nombre = int(nombre)
# Si celui-ci est pair, printer "Vous avez entré un nombre pair."
    if (type(nombre) == int and nombre % 2 == 0) :
        print("Vous avez entré un nombre pair.")
# Si celui-ci est impair, printer "Vous avez entré un nombre impair."
    elif (type(nombre) == int and nombre % 2 != 0) :
        print("Vous avez entré un nombre impair.")
# Si l'information entrée n'est pas un nombre printer "Vous devez entrer un nombre!"
except :
    print("Vous devez entrer un nombre!")

# Exo 2
# Demander à un utilisateur de taper un mot
mot = input("Tappez un mot ")
# Si celui-ci possède la lettre e OU la lettre a printer "Beep"
# Si celui-ci possède la lettre e OU la lettre a, mais sans que les deux conditions soit vraies en même temps, printer "Boop"
if (("e" in mot and "a" not in mot) or ("a" in mot and "e" not in mot)) :
    print("Boop")
elif ("e" in mot or "a" in mot) :
    print("Beep")

# Exo 3 - Optionnel
# A l'aide d'un match case et d'une boucle, printer "RGB" lorsque la couleur présente dans la liste suivante est une couleur au format RGB (Red Green Blue), et
# printer "RGBA" lorsque la couleur est au format RGBA (Red Green Blue Alpha).

# Si r, g, et b sont égaux à 0 (quelque soit le format de la couleur), alors il faudra printer "Couleur noire" en priorité seulement si la valeur d'alpha (si elle
# existe) est supérieure à 0

# Si r, g, et b sont égaux à 255 (quelque soit le format de la couleur), alors il faudra printer "Couleur blanche" en priorité seulement si la valeur d'alpha (si
# elle existe) est supérieure à 0

# Résultat attendu: RGB RGBA RGB de couleur noire RGBA RGBA RGBA de couleur blanche RGBA
colors = [(12, 72, 89), (23, 77, 200, 1), (0, 0, 0), (123, 123, 67, 1), (255, 255, 255, 0), (255, 255, 255, 1), (0, 0, 0, 0)]
for color in colors:
    match color:
        case [R, G, B] if R == 0 and G == 0 and B == 0:
            print("Couleur noire")
        case [R, G, B] if R == 255 and G == 255 and B == 255:
            print("Couleur blanche")
        case [R, G, B, A] if R == 0 and G == 0 and B == 0 and A > 0:
            print("Couleur noire")
        case [R, G, B, A] if R == 255 and G == 255 and B == 255 and A > 0:
            print("Couleur blanche")
        case [R, G, B]:
            print("RGB")
        case [R, G, B, A] :
            print("RGBA")
        # Ecrire le code ici
