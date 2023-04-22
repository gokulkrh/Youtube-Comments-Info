import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
stop = stopwords.words('english')
from sklearn.feature_extraction.text import TfidfVectorizer


def sort_coo(coo_matrix):
    tuples = zip(coo_matrix.col, coo_matrix.data)
    return sorted(tuples, key=lambda x: (x[1], x[0]), reverse=True)


def extract_feature_scores(feature_names, sorted_items):
    score_vals = []
    feature_vals = []
    
    for idx, score in sorted_items:
        score_vals.append(round(score, 3))
        feature_vals.append(feature_names[idx])

    results= {}
    for idx in range(len(feature_vals)):
        results[feature_vals[idx]]=score_vals[idx]
    
    return results


def calculate_tf_idf_scores(text):
    vectorizer = TfidfVectorizer(stop_words=stop, smooth_idf=True, use_idf=True)
    vectorizer.fit_transform([text])

    feature_names = vectorizer.get_feature_names_out()
    tf_idf_vector = vectorizer.transform([text])
    sorted_items=sort_coo(tf_idf_vector.tocoo())
    tf_idf_scores = extract_feature_scores(feature_names, sorted_items)

    return tf_idf_scores
