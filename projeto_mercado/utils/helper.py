from datetime import datetime, date
from collections import defaultdict, deque
from typing import Union


def str_para_date(data: str) -> Union[date, bool]:
    try:
        return datetime.strptime(data, '%d/%m/%Y')
    except ValueError:
        return False

def date_para_str(data: date) -> str:
    return data.strftime('%d/%m/%Y')


def float_para_moeda(moeda: float) -> str:
    return f'R${moeda}'
    