#-*- encoding: utf-8 -*-
import tweepy
import codecs

CODING = 'UTF-8'

consumer_key = 'r3njw0YBWHAi0MQ4QyIwnaBx8'
consumer_secret = '1xTAvXJulcoP8fAGHSC4nrrl8mxfvmaVs3u99nCSWxd7lrKFW8'
access_token = '1244591011407552512-4EBdK9Tpek2K6Ge8SpuohiVzTAdMGl'
access_token_secret = '6uWkwUx0FssImftCIf75Ym39hQLCCvQlbpZSRDViXHXir'


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
        liste_de_mot = []
        with open('wordlist.txt', 'r') as mot:
            for i in mot.readlines():
                liste_de_mot.append(i)
        nombre_de_mot = len(liste_de_mot)
        a = []
        final_list = []
        for i in range(0, nombre_de_mot):
            b = liste_de_mot[i].replace("\n", '')
            a.append(b)
        for i in range(0, nombre_de_mot):
            a[i] = bytes(a[i], 'cp1252')
            c = codecs.decode(a[i], 'utf-8')
            final_list.append(c)
        del a
        del liste_de_mot
        self._word_list+=final_list
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

