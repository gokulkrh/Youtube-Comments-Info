from flask import Flask, jsonify
import mock_responses

app = Flask(__name__)


@app.route("/fyp/v1/emo_stats/<videoid>")
def return_emo_stats(videoid):
    return jsonify(mock_responses.mock_emotion)


@app.route("/fyp/v1/named_entities/<videoid>")
def return_named_keywords(videoid):
    return jsonify(mock_responses.mock_named_keywords)


@app.route("/fyp/v1/comments_summary/<videoid>")
def return_comments_summary(videoid):
    return jsonify(mock_responses.mock_summary)


@app.route("/fyp/v1/all/<videoid>")
def return_everything(videoid):
    return jsonify(mock_responses.mock_all)


if __name__=="__main__":
    app.run(debug=True)
