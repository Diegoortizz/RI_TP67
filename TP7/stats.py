from stop_words import get_stop_words
import itertools
import re

# files = ["test.txt"]

files = ["battery-life_netbook_1005ha.txt.data", "price_amazon_kindle.txt.data",
         "room_holiday_inn_london.txt.data", "sound_ipod_nano_8gb.txt.data", "speed_windows7.txt.data"]

# files = ["battery-life_netbook_1005ha.txt.data"]



Z = ["says", "wi", "I'd", "leftover", "receiving", "Another", "we", "hesitant", "Ultimately", "applies", "99", "search", "Check",
     "placed", "useful", "1030am", "I'd", "00am", "wanted", "gave", "They", "makes", "pushed", "We", "Finding", "snappier"]
Z = []

def parseW(s):
    return (" ".join(s.strip("\n").split()).replace(",", "").split())


print("-"*70)

for filename in files:
    with open("Critiques/projects/test-summarization/topics/" + filename, "r") as f:

        occ = {}

        lines = f.readlines()

        # on retire le dernier élement qui est une chaine vide
        nblines = len(lines)
        mots = list(map(lambda x: len(parseW(x)), lines))
        w = list(map(lambda x: parseW(x), lines))
        nbmots = sum(mots)

        # set de mot unique
        merged = (list(itertools.chain.from_iterable(w)))
        nbmots_unique = (len(set(merged)))
        lmots = list(merged)

        # on retire les stop words
        stop_words = set(get_stop_words('en'))
        stop_words.union(set(Z))
        stop_words = list(map(lambda x : x.lower(), stop_words))


        # construction de la map d'occurence
        for mots in lmots:
            if mots in occ and mots.lower() not in stop_words:
                occ[mots] += 1
            else:
                occ[mots] = 1

        sorted_x = sorted(occ.items(), key=lambda kv: kv[1], reverse=True)

        #### affichage ####
        print(f"nombre de ligne de {filename} : {nblines}")
        print(f"nombre de mots de {filename} : {nbmots}")
        print(f"nombre de mots UNIQUE de {filename} : {nbmots_unique}")
        print(
            f"nombre de mots moyen par ligne : {round(nbmots / nblines, 2) }")
        print(
            f"les 5 mots les PLUS utilisés sans les stop-words de {filename} sont :")
        # for w, c in sorted_x[:20]:
        #     print(f"{w} ({c})", end=", ")

        # print()
        # print(
            # f"les 5 mots les MOINS utilisés sans les stop-words de {filename} sont :")
        # for w, c in sorted_x[-20:]:
        #     print(f"{w} ({c})", end=", ")
        print()
        print("-"*70)
