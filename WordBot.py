#-*- encoding: utf-8 -*-
import tweepy
import codecs

CODING = 'UTF-8'

consumer_key = '...'        #I'm not stupid haha
consumer_secret = '...'
access_token = '...'
access_token_secret = '...'


class WordBot(object):
    """
    Bot tweetant tout les mots du dictionnaire
    """
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self._consumer_key = consumer_key
        self._consumer_secret = consumer_secret
        self._access_token = access_token
        self._access_token_secret = access_token_secret
        self._auth = tweepy.OAuthHandler(self._consumer_key, self._consumer_secret)
        self._auth.set_access_token(self._access_token, self._access_token_secret)
        self.api = tweepy.API(self._auth)
        self.initial_index = '0'
        self._word_list = []
        self._current_index = ''

    @property
    def _get_current_index(self):
        with open("current_index.txt", 'r') as current_index_file:
            self._current_index = current_index_file.readline()
        return int(self._current_index)

    @property
    def _increment_index(self, add=1):
        self._current_index = self._get_current_index
        self._current_index +=add
        self._current_index = str(self._current_index)
        with open("current_index.txt", "w") as current_index_file:
            current_index_file.write(self._current_index)

    def _tweet(self, mot):
        try:
            self.api.update_status(f"Moi aimer \"{mot}\"♥")
        except Exception as e:
            raise e

    @property
    def _get_word_list(self):
        self._word_list = []
        with open('wordlist.txt', 'r') as mot:
            for i in mot.readlines():
                word = i.replace("\n", '')
                word = bytes(word, 'cp1252')
                word = codecs.decode(word, 'utf-8')
                self._word_list.append(word)
            mot.close()
        return self._word_list
    def reset_index(self):
        with open("current_index.txt", "w") as current_index_file:
            current_index_file.write(self.initial_index)
    def post_tweet(self):
       index = self._get_current_index
       wordlist = self._get_word_list
       word = wordlist[index]
       self._tweet(word)

if __name__ == '__main__':
    wordBot = WordBot(consumer_key, consumer_secret, access_token, access_token_secret)
    wordBot.post_tweet()

