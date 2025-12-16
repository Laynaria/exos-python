# Exo 1
# Printer le nombre 5 à partir de la liste suivante
liste = [1, 2, [3, 4, [5, 6, 7]]]
print(liste[2][2][0])
# A l'aide d'une slice, extrayez 3 et 4
print(liste[2][0:2])

# Exo 2
# A partir du texte suivant, créer une liste contenant chacune des phrases
# Créer une slice regroupant les phrases du texte en inversant leur ordre d'apparition
# Joindre la slice avec un antislash pour séparateur et printer le résultat
texte = "Les Cucurbitaceae (Cucurbitacées) sont une famille de plantes dicotylédones de l'ordre des Cucurbitales, originaires pour la plupart des régions tropicales et subtropicales, qui comprend environ 800 espèces réparties en 180 genres. Ce sont généralement des plantes herbacées, annuelles ou vivaces, à port rampant ou grimpant, aux tiges munies de vrilles, et plus rarement des arbustes. Ces plantes sont sensibles au gel. Les fleurs sont unisexuées, portées parfois par les mêmes plantes (monoïques), parfois par des plantes différentes (dioïques). Les fruits sont le plus souvent des baies modifiées appelées péponides, plus rarement des fruits secs (capsules, samares). De nombreuses espèces sont cultivées pour leur fruits comestibles (courges, courgettes, concombres, cornichons, doubeurres, melons, pastèques, chayotes, etc.) et parfois pour leurs graines (courge à huile, pistache africaine). Leur domestication est très ancienne et remonte à plusieurs milliers d'années, tant dans le Nouveau Monde (Cucurbita, Sechium) que dans l'Ancien (Citrullus, Cucumis, Lagenaria, Luffa, Albanus Quénetus)."

liste2 = texte.split(". ")

liste2 = liste2[::-1]

print(("/").join(liste2))
