import csv
import matplotlib.pyplot as plt


with open("RTE_2022.csv", mode='r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    sources = {
        "Eolien": 0,
        "Solaire": 0,
        "Hydraulique": 0,
    }
    production_totale = 0

    header = next(reader)  #ça permet de skip l'en-tête
    for row in reader:
        try:
            prod_row = {
                "Eolien": int(row[11]) if row[11].strip() else 0,         #on prend la valeur de la collone mais si il y n'a pas de valeur valide(comme les espace), on met 0
                "Solaire": int(row[12]) if row[12].strip() else 0,
                "Hydraulique": int(row[13]) if row[13].strip() else 0,
            }
            for key in sources:                             #on met à jour pour chaque valeur qu'on enregistre dans le dico sources, on les additionne.
                sources[key] += prod_row[key]

            production_totale += sum(prod_row.values()) #le total global avec la somme des valeurs du précédent dictionnaire prod_row
        except (IndexError, ValueError):       #ca permet juste d'ignorer les valeurs invalides(comme les espaces) et continuer(Index c pour les colonnes et Value c pour les valeurs dans le fichier)
            continue


parts = {key: (value / production_totale) * 100 for key, value in sources.items()}    #c'est juste pour calculer la production en pourcentage par rapport à la production totale de chaque part donc l'éolien ,le solaire et l'hydraulique


print("Production totale :", production_totale)
for source, pct in parts.items():
    print("Part de " , source , ": " , (parts[source]) , "%") 


labels = list(parts.keys())           #les noms des sources 
values = list(parts.values())         #les valeurs en pourcentages calculés juste avant

plt.figure(figsize=(16, 9))
plt.pie(values, labels=labels, autopct='%1.1f%%', 
        colors=['green', 'yellow', 'cyan'])
plt.title("Production des énergies renouvelables : Solaire, Hydraulique, Éolien ")
plt.show()
