n1=int(input("Insira o primeiro número:"))
n2=int(input("Insira o segundo número:"))
n3=int(input("Insira o terceiro número:"))
menor=n1
if n2<n1 and n2<n3:
   menor=n2
if n3<n1 and n3<n2:
    menor=n3
print("O maior valor inserido é:",menor)
maior=n1
if n2>n1 and n2>n3:
   maior=n2
if n3>n1 and n3>n2:
   maior=n3
print("O menor valor inserido é:",maior)