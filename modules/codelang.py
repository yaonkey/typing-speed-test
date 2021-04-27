from github import Github
from parsing import Parsing


class CodeLang:
    urls: list[str] = ['https://raw.github.com/', '/master/']
    av_langs: list = [
        'php', 'c', 'cs', 'cpp', 'python', 'java',
        'rust', 'javascript', 'html', 'css']
    git = Github()

    def __init__(self, lang: str):
        if lang in self.av_lang:
            self.__load(lang)
        else:
            raise ValueError(f'Язык программирования {lang} недоступен!')

    def __load(self, lang: str):
        '''Метод, подгружающий ссылку на репозиторий по выбранному языку'''
        repo = self.git.search_repositories(query=f'language:{lang}')
        _url = self.urls[0] + repo.full_name + self.urls[1] + f'main.{lang}'
        print(_url)  # debug
        Parsing(_url)
