# leia o ano e diga se é bisexto ou não

import datetime
import time

ano = int(input('Qual ano deseja analisar? \n(se deseja o ano atual, digite 0): '))
if ano == 0:
    ano = datetime.date.today().year

print('Analisando...')
time.sleep(2)

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('*'*50)
    print('O ano {} é bissexto!'.format(ano))
    print('*' * 50)
else:
    print('*' * 50)
    print('O ano {} NÃO É bissexto!'.format(ano))
    print('*' * 50)
