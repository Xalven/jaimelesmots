#-*- encoding: utf-8 -*-
import time
from file import *
from WordBot import *

def main():
    wordBot = WordBot(consumer_key, consumer_secret, access_token, access_token_secret)
    fileHandler = FileHandler()
    current_index = fileHandler.get_current_index
    current_index = int(current_index)
    wordlist = fileHandler.get_all_word()
    wordBot.tweet(wordlist[current_index])
    fileHandler._set_current_index

if __name__ == '__main__':
    main()

