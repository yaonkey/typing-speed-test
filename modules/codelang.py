from github import Github
import requests
class CodeLang:
    url: str = 'https://raw.github.com/'
    av_langs: list = [
        'php', 'c', 'cs', 'cpp', 'python', 'ruby', 'rust', 'js', 'html', 'css'
    ]

    def __init__(self, lang: str):
        if lang in self.av_lang:
            pass
        else:
            raise ValueError(f'Язык программирования {lang} недоступен!')

    def load(self):
        _url = self.url + repo.full_name + '/master/'  # todo: поиск файла
