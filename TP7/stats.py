import itertools
import re

# files = ["test.txt"]

files = ["battery-life_netbook_1005ha.txt.data", "price_amazon_kindle.txt.data",
         "room_holiday_inn_london.txt.data", "sound_ipod_nano_8gb.txt.data", "speed_windows7.txt.data"]


def parseW(s):
    return (" ".join(s.strip("\n").split()).replace(",", "").split())


print("-"*70)

for filename in files:
    with open("Critiques/projects/test-summarization/topics/" + filename, "r") as f:

        occ = {}

        data = " ".join(f.readlines())
        lines = re.split('[?.!]', data)

        # on retire le dernier élement qui est une chaine vide
        nblines = len(lines) - 1
        mots = list(map(lambda x: len(parseW(x)), lines))
        w = list(map(lambda x: parseW(x), lines))
        nbmots = sum(mots)

        # set de mot unique
        merged = (list(itertools.chain.from_iterable(w)))
        nbmots_unique = (len(set(merged)))
        lmots = list(merged)
        for mots in lmots:
            if mots in occ:
                occ[mots] += 1
            else:
                occ[mots] = 1
        
        sorted_x = sorted(occ.items(), key=lambda kv: kv[1], reverse=True)
        print(sorted_x[:15])
        print(f"nombre de ligne de {filename} : {nblines}")
        print(f"nombre de mots de {filename} : {nbmots}")
        print(f"nombre de mots UNIQUE de {filename} : {nbmots_unique}")
        print(
            f"nombre de mots moyen par ligne : {round(nbmots / nblines, 2) }")
        print("-"*70)

        # retirer les mots vides