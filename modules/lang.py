class Lang:
    def __init__(self, language: str):
        self.__curlang: str = language

    def __eq__(self, other: str):
        return self.__curlang == other.language

    @property
    def language(self):
        return self.__curlang

    @language.setter
    def language(self, new_language: str):
        self.__curlang = new_language

    def load(self):
        '''
        Load programming language text
        :return: 
        '''
        #todo: choose url
        pass

