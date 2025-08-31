print("Calculadora Simples")
print("escolha a operacao")
print("1 - Adicao")
print("2 - Subtracao")
print("3 - Multiplicacao")
print("4 - Divisao")

def adicao (x, y):
    return x + y

def subtracao (x, y):
    return x - y

def multiplicacao (x, y):
    return x * y

def divisao (x, y):
    return x / y

escolha = input("Digite a operacao (1/2/3/4): ")

num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))

if escolha == '1':
    print(num1, "+", num2, "=", adicao(num1, num2))
    
elif escolha == '2':
    print(num1, "-", num2, "=", subtracao(num1, num2))

elif escolha == '3':
    print(num1, "*", num2, "=", multiplicacao(num1, num2))
    
elif escolha == '4':
    print(num1, "/", num2, "=", divisao(num1, num2))
    

