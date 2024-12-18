import csv
import matplotlib.pyplot as plt


with open("RTE_2022.csv", mode='r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    sources = {
        "Eolien": 0,
        "Solaire": 0,
        "Hydraulique": 0,
        "Fioul": 0,
        "Charbon": 0,
        "Gaz": 0,
        "Nucleaire": 0,
    }
    production_totale = 0

    header = next(reader)  
    for row in reader:
        try:
            prod_row = {
                "Eolien": int(row[11]) if row[11].strip() else 0,
                "Solaire": int(row[12]) if row[12].strip() else 0,
                "Hydraulique": int(row[13]) if row[13].strip() else 0,
                "Fioul": int(row[7]) if row[7].strip() else 0,
                "Charbon": int(row[8]) if row[8].strip() else 0,
                "Gaz": int(row[9]) if row[9].strip() else 0,
                "Nucleaire": int(row[10]) if row[10].strip() else 0,
            }
            for key in sources:
                sources[key] += max(prod_row[key], 0)  #on a juste rajouté max 0 pour dire que à chaque fois qu'on a une valeur négative, on l'ignore(remplacé par 0)(max(x,0) permet de prendre la plus grande valeur entre x et 0)

            production_totale += sum([max(x, 0) for x in prod_row.values()]) #et là on a rajouté max x 0 pour que chaque valeur x du dico qui soit négatives soit remplacé par 0 et ensuite ça calcule les valeurs filtrés
        except (IndexError, ValueError):
            continue



parts = {key: max((value / production_totale) * 100, 0) for key, value in sources.items()} #là on a encore rajouté max 0 pour filtrer les valeurs négatives


print("Production totale :", production_totale)
for source, pourcentage in parts.items():
    print("Part de ", source, ": ", pourcentage, "%")


labels = list(parts.keys())  
values = list(parts.values())  

plt.figure(figsize=(10, 7))
plt.pie(values, labels=labels, autopct='%1.1f%%', 
        colors=['green', 'yellow', 'cyan', 'red', 'blue', 'brown', 'pink','grey','black'])
plt.title("La comparaison avec les énergies non-renouvelables ")
plt.show()
