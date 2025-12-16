# Exo 1:
# 1. Créez une fonction `addition` qui prend un nombre variable d'arguments et retourne leur somme. Testez la fonction.
def addition(*args):
    somme = 0;
    for arg in args:
        somme += arg
    return somme

print(addition(1, 2, 3, 4))

# 2. Créez une fonction `liste_arguments` qui prend un nombre variable d'arguments et les affiche. Testez la fonction.
def liste_arguments(*args):
    for arg in args:
        print(arg)

liste_arguments("a", "zerty", "salut")

# Exo 2:
# 1. Créez une fonction `infos_personnelles` qui prend un nombre variable d'arguments par mot-clé et affiche ces informations. Testez la fonction.
def infos_personnelles(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

infos_personnelles(nom="Roger", age=150, is_ready=False)
infos_personnelles(nom="Alice", age=49, is_ready=True)

# 2. Créez une fonction `multiplication_kwargs` qui multiplie les valeurs des arguments par mot-clé qui sont des nombres. Testez la fonction.
# Exemple :
def multiplication_kwargs(**kwargs):
    multiply = 1
    for key, value in kwargs.items():
        if isinstance(value, int):
            multiply *= value
    return multiply

print(multiplication_kwargs(a=2, b=3, c=4)) # 2 * 3 * 4 => 24
print(multiplication_kwargs(a=2, b="toto", c=4)) # 2 * 4 => 8

# Exo 3:
# 1. Créez une fonction `affiche_details` qui accepte un argument positionnel, un
# nombre variable d'arguments positionnels et un nombre variable d'arguments par
# mot-clé. Testez la fonction.
def affiche_details(arg1, *args, **kwargs):
    print(f"arg1 : {arg1}")
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
            print(f"{key} : {value}")

affiche_details("salut", 12, "magie", nom="minestrone", age=67, is_ready=True)
affiche_details(67, "nope", "arrêtez", False, nomination=False, name="Silksong", story="Il était une fois", bad_number = 33)