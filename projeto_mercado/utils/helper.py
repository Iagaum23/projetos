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


def verif_cpf(pass_cpf: str) -> bool:
    nums: defaultdict = defaultdict(lambda: 0)
    calculo_cpf: list = []
    calculo_cpf2: list = []
    digitos: list = []
    if len(pass_cpf) > 10:
        pass_cpf: list= pass_cpf.split(".")
        pass_cpf: str = "".join(pass_cpf)
        pass_cpf: list = pass_cpf.split("-")
        pass_cpf: str = "".join(pass_cpf)
    if pass_cpf == "111111111111" or pass_cpf == "22222222222" or pass_cpf == "33333333333" or pass_cpf ==\
            "44444444444" or pass_cpf == "55555555555" or pass_cpf == "66666666666"\
            or pass_cpf == "77777777777" or pass_cpf == "88888888888" or pass_cpf == "99999999999":
        return False
    if len(pass_cpf) < 10:
        return False
    cpfv: list = deque(pass_cpf)
    contador: int = 11
    if len(digitos) < 1:
        for x in range(9):
            contador -= 1
            nums[x] = int(cpfv[x])
            nums[x] = nums[x] * contador
            calculo_cpf.append(nums[x])
        calculo_cpf = 0 + sum(calculo_cpf)
        if calculo_cpf % 11 < 2:
            digitos.append(0)
        else:
            digitos.append(11 - (calculo_cpf % 11))
    contador: int = 12
    for x in range(10):
        contador -= 1
        if x < 9:
            nums[x] = int(cpfv[x])
            nums[x] = nums[x] * contador
            calculo_cpf2.append(nums[x])
        else:
            nums[x] = int(digitos[0])
            nums[x] = nums[x] * contador
            calculo_cpf2.append(nums[x])
    calculo_cpf2 = 0 + sum(calculo_cpf2)
    if calculo_cpf2 % 11 < 2:
        digitos.append(0)
    else:
        digitos.append(11 - (calculo_cpf2 % 11))
    if int(cpfv[9]) == digitos[0] and int(cpfv[10]) == digitos[1]:
        return True
    else:
        return False


def imprime_cpf(pass_cpf: str) -> str:
    if len(pass_cpf) > 10:
        pass_cpf: list = pass_cpf.split(".")
        pass_cpf: str = "".join(pass_cpf)
        pass_cpf: list = pass_cpf.split("-")
        pass_cpf: str = "".join(pass_cpf)
    cpf1: str = pass_cpf[0:3]
    cpf2: str = pass_cpf[3:6]
    cpf3: str = pass_cpf[6:9]
    cpf4: str = pass_cpf[9:11]
    return f"{cpf1}.{cpf2}.{cpf3}-{cpf4}"


def verif_cnpj(pass_cnpj) -> bool:
    nums: defaultdict = defaultdict(lambda: 0)
    calculo_cnpj: list = []
    calculo_cnpj2: list = []
    digitos: list = []
    if len(pass_cnpj) > 14:
        pass_cnpj: list = pass_cnpj.split(".")
        pass_cnpj: str = "".join(pass_cnpj)
        pass_cnpj: list = pass_cnpj.split("/")
        pass_cnpj: str = "".join(pass_cnpj)
        pass_cnpj: list = pass_cnpj.split("-")
        pass_cnpj: str = "".join(pass_cnpj)
    if len(pass_cnpj) < 14:
        return False
    cnpjv: deque = deque(pass_cnpj)
    y: int = 0
    if len(digitos) < 1:
        for x in range(5, 1, -1):
            nums[y] = int(cnpjv[y])
            nums[y] = nums[y] * x
            calculo_cnpj.append(nums[y])
            y += 1
        for x in range(9, 1, -1):
            nums[y] = int(cnpjv[y])
            nums[y] = nums[y] * x
            calculo_cnpj.append(nums[y])
            y += 1
    calculo_cnpj = 0 + sum(calculo_cnpj)
    if 11 - (calculo_cnpj % 11) < 2:
        digitos.append(0)
    else:
        digitos.append(11 - (calculo_cnpj % 11))
    y = 0
    for x in range(6, 1, -1):
        nums[y] = int(cnpjv[y])
        nums[y] = nums[y] * x
        calculo_cnpj2.append(nums[y])
        y += 1
    for x in range(9, 1, -1):
        nums[y] = int(cnpjv[y])
        nums[y] = nums[y] * x
        calculo_cnpj2.append(nums[y])
        if y == 12:
            break
        y += 1
    calculo_cnpj2 = 0 + sum(calculo_cnpj2)
    if 11 - round(calculo_cnpj2 % 11) < 2:
        digitos.append(0)
    else:
        digitos.append(11 - (calculo_cnpj2 % 11))
    if digitos[0] == int(cnpjv[12]) and digitos[1] == int(cnpjv[13]):
        return True
    else:
        return False


def imprime_cnpj(pass_cnpj) -> str:
    if len(pass_cnpj) > 12:
        pass_cnpj: list = pass_cnpj.split(".")
        pass_cnpj: str = "".join(pass_cnpj)
        pass_cnpj: list = pass_cnpj.split("/")
        pass_cnpj: str = "".join(pass_cnpj)
        pass_cnpj: list = pass_cnpj.split("-")
        pass_cnpj: str = "".join(pass_cnpj)
    cnpj1: str = pass_cnpj[0:2]
    cnpj2: str = pass_cnpj[2:5]
    cnpj3: str = pass_cnpj[5:8]
    cnpj4: str = pass_cnpj[8:12]
    cnpj5: str = pass_cnpj[12:15]
    return f"{cnpj1}.{cnpj2}.{cnpj3}/{cnpj4}-{cnpj5}"

