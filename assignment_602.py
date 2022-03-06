"""Assignment602_WebCrawler - Python3 program
Author: Robert Mwaniki
Date: 2/14/2022
Youtube: https://youtu.be/j06QgdndACE

I have not given or received any unauthorized assistance on this assignment.
"""
from urllib.request import urlopen
import urllib
import re

my_stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're",
                "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he',
                'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's",
                'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which',
                'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are',
                'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do',
                'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because',
                'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against',
                'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to',
                'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further',
                'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any',
                'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only',
                'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don',
                "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain',
                'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't",
                'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma',
                'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't",
                'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't",
                'wouldn', "wouldn't", 'both']

def remove_mystopwords(sentence):
    """Remove stop words from html text.

    :param string sentence: raw html
    :return string tokens_filtered: clean text
    """
    text_tokens = sentence.split(" ")
    tokens_filtered= [word for word in text_tokens if not word in my_stopwords]
    return (" ").join(tokens_filtered)

def count_words(tag, word_count):
    """Count words.

    :param string tag: text from html tag
    :param dictionary word_count: store count of words
    """

    for words in tag:
        words_split = words.split(' ')
        for word in words_split:
            formated_word = remove_mystopwords(word)
            l_word = len((formated_word).strip())
            if "<" not in formated_word and ">" not in formated_word and l_word > 0:
                if word not in word_count:
                    word_count[word] = 1
                else:
                    word_count[word] += 1
    return word_count

def get_html(url):
    """Get HTML.

    :param string url: html string

    Returns:
    return list links: links found on page
    return list p: text found in <p> tag
    return list h2: text found in <h2> tag
    return list h1: text found in <h1> tag
    """
    # Request header
    header={
        'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7)" \
                    "AppleWebKit/5362 (KHTML, like Gecko)" \
                    "Chrome/36.0.879.0 Mobile Safari/5362',
        'Referer':'https://www.cdm.depaul.edu/Pages/default.aspx',
        'Connection':'keep-alive'}
    req=urllib.request.Request(url,headers=header)
    response=urllib.request.urlopen(req)
    html=response.read().decode('utf8')

    # pylint: disable=anomalous-backslash-in-string
    links = re.findall('"((http|ftp)s?://.*?)"', html)
    p = re.findall("<\s*p[^>]*>(.*?)<\s*\/\s*p\s*>", html)
    h2 = re.findall("<\s*h2[^>]*>(.*?)<\s*\/\s*h2\s*>", html)
    h1 = re.findall("<\s*h1[^>]*>(.*?)<\s*\/\s*h1\s*>", html)
    # pylint: enable=anomalous-backslash-in-string
    return links, p, h1, h2

def print_top_25(sorted_words):
    """Print top 25."""
    print("\n**********")
    print("Top 25")
    print("**********")

    for key, value in sorted_words[0:25]:
        print("Key : {} | Value : {}".format(key,value))

def loop(links,word_count, seen):
    """Iterate through html requests in loop."""
    if not links:
        return word_count
    try:
        url = links.pop(0)[0]
        if not url in seen and 'edu' in url:
            seen.append(url)
            print(url)
            new_links, p, h1, h2 = get_html(url)
            links.append(new_links)

            count_words(p, word_count)
            count_words(h1, word_count)
            count_words(h2, word_count)

            # OPTION TO PRINT TOP 25 on each website
            # sorted_words = sorted(word_count.items(), key=lambda x:x[1], reverse=True)
            # print_top_25(sorted_words)
        return loop(links, word_count, seen)
    except:
        return loop(links, word_count, seen)


def main():
    """Main function."""
    word_count = {}
    seen = []
    starting_url = "https://www.cdm.depaul.edu/Pages/default.aspx"
    links, p, h1, h2 = get_html(starting_url)

    count_words(p, word_count)
    count_words(h1, word_count)
    count_words(h2, word_count)

    seen.append(starting_url)
    # recursively loop through sites
    loop(links, word_count, seen)
    # Total word count
    sorted_words = sorted(word_count.items(), key=lambda x:x[1], reverse=True)
    print_top_25(sorted_words)


if __name__ == "__main__":
    main()
