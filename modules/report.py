from pathlib import Path
## report system ##
def run(res):
    res_file = 'typing-speed-test.results.txt' 
    res_file_exists = Path(res_file)
    if res_file_exists.is_file():
        with open(res_file, 'r+') as rf:
            rf.write(res)
    else:
        with open(res_file, 'w') as rf:
            rf.write(res)
