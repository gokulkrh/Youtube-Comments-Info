import joblib
from Preprocessing import spamfilter_process


def spam_or_ham(comment):
    model = joblib.load('/home/gokul/Projects/Youtube-Comments-Info/Spam_Filter/spam_filter.pkl')
    comment = spamfilter_process.vectorized_comment(comment)
    return model.predict(comment)
