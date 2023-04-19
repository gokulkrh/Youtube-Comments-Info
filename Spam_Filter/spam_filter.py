import joblib
from Preprocessing import spamfilter_process


def spam_or_ham(comment):
    model = joblib.load('Spam_Filter/spam_filter.pkl')
    comment = spamfilter_process.vectorized_comment(comment)
    return model.predict(comment)
