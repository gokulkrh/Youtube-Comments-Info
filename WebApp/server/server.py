from flask import Flask, jsonify
from flask_caching import Cache
from Fetch_Comments import fetch_comments
import mock_responses
import os
from flask_cors import CORS
import emotion_stats

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
CORS(app)


@app.route("/fyp/v1/fetch-comments/<videoid>")
@cache.cached(timeout=3600)
def cache_comments(videoid):
    comments = cache.get(videoid)
    if comments is None:
        comments, _ =  fetch_comments.get_comment_corpus(videoid, 300)
        cache.set(videoid, comments)
        print("fetched comments")
        return "Success"
    return "Success"


@app.route("/fyp/v1/emo-stats/<videoid>")
def return_emo_stats(videoid):
    comments = cache.get(videoid)
    if comments is None:
        comments, _ =  fetch_comments.get_comment_corpus(videoid, 300)
        cache.set(videoid, comments)
        print("fetched comments")
    x = emotion_stats.emostats(comments)
    print("got emotions")
    return x
    


@app.route("/fyp/v1/keywords/<videoid>")
def return_named_keywords(videoid):
    comments = cache.get(videoid)
    if comments is None:
        comments, _ =  fetch_comments.get_comment_corpus(videoid, 300)
        cache.set(videoid, comments)
        print("fetched comments")
    corpus = ""
    for i in comments:
        corpus += i
        corpus += " "
    x = emotion_stats.extractkeywords(corpus)
    print("found keywords")
    return x



@app.route("/fyp/v1/summary/<videoid>")
def return_comments_summary(videoid):
    comments = cache.get(videoid)
    if comments is None:
        comments, _ =  fetch_comments.get_comment_corpus(videoid, 300)
        cache.set(videoid, comments)
        print("fetched comments")
    x = [comments[i:i+100] for i in range(0, len(comments), 100)]
    extra = x[len(x)-1]
    x[0] += extra
    summ_list = ""
    for i in range(len(x)):
        cent_summ = emotion_stats.summarizer(x[i])
        summ_list += cent_summ
        summ_list += " "
        print(i)
    return summ_list


@app.route("/fyp/v1/all/<videoid>")
def return_everything(videoid):
    return jsonify(emotion_stats.everything(videoid))


@app.route("/fyp/v1/all/mock/<videoid>")
def return_mock_everything(videoid):
    return jsonify(mock_responses.new_mock)


if __name__=="__main__":
    app.run(debug=False, threaded=False)
