import nltk

NLTK_DATA = [
    "punkt",
    "stopwords",
    "averaged_perceptron_tagger",
]


def download_nltk_resources():
    for resource in NLTK_DATA:
        try:
            nltk.download(resource)
            print(f"Successfully downloaded {resource}")
        except Exception as e:
            print(f"Failed to download {resource}: {str(e)}")


if __name__ == "__main__":
    download_nltk_resources()
