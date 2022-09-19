#Crie um tipo abstrato de dado (TAD) para manipular números complexos na linguagem Python.
#O método deve:
#- calcular três números complexos;
#- realizar todas as operações básicas;
#- e imprimir as propriedades real e img do números.

class numcomplexo:
    def __init__(self,com1,com2,com3):
        self.n1=com1
        self.n2=com2
        self.n3=com3

    def somar(self):
        soma=self.n1+self.n2+self.n3
        print(soma)

    def subtrair(self):
        subtracao=self.n1-self.n2-self.n3
        print(subtracao)

    def multiplicar(self):
        multiplicacao=self.n1*self.n2*self.n3
        print(multiplicacao)
    
    def dividir(self):
        divisao=self.n1/self.n2/self.n3
        print(divisao)

a=float(input("Que número será a parte real do 1º número complexo? "))
b=float(input("Que número será a parte imaginária do 1º número complexo? "))
c=float(input("Que número será a parte real do 2º número complexo? "))
d=float(input("Que número será a parte imaginária do 2º número complexo? "))
e=float(input("Que número será a parte real do 3º número complexo? "))
f=float(input("Que número será a parte imaginária do 3º número complexo? "))


com1=complex(a,b)
com2=complex(c,d)
com3=complex(e,f)

resultado=numcomplexo(com1, com2, com3)
print("O resultado da soma é: ")
print(resultado.somar())
print("O resultado da subtração é: ")
print(resultado.subtrair())
print("O resultado da multiplicação é: ")
print(resultado.multiplicar())
print("O resultado da divisão é: ")
print(resultado.dividir())
