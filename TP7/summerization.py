from sklearn.feature_extraction.text import TfidfVectorizer
from copy import deepcopy

files = ["battery-life_netbook_1005ha.txt.data", "price_amazon_kindle.txt.data",
         "room_holiday_inn_london.txt.data", "sound_ipod_nano_8gb.txt.data", "speed_windows7.txt.data"]

# files = ["battery-life_netbook_1005ha.txt.data"]

# corpus = []
# for filename in files:
#     with open("Critiques/projects/test-summarization/topics/" + filename, "r") as f:
#         temp = list(
#             map(lambda x: x.strip().rstrip(), f.readlines()))
#         corpus = temp

# corpus = [
#     'This is the first document.',
#     'This document is the second document.',
#     'And this is the third one.',
#     'Is this the first document?',
# ]


def summarization_v1(corpus, longRes=10):
    corpussave = deepcopy(corpus)
    resume = []
    for i in range(longRes):
        vectorizer = TfidfVectorizer(stop_words="english")
        tfidf = vectorizer.fit_transform(corpus)
        fn = vectorizer.get_feature_names()
        best = max([(sum(list(tfidf.toarray()[i])), i)
                    for i in range(len(corpus))])
        resume.append(best[1])
        corpus[best[1]] = ""
    # print(resume)
    return list(map(lambda x: corpussave[x], resume))


def summarization_v2(corpus, longRes=5):
    tfidf = TfidfVectorizer(stop_words="english").fit_transform(corpus)
    best = [b for _, b in sorted([(sum(list(tfidf.toarray()[i])), i)
                                  for i in range(len(corpus))], reverse=True)[:longRes]]
    # print(best)
    return list(map(lambda x: corpus[x], best))

# print("\n".join(summarization_v2(corpus)))
# print("\n".join(summarization_v1(corpus)))


corpus = []
for filename in files:
    with open("Critiques/projects/test-summarization/topics/" + filename, "r") as f:
        print(filename)
        corpus = list(
            map(lambda x: x.strip().rstrip(), f.readlines()))
        resume = summarization_v1(corpus)
        filenamewrite = "".join(filename.split(".")[:-2]) + ".txt.sys.head5"
        print("".join(filename.split(".")[:-2]) + ".txt.sys.head5")
        with open("Critiques/projects/test-summarization/system/" + filenamewrite, 'w+') as f2:
            f2.write("\n".join(resume))
