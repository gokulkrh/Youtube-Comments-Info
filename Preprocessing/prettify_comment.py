import html
import re
import string


def prettify_comment(raw_comment):
    raw_comment = html.unescape(raw_comment)
    raw_comment = "".join(x for x in raw_comment if x in string.printable)
    raw_comment = re.sub(r'<[^<]+?>', ' ', raw_comment)
    raw_comment = re.sub("^https?:\/\/.*[\r\n]*", "", raw_comment)
    return raw_comment
