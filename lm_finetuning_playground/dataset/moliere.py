import nltk
import pandas as pd
from itertools import chain

_ = nltk.data.load("nltk:tokenizers/punkt/french.pickle")
DEFAULT_MOLIERE_DIALOGS_PATH = "/Users/frweber/tmp/dialogues_moliere.csv"


def get_moliere_sentences():
    df = pd.read_csv(DEFAULT_MOLIERE_DIALOGS_PATH)

    texts = list(
        chain(*[nltk.sent_tokenize(t.replace("\xa0", " ")) for t in df.text.to_list()])
    )
    return texts
