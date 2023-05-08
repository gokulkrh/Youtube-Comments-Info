from Multilabel_Emotion_Recognition import emotion_recognition
from Fetch_Comments import fetch_comments
from Keyword_Extraction import tf_idf_scores, textrank_scores
from itertools import islice
from Summarization import extractive_summarization, abstractive_summarization


def emostats(commentlist):
    detectedEmotions = emotion_recognition.emotion_recognizer(commentlist)
    em = []
    for i in detectedEmotions['Emotions']:
        for j in i:
            em.append(j)
    stats = {}
    for i in set(em):
        t = em.count(i)
        per = t/len(em)
        stats[i] = per*100
    emo_stats = dict(sorted(stats.items(), key=lambda x: x[1], reverse=True))

    return emo_stats


def extractkeywords(comments):
    tf_idf = tf_idf_scores.calculate_tf_idf_scores(comments)
    textranker = textrank_scores.TextRank()
    textranker.analyze(comments, candidate_pos = ['PROPN', 'ADJECTIVE'], window_size=4, lower=False)
    textrank_score = textranker.get_keywords()
    for key, value in tf_idf.items():
        if key in textrank_score:
            textrank_score[key] += value
    sorted_dict = dict(sorted(textrank_score.items(), key=lambda item: item[1], reverse=True))
    return dict(islice(sorted_dict.items(), 15))


def summarizer(comments):
    ext_result = extractive_summarization.get_extractive_summ(comments)
    result = abstractive_summarization.abstractive_summary(ext_result)
    return result


def everything(videoId):
    comments, corpus = fetch_comments.get_comment_corpus(videoId)
    emos = emostats(comments)
    keywords = extractkeywords(corpus)
    summary = summarizer(comments)

    resp = {
        "Emostats": emos,
        "Keywords": keywords,
        "Summary": summary
    }
    return resp


