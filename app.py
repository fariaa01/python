#9 ou menos  = mirim
#14 = infantil
#19 = junior
#25 = senior
# que todos =  master
from datetime import date
data = date.today().year
ano = int(input('Digite seu ano de nascimento: ' ))

idade = data - ano

if idade <=9:
    print('Voce participara do ramo mirim')
elif idade <=14:
    print('Voce vai participara do ramo infantil')
elif idade <=19:
    print('Voce vai participara do ramo junior')
elif idade <=25:
    print('Voce vai participara do ramo senior')
else:
    print('Voce vai participara do ramo master')