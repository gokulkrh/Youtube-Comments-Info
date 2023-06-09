import re
import joblib
import demoji
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
from textblob import Word
import nltk
nltk.download('stopwords')
stop = stopwords.words('english')

#remove hashtags, emojis, user mentions from comments.
def remove_tags_mentions(raw_comment):
    raw_comment = demoji.replace(raw_comment, '')
    raw_comment = re.sub("@[A-Za-z0-9_]+", "", raw_comment)
    raw_comment = re.sub("#[A-Za-z0-9_]+", "", raw_comment)
    return raw_comment


#removes unnecessary repeating characters from words, changes words like booook into book.
def remove_repeating_chars(raw_comment):
    pattern = re.compile(r"(.)\1{2,}")
    return pattern.sub(r"\1\1", raw_comment)


#removes numbers and punctuations.
def remove_nps(raw_comment):
    raw_comment = re.sub('[^\w\s]', ' ', raw_comment)
    raw_comment = re.sub('[0-9]', ' ', raw_comment)
    return raw_comment


#lemmatize words
def remove_stw_lemmatize(raw_comment):
    raw_comment = " ".join(x for x in raw_comment.split() if x not in stop)
    raw_comment = " ".join([Word(word).lemmatize() for word in raw_comment.split()])
    return raw_comment


def preprocessed_comment(raw_comment):
    raw_comment = remove_tags_mentions(raw_comment)
    raw_comment = remove_nps(raw_comment)
    raw_comment = remove_stw_lemmatize(raw_comment)
    raw_comment = remove_repeating_chars(raw_comment)
    raw_comment = raw_comment.lower()
    return raw_comment


def vectorized_comment(raw_comment):
    preprocessed_comment(raw_comment)
    vectorizer = joblib.load('/home/gokul/Projects/Youtube-Comments-Info/Preprocessing/count_vect.pkl')
    comment_vector = vectorizer.transform([raw_comment])
    return comment_vector
