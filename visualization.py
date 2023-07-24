import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def MDA_positive_negative_words_count():
    # Synthetic data
    words = ["bulgogi", "sushi", "pizza", "cake", "pasta"]
    negative_word_label_dict = {word: np.random.choice(np.linspace(0.4, 0.8, 10)) for word in words}
    positive_word_label_dict = {word: np.random.choice(np.linspace(0.7, 1, 10)) for word in words}

    # Combine data for histogram plot
    list_ = [(value, "Negative") for key, value in negative_word_label_dict.items()]
    list_.extend([(value, "Positive") for key, value in positive_word_label_dict.items()])

    # Plotting
    plt.figure(figsize=(10, 5), dpi=180)
    sns.set_theme(style="white", font_scale=1)
    cmap = sns.color_palette("Blues", as_cmap=True)

    bins = np.linspace(0, 1, 7)
    sns.histplot(list(negative_word_label_dict.values()), label='MDA negative words', color=cmap(116), bins=bins)
    sns.histplot(list(positive_word_label_dict.values()), label='MDA positive words', color=cmap(200), bins=bins)

    plt.ylabel("Words count")
    plt.title(f'Project: CryptoPunks, label: "market"')
    plt.xlabel("One-shot learning scores")
    plt.legend()
    plt.show()


def subtraction_summary_cores():
    # Synthetic data
    project_names = ["bulgogi", "pizza", "sushi", "cake", "pasta"]
    project_scores_dict = {name + "_project": (np.random.uniform(0.2, 0.9),) for name in project_names}

    # Plotting
    plt.figure(figsize=(10, 6), dpi=180)
    sns.set_theme(style="white", font_scale=1.0)
    cmap = sns.color_palette("ch:s=.25,rot=-.25", as_cmap=True)
    ax = sns.barplot([l.split('_')[0] for l in list(project_scores_dict.keys())],
                     [x[0] for x in list(project_scores_dict.values())], color=cmap(116), ci=None)
    for item in ax.get_xticklabels():
        item.set_rotation(35)

    plt.ylabel("Subtraction of summation of scores")
    plt.title(f"label: 'community'")
    plt.show()


def project_sentiment_labels():
    # Synthetic data
    project_names = ["BulgogiTaste", "SushiMasters", "PizzaLovers", "CakeDelight", "PastaWorld"]
    project_sentiment_labels_dict = {name + "_project": (np.random.uniform(0.2, 0.9), np.random.uniform(0.1, 0.8)) for
                                     name in project_names}

    # Plotting
    plt.figure(figsize=(10, 6), dpi=180)
    sns.set_theme(style="white", font_scale=0.9)

    list_ = []
    for proj, v in project_sentiment_labels_dict.items():
        list_.append([proj.split('_')[0], v[0], 'MDA negative words'])
        list_.append([proj.split('_')[0], v[1], 'MDA positive words'])

    sentiment_df = pd.DataFrame(list_, columns=['project', 'sentiment_scores', 'word type'])

    cmap = sns.color_palette("Blues", as_cmap=True)
    ax = sns.barplot(data=sentiment_df, x='project', y='sentiment_scores', hue='word type', ci=None,
                     palette=[cmap(76), cmap(200)])
    for item in ax.get_xticklabels():
        item.set_rotation(35)

    plt.ylabel("Summation of sentiment scores")
    plt.title(f"Summation of sentiment scores between top 50 MDA positive and negative words")
    plt.xlabel('')
    plt.show()


if __name__ == "__main__":
    MDA_positive_negative_words_count()
    subtraction_summary_cores()
    project_sentiment_labels()