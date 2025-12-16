# Exo 1 :
# A l'aide d'une boucle, parcourir la liste suivante à la recherche de l'intrus
# Une fois l'intrus trouvé, printer "intrus trouvé!" et sortir de la boucle
liste = ["bernard", "gérard", "gontran", "jacqueline", "intrus", "nadia", "jack"]

for name in liste:
        if name == "intrus":
                print("intrus trouvé!")
                break

# Exo 2 :
# Sans utiliser la fonction sum(), retourner la somme de la liste suivante à l'aide d'une boucle
liste_somme = [12.3, 34, 1, 0.4, 23, -17, 76, -300.2]
somme = 0

for nb in liste_somme:
        somme += nb
print(somme)


# Exo 3 :
# A l'aide d'une boucle et d'une range, calculer le factoriel de 10 (Résultat: 3 628 800) (1*2*3*4*5*6*7*8*9*10)
# Le factoriel d'un entier n est le produit des nombres entiers strictement positifs inférieurs ou égaux à n
# Printer le résultat
list3 = list(range(2, 11))
facto = 1

for nb in list3:
        facto *= nb
print(facto, facto == 3_628_800)

# Exo 4 :
# A l'aide d'une boucle while, demander à l'utilisateur de "Taper oui, ou non.", et tant que ce dernier n'a pas tapé "non", continuer de lui demander "Taper oui, ou non."
# Si l'utilisateur ne tape ni "oui", ni "non", continuer la boucle en lui mettant un message d'erreur car l'input est invalide

answer = "oui"

while answer != "non":
        if answer != "oui" and answer != "non":
                print("Erreur, vous devez écrire oui ou non!")
        answer = input("Tappez oui, ou non. ")

# Exo 5 :
# A partir de la liste suivante printer le résultat suivant à l'aide d'une boucle :
# "L'élément à l'index 0 est a"
# "L'élément à l'index 1 est 3"
# "L'élément à l'index 2 est True"
# ...
ma_liste = ['a', 3, True, "coucou", 'r', 3.14, [1, 2, 3]]

for item in ma_liste:
        print(f"L'élément à l'index {ma_liste.index(item)} est {item}")

# Exo 6 :
# A l'aide d'une compréhension de liste générer une nouvelle liste suivant les règles suivante :
# Si le chiffre est un multiple de 5, le multiplier par 2
# Sinon, retourner sa division entière par 3
# Printer la nouvelle liste obtenue
liste_de_base = [23, 1, 27, 28, 3, 4, 763, 12, 90]
new_list = [x * 2 if x % 5 == 0 else x // 3 for x in liste_de_base]

print(new_list)

# Exo 7 :
# A l'aide d'une compréhension de liste et de all() printer une fois True ou False si toutes les chaînes de caractères contenues dans la liste sont des palindromes.
palindrome = ["kayak", "coloc", "malayalam", "pop", "erre"]
is_palindrome = all([word[:] == word[::-1] for word in palindrome])

print(is_palindrome)

# Exo 8 :
# A l'aide de boucles imbriquées, créer une nouvelle liste "flat", qui sera une liste applatie de "liste", 
# ayant les éléments classés dans l'ordre décroissant : [7, 6, 5, 4, 3, 2, 1]
liste8 = [1, 3, 7, [4, 6, [5, 2]]]

flat = []

for root_item in liste8:
        if isinstance(root_item, list):
            for child_item in root_item:
                    if isinstance(child_item, list):
                            flat.extend(child_item)
                    else:
                            flat.append(child_item)
        else:
                flat.append(root_item)

flat.sort(reverse=True)

print(flat)