import amrlib
import pandas as pd
import spacy

amrlib.setup_spacy_extension()

NER = spacy.load("en_core_web_lg")
stog = amrlib.load_stog_model()


def get_NER(dfs):
    all_verbs = []
    all_nouns = []
    all_prons = []
    all_vectors = []
    all_tweets = []
    all_usernames = []

    for i, (tweet, date, username) in enumerate(
        zip(dfs.tweet_text, dfs.date, dfs.username)
    ):
        print(date)
        raw_text = tweet
        text1 = NER(raw_text)

        verb_list = [token.lemma_ for token in text1 if token.pos_ == "VERB"]
        noun_list = [token.lemma_ for token in text1 if token.pos_ == "NOUN"]
        pron_list = [token.lemma_ for token in text1 if token.pos_ == "PRON"]

        all_verbs.append(verb_list)
        all_nouns.append(noun_list)
        all_prons.append(pron_list)
        all_vectors.append(text1.vector)
        all_tweets.append(tweet)

        all_usernames.append(username)

    return all_nouns, all_verbs, all_prons


if __name__ == "__main__":
    data = {
        "tweet_text": [
            "I am working on a solution",
            "She is reading a book",
            "He is playing outside",
        ],
        "date": ["2023-07-21", "2023-07-22", "2023-07-23"],
        "username": ["user1", "user2", "user3"],
    }

    dfs = pd.DataFrame(data)

    nouns, verbs, prons = get_NER(dfs)

    # Checking the results
    print("Nouns:", nouns)
    print("Verbs:", verbs)
    print("Pronouns:", prons)
