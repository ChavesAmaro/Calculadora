import os
import time
import math

def calculadora(num1: float, num2: float, operador: str) -> float:
    
    result = float("nan")
    if operador == '+':
        result = num1 + num2
    elif operador == '-':
        result = num1 - num2
    elif operador == '*':
        result = num1 * num2
    elif operador == '/':
        result = num1 / num2
    elif operador == '**':
        result = num1 ** num2
    return result



if __name__ == "__main__":
    continuar = True
    while continuar == True:
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            print('Calculadora')
            print('----------------------------------\n')
            num1 = float(input("Introduza o primeiro número.\n"))
            num2 = float(input("Introduza o segundo número.\n"))
            operador = input("Introduza a operação a realizar (+|-|*|/|**)").strip()
            
            resultado = calculadora(num1, num2, operador)
            if math.isnan(resultado):
                print("Erro! Escolha uma operação válida (+|-|*|/|**)")
            else:
                print(f"O resultado é {resultado}")
            
        except ValueError:
            print('Dados inválidos! -> Tente novamente!')
            time.sleep(2)
            continue
        except ZeroDivisionError:
            print('Impossível dividir por zero! -> Tente novamente!')
            time.sleep(2)
            continue
        repetirOK = False
        while repetirOK == False:
            repetir = input("Deseja fazer nova operação (s/n)").strip().lower()
            if repetir == 's':
                repetirOK = True
                continue
            elif repetir == 'n':
                repetirOK = True
                continuar = False
            else:
                print("Erro! Introduza uma opção válida (s/n)")
    print('\nVolte sempre!\n')
