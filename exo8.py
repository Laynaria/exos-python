# Exo1
# En chaînant la fonction replace(), transformer la phrase suivante en "Au clair du soleil"
# Printer le résultat
base = "Au clair de la lune".replace("de la lune", "du soleil")
print(base)

# Exo2
# Compter le nombre de 'e' dans la phrase suivante et printer le résultat
phrase = "J'aime bien le python même si le snake case, ça fait bizarre au début".count("e")
print(phrase)

# Exo3
# Transformer la phrase suivante pour qu'elle devienne : "Python c'est trop cool"
# Une seule ligne de code autorisée pour la transformation
# Printer le résultat
phrase2 = " python\tc'est\ntrop cool xx".strip(" ").replace("\t", " ").replace("\n", " ").capitalize().strip(" xx")
print(phrase2)

# Exo4
# Compter le nombre de phrases dans ce texte
# Printer le résultat
texte_super_interessant = """L'ornithorynque ne peut être confondu avec aucun
autre animal. C'est un petit mammifère – il dépasse rarement 2 kg – vraiment
original, à la fourrure courte et dense et au large bec de canard.
Son pelage est typique d'une espèce aquatique. La peau est protégée par une dense
couche de poils de bourre, qui maintiennent une pellicule d'air tempéré entre elle
et l'eau. Les poils de jarre, plus longs, protègent l'ensemble. La fourrure est
presque aussi dense sur le ventre que sur le dos. Seule la couleur change.
""".count(".")

print(texte_super_interessant)