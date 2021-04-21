# report system
from datetime import datetime


def run(res):
    # TODO: change report file type to markdown
    res_file = 'typing-speed-test.results.txt'
    with open(res_file, 'a+') as rf:
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        rf.write(str(date) + ' ' + res + '\n')
