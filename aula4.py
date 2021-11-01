a = int(input('Primeiro bimestre: '))
while a > 10:
    a = int(input('Você dgitou errado. Primeiro bimestre: '))
b = int(input('Segundo bimestre: '))
while b > 10:
    b = int(input('Você dgitou errado. Segundo bimestre: '))
c = int(input('Terceiro bimestre: '))
while c > 10:
    c = int(input('Você dgitou errado. Terceiro bimestre: '))
d = int(input('Quarto bimestre: '))
while d > 10:
    d = int(input('Você dgitou errado. Quarto bimestre: '))
media = (a + b + c + d) / 4
print('Média: {}'.format(media))



# nota = int(input('Entre com a nota: '))
#
# while nota > 10:
#     nota = int(input('Nota inválida. Entre com a nota correta: '))


# a = int(input('Entre com um valor: '))
# for num in range(a+1):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#         if resto == 0:
#             div += 1
#     if div == 2:
#         print(num)

# a = int(input('Entre com o número: '))
#
# div = 0
# for x in range(1, a + 1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div += 1
#
# if div == 2:
#     print('O npumero {} é primo' .format(a))
# else:
#     print('O número {} não é primo' .format(a))
