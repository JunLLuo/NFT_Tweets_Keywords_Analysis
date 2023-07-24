from transformers import pipeline
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def get_predicted_label(classifier, sequence_to_classify, candidate_labels=None):
    if not candidate_labels:
        candidate_labels = ['positive', 'negative', 'neutral']

    result_labels_scores = classifier(sequence_to_classify, candidate_labels)
    predicted_label = result_labels_scores['labels'][0]
    predicted_score = result_labels_scores['scores'][0]
    return result_labels_scores, predicted_label, predicted_score


def get_negative_positive_keywords(key, input_dict, top_n_split=50):
    positive_words = input_dict[key][:top_n_split]
    negative_words = input_dict[key][top_n_split:]
    return negative_words, positive_words


def sentiment_vader(sid_obj, sentence):
    sentiment_dict = sid_obj.polarity_scores(sentence)
    negative = sentiment_dict['neg']
    neutral = sentiment_dict['neu']
    positive = sentiment_dict['pos']
    compound = sentiment_dict['compound']

    if sentiment_dict['compound'] >= 0.05:
        overall_sentiment = "Positive"

    elif sentiment_dict['compound'] <= - 0.05:
        overall_sentiment = "Negative"

    else:
        overall_sentiment = "Neutral"

    return negative, neutral, positive, compound, overall_sentiment


if __name__ == "__main__":
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

    sid_obj = SentimentIntensityAnalyzer()

    sentences = [
        "We will announce a new NFT collection soon!",
        "Many people are skeptical about the long-term value of cryptocurrencies.",
        "Artificial intelligence is revolutionizing various industries.",
        "The sentiment analysis tool seems to be working well!"
    ]

    for sentence in sentences:
        # Zero-shot classification
        result_labels_scores, predicted_label, predicted_score = get_predicted_label(classifier, sentence, candidate_labels=['market', 'community', 'non-fungible tokens'])
        print(f"Sentence: {sentence}")
        print(f"Zero-shot Predicted Label: {predicted_label},  with confidence {predicted_score:.4f}")

        # Vader sentiment analysis
        negative, neutral, positive, compound, overall_sentiment = sentiment_vader(sid_obj, sentence)
        print(f"VADER Sentiment: {overall_sentiment} with compound score {compound:.4f}")
        print('-' * 50)
