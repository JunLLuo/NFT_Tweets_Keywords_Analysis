import re
import warnings
from collections import Counter

import amrlib
import numpy as np

warnings.filterwarnings("ignore")

amrlib.setup_spacy_extension()


def computeTF(wordDict):
    tfDict = {}
    bowCount = np.sum([w[1] for w in wordDict])
    for w in wordDict:
        tfDict[w[0]] = w[1] / float(bowCount)
    return tfDict


def computeIDF(docList, p):
    import math

    N = len(docList)

    idfDict = {}
    for doc in docList:
        for w in doc:
            if w[0] not in idfDict:
                idfDict[w[0]] = 0
            if w[1] > doc[int(len(doc) * p)][1]:
                idfDict[w[0]] += 1
    for word, val in idfDict.items():
        val_ = 1 if val == 0 else val
        idfDict[word] = math.log10(N / float(val_))
    return idfDict


def computeTFIDF(tfs, idfs, filterout_word_list=[]):
    tfidf = {}
    for word, val in tfs.items():
        if word in filterout_word_list:
            continue
        tfidf[word] = val * idfs[word]
    return tfidf


def Convert(tup, di):
    for a, b in tup:
        di[a] = b
    return di


def get_tfidf_from_cnts(cnts, i, p, size=15, filterout_word_list=[]):
    tfs = computeTF(cnts[i])
    idfs = computeIDF(cnts, p)
    tfidf = computeTFIDF(tfs, idfs, filterout_word_list)
    tfidf = sorted(tfidf.items(), key=lambda item: -item[1])

    return Convert(tfidf[:size], {}), tfs, idfs


def get_event_vector_from_tfidfs(tfidfs):
    vec_dict = {}
    for tfidf in tfidfs:
        for k, v in tfidf.items():
            if k not in vec_dict:
                vec_dict[k] = 0

    all_tfidf_vec_dict = []
    for tfidf in tfidfs:
        tfidf_vec_dict = {}
        for word in vec_dict.keys():
            if word not in tfidf:
                tfidf_vec_dict[word] = 0
            else:
                tfidf_vec_dict[word] = tfidf[word]
        all_tfidf_vec_dict.append(tfidf_vec_dict)

    return all_tfidf_vec_dict


if __name__ == "__main__":

    sentences = [
        "The NFT market is booming this year",
        "Artists are earning significantly from their NFT sales",
        "Blockchain technology underpins the authenticity of NFTs",
    ]

    cnts = [
        sorted(
            Counter(re.findall(r"\w+", sentence.lower())).items(),
            key=lambda x: x[1],
            reverse=True,
        )
        for sentence in sentences
    ]

    tup_list = [("a", 1), ("b", 2)]
    dictionary = {}
    print("Converted Tuple List to Dict:", Convert(tup_list, dictionary))

    i = 0
    p = 0.5
    tfidf, tfs, idfs = get_tfidf_from_cnts(cnts, i, p)
    print("\nTF-IDF for Document", i, ":", tfidf)
    print("Term Frequencies:", tfs)
    print("Inverse Document Frequencies:", idfs)

    tfidfs = [tfidf]
    event_vectors = get_event_vector_from_tfidfs(tfidfs)
    print("\nEvent Vector Representation:", event_vectors)
