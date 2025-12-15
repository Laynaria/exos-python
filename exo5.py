# Exo 1 
# Initialisez une variable x avec une valeur entière.
# Utilisez la fonction id() pour afficher l'identifiant de x.
x = 3
print(id(x))

# Exo 2
# Déclarez une variable a et assignez-lui une valeur entière.
# Affectez la valeur de a à une nouvelle variable b. Affichez leurs identifiants.
# Modifiez la valeur de a et vérifiez si les identifiants de a et b ne sont plus les mêmes.
a = 5
b = a
print(id(a), id(b), sep="\n")
a = 7
print(id(a), id(b), sep="\n")

# Exo 3
# Initialisez deux variables message1 et message2 avec des chaînes de caractères différentes en même temps.
# Utilisez l'affectation parallèle pour échanger les valeurs de message1 et message2.
# Affichez les valeurs de message1 et message2 pour vérifier l'échange
message1, message2 = "ceci est un message", "ceci en est un autre"
message1, message2 = message2, message1
print(message1, message2, sep="---")