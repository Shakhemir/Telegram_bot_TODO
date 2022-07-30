from config import log_file
from datetime import datetime


def add_log(text):
    log_txt = f'{datetime.now().strftime("%Y.%m.%d %H:%M:%S")} {text}'
    with open(log_file, 'a', encoding='utf-8') as file:
        print(log_txt, file=file)
    print(log_txt)