from fetch_comments import get_comment_corpus

if __name__ == "__main__":
    comments_list, comments = get_comment_corpus("5QiW4kOxXVg", 100)
    print(len(comments_list))
    print(comments)
