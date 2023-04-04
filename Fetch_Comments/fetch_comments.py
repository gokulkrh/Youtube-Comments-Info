from dotenv import load_dotenv
import os
import requests

from Preprocessing.prettify_comment import prettify_comment
from Spam_Filter.spam_filter import spam_or_ham


def get_comment_corpus(videoid, num_comments):
    text_data = []
    comment_corpus = ""
    load_dotenv()
    api_key = os.getenv("API_key")
    url = "https://youtube.googleapis.com/youtube/v3/commentThreads?videoId=" + videoid
    params = {'key': api_key, 'Accept': "application/json", 'order': 'relevance', 'part': "snippet"}

    while len(text_data) <= num_comments:
        r = requests.get(url=url, params=params)
        data = r.json()
        for i in data["items"]:
            comm = i["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            comment = prettify_comment(comm)
            if not spam_or_ham(comment):
                text_data.append(comment)
            else:
                print(comment)

        if data.get("nextPageToken"):
            params.update({"pageToken": data["nextPageToken"]})

    for i in text_data:
        comment_corpus += i
        comment_corpus += "\n"

    return comment_corpus

#for testing
if __name__ == "__main__":
    get_comment_corpus("5QiW4kOxXVg", 10)
