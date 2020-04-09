#-*- encoding: utf-8 -*-
import tweepy


CODING = 'UTF-8'

consumer_key = '...'
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

    @property
    def get_auth(self):
        return self._auth

    @property
    def get_consumer_key(self):
        return self._consumer_key

    @property
    def get_consumer_secret(self):
        return self._consumer_secret

    @property
    def get_access_token(self):
        return self._access_token

    @property
    def get_access_token_secret(self):
        return self._access_token_secret

    def tweet(self, mot):
        try:
            self.api.update_status(f"J'aime le mot \"{mot}\"♥")
        except Exception as e:
            raise e
