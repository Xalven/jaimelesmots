#-*- encoding: utf-8 -*-
import codecs

def read_current_index():
    with open("current_index.txt", 'r') as current_index_file:
        current_index = current_index_file.readline()
        return current_index
class FileHandler(object):
    """
    Classe gérant la wordlist:
        - Elle est capable de localiser l'index où l'on est rendu (current_index)
        - Elle est capable de l'update
        - Elle est capable de retourner le mot correspondant au 'current_index'
        - Elle est capable de reset l'index en le remmettant à son 'initial_index'
    """

    def __init__(self):
        self.initial_index = '0'
        self._current_index = read_current_index()
        self._word_list = []

    def reset_index(self):
        with open("current_index.txt", "w") as current_index_file:
            current_index_file.write(self.initial_index)
    @property
    def get_current_index(self):
        return read_current_index()

    @property
    def _set_current_index(self, add = 1):
        self._current_index = int(self._current_index)
        self._current_index +=add
        self._current_index = str(self._current_index)
        with open("current_index.txt", "w") as current_index_file:
            current_index_file.write(self._current_index)

    def get_all_word(self):
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


if __name__ == '__main__':
    fileHandler = FileHandler

    print(read_current_index())
