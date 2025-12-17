# Exo 1 :
# 1. Créez un tuple avec les éléments suivants : 10, 20, 30, 40. Affichez ce tuple.
tuple1 = (10, 20, 30, 40)
print(tuple1)
# 2. Convertissez ce tuple en une liste, puis affichez cette liste.
liste = list(tuple1)
print(liste)
# 3. Modifiez le premier élément de la liste pour qu'il soit égal à 15, puis affichez la liste.
liste[0] = 15
# 4. Convertissez la liste modifiée en un nouveau tuple, puis affichez ce nouveau tuple.
newtuple = tuple(liste)
print(newtuple)


# Exo 2 :
# 1. Créez un tuple contenant une chaîne de caractères, un nombre, et une liste. Affichez ce tuple.
tuple2 = ("Il était une fois", 37, [1, 2, 3, 4, 5, 6])
print(tuple2)
# 2. Accédez au troisième élément du tuple (la liste) et modifiez son premier élément pour qu'il soit égal à 10. Affichez le tuple.
tuple2[2][0] = 10
print(tuple2)
# 3. Essayez de modifier le deuxième élément du tuple directement pour qu'il soit égal à 200. Que se passe-t-il ?
# tuple2[1] = 200
# Renvoie une erreur puisqu'un tuple est immuable, mais il semblerait qu'une liste dans un tuple n'y soit pas.

# Exo 3 Optionnel :
# 1. Créez un tuple contenant les nombres de 1 à 1_000_000. Utilisez la fonction range() pour vous aider.
tuple3 = tuple(range(1, 1_000_001))
print(tuple3[0], tuple3[-1])
# 2. DEFI : Comparez le temps de création d'un tuple et d'une liste contenant les mêmes éléments en utilisant la fonction time de la bibliothèque time.
# Note: Les résultats de temps peuvent varier en fonction de l'environnement d'exécution
import time

start_tuple = time.time()
tuple4 = tuple(range(1, 1_000_001))
end_tuple = time.time()

start_list = time.time()
list2 = list(range(1, 1_000_001))
end_list = time.time()

print(f"tuple : {end_tuple - start_tuple}")
print(f"liste : {end_list - start_list}")