# Teste 1
print("=-=-=-=-=-=-=-=-= TESTE 1 =-=-=-=-=-=-=-=-=")
indice = 13
soma = 0
k = 0

while ( k < indice):
    k = k + 1
    soma = soma + k

print(f'O valor de soma é: {soma}') # 91

# 2
print("=-=-=-=-=-=-=-=-= TESTE 2 =-=-=-=-=-=-=-=-=")
# função fibonacci
def fibo(n):
    seq_fibo = [0, 1]
    for i in range(2, n):
        prox = seq_fibo[i-1] + seq_fibo[i-2]
        seq_fibo.append(prox)
    return seq_fibo

# função verificar num
def verifica_num(num, seq_fibo):
    if num in seq_fibo:
        print(f'O número {num} pertence a sequência!')
    else:
        print(f'O número {num} não pertence a sequência!')

num_termos = int(input("Informa quantidade desejada de números na sequência: "))
seq_fibo = fibo(num_termos)
print(seq_fibo)

num_informado = int(input("Informe o número para testar: "))
verifica_fibo = verifica_num(num_informado, seq_fibo)

# 3
print("=-=-=-=-=-=-=-=-= TESTE 3 =-=-=-=-=-=-=-=-=")
a = [1]
for i in range(10):
    prox = a[-1] + 2
    a.append(prox)
print("Lista A")
print(a)
print(f'onde o elemento desejado é: {a[4]}\n')

b = [2]
for i in range(10):
    prox = b[-1] * 2
    b.append(prox)
print("Lista B")
print(b)
print(f'onde o elemento desejado é: {b[6]}\n')

c = []
for i in range(10):
    prox = i ** 2
    c.append(prox)
print("Lista C")
print(c)
print(f'onde o elemento desejado é: {c[7]}\n')

d = []
for i in range(10):
    prox = (2 * i) ** 2
    d.append(prox)
print("Lista D")
print(d)
print(f'onde o elemento desejado é: {d[5]}\n')

e = [1, 1]
for i in range(10):
    prox = e[-1] + e[-2]
    e.append(prox)
print("Lista E")
print(e)
print(f'onde o elemento desejado é: {e[6]}\n')

print("Lista F")
print("Numeros que começam com a letra D")
print('onde o elemento desejado é: 200')

# 4
print("=-=-=-=-=-=-=-=-= TESTE 4 =-=-=-=-=-=-=-=-=")
# Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada.
# Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?
print("Posso ligar o primeiro interruptor e esperar alguns minutos para a lâmpada que estive acessa desse tempo de esquentar um pouco")
print("Depois, desligo esse primeiro interruptor, ligo o segundo e vou até a sala conferir")
print("Se a lâmpada estiver acessa, sei que o segundo é o certo, se não estiver e a lâmpada estiver quente, sei que o primeiro é o certo")
print("Se só estiver apagado, sei que o terceiro controla essa lâmpada")
print("Assim com mais um teste e uma visita conseguiria descobrir quais interruptores controlam cada lâmpada")

# 5
print("=-=-=-=-=-=-=-=-= TESTE 5 =-=-=-=-=-=-=-=-=")
palavra = str(input("Digite a palavra desejada: "))
invertida = palavra[::-1]
print(invertida)