from nltk import word_tokenize
from nltk.corpus import words
from nltk.stem.porter import PorterStemmer


class CaesarCipher(object):
    def __init__(self):
        self.__string: None
        self.__module: None
        self.__decoded_string = None
        self.__encoded_string = None
        self.__chiper_table = 'abcdefghijklmnopqrstuvwxyz'
        self.__dict_of_case = []
        self.__list_of_modules = ()
        self.__stemmer = PorterStemmer()

    def __string_set(self, string: str):
        if type(string) is str:
            self.__string = string.lower()
        else:
            raise Exception('Only string type')

    def __module_set(self, module: int):
        if type(module) is int:
            if module > 25:
                raise Exception("Module isn't more than 25")
            elif module <= 0:
                raise Exception("Module isn't less than 1")
            else:
                self.__module = module
        else:
            raise Exception("Module is only integer type")

    def __shifter(self, module: int) -> str:
        temp = ''
        for el in self.__string:
            if el in self.__chiper_table:
                index = self.__chiper_table.index(el) + module
                if index >= 25:
                    index = +(26 - index)
                temp += self.__chiper_table[index]
            else:
                temp += el
        return temp

    def encoded_string(self, string: str, module: int) -> str:
        self.__string_set(string)
        self.__module_set(module)
        return self.__shifter(self.__module)

    def decoded_string(self, string: str, module: int) -> str:
        self.__string_set(string)
        self.__module_set(module)
        return self.__shifter(-self.__module)

    def __counter_of_understanding_words(self, module: int, options: int) -> int:
        self.__module = module
        list_of_word = word_tokenize(self.decoded_string(self.__string, self.__module))
        list_of_word = list_of_word[:options]
        return len([word for word in list_of_word if self.__stemmer.stem(word) in words.words()])

    def __counter_of_understanding_words_for_all_modules(self, options: int):
        for i in range(1, 26):
            self.__dict_of_case.append((self.__counter_of_understanding_words(i, options), i))
        self.__dict_of_case.sort()

    def hack_of_caesar_chiper(self, text: str, options: int = 5) -> str:
        self.__string_set(text)
        self.__counter_of_understanding_words_for_all_modules(options)
        count = len(self.__dict_of_case)
        self.__module_set(self.__dict_of_case[count - 1][1])
        return self.decoded_string(self.__string, self.__module)
