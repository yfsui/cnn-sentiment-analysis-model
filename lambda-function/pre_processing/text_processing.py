"""
Clean and tokenize text

Reference from Prof. Pierre-Hadrien Arnoux
"""

import re
from pre_processing.nltk_tokenize import TweetTokenizer
personal_pronouns = ['i','me','my','myself','we','our','ours','ourselves','you',"you're","you've","you'll",
 "you'd",'your','yours','yourself','yourselves','he','him','his','himself',
 'she',"she's",'her','hers','herself','it',"it's",'its','itself','they','them',
 'their','theirs','themselves']

class TextProcessor():
    """
    change a string of raw text into an array of int
    """

    def __init__(self):
        self.tknzr = TweetTokenizer()

    def clean_text(self,string):
        """
        remove urls and unnecessary tokens
        """
        # remove stopwords
        clean_tweet = [string for string in string .lower().split() if string not in personal_pronouns]
        clean_tweet = ' '.join(clean_tweet)
        
        # remove link
        pattern1 = re.compile(r'https?://[A-Za-z0-9.,\/\'-:_\"@!&#…\n]+')
        tweet_without_link = pattern1.sub('', clean_tweet)
        tweet_without_link = tweet_without_link.replace('\n', ' ')
        
        # remove retweet handlers "RT"
        pattern2 = re.compile(r'RT @[\w_]+: ')
        cleaned_text = pattern2.sub('', tweet_without_link)
        
        # remove @
        pattern3 = re.compile(r'\@[\w_]+ ')
        cleaned_text = pattern3.sub('', cleaned_text)

        return cleaned_text

    def tokenize_text(self,string):
        """
        change text into tokens
        """
        tokens = self.tknzr.tokenize(string)
        return tokens