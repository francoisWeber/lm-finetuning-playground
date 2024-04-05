from glob import glob
import nltk
from os import path as osp

_ = nltk.data.load("nltk:tokenizers/punkt/french.pickle")
DEFAULT_OBSIDIAN_DIR = "/Users/frweber/Documents/Obsidian"


def load_personal_sentences():
    texts = []
    for fpath in glob(osp.join(DEFAULT_OBSIDIAN_DIR, "**", "*.md"), recursive=True):
        with open(fpath) as f:
            for line in f.readlines():
                texts += nltk.sent_tokenize(line)
    return texts
