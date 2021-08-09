from datetime import datetime, date
from collections import defaultdict, deque


def str_para_date(data: str) -> date:
    return datetime.strptime(data, '%d/%m/%Y')


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
