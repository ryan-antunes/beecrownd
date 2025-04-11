numero1,numero2,numero3= map(int,input().split())
tds_nums=numero1,numero2,numero3
nmaior=max(numero1,numero2,numero3)
nmenor=min(numero1,numero2,numero3)
soma=numero1+numero2+numero3
nmeio=soma-nmaior-nmenor
print(nmenor)
print(nmeio)
print(nmaior)
print()
for n in tds_nums:
    print(n)