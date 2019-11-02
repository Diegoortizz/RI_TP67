import csv

files = ["battery-life_netbook_1005ha.txt.data", "price_amazon_kindle.txt.data",
         "room_holiday_inn_london.txt.data", "sound_ipod_nano_8gb.txt.data", "speed_windows7.txt.data"]

# files = ["battery-life_netbook_1005ha.txt.data"]

data = []
cpt = 0

for filename in files:
    with open("Critiques/projects/test-summarization/topics/" + filename, "r") as f:
        temp = list(
            map(lambda x: [filename, x.strip().rstrip()], f.readlines()))
        data.append(temp)


for d in data:
    for i in range(len(d)):
        d[i] = [cpt] + d[i]
        cpt+=1


with open("datacsv.csv", "w", newline='') as f:
    writer = csv.writer(f)
    for e in data:
        writer.writerows(e)
