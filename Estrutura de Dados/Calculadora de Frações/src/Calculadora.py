from fraction import Fraction
import os;

def divZero():
    print("Operação inválida! Não é possível dividir por zero!")

def limpa():
    if(os.name == 'nt'): 
        os.system('cls');
    else:
        os.system('clear');

def compara(flag):
    if(flag == True):
        return " é ";
    return " não é ";

def main():

    print("Insira o numerador da primeira Fração:");
    while True:
        try:
            n1 = int(input());
            break;
        except ValueError:
            print("Operação inválida. Insira um número inteiro!");

    print("Insira o denominador da primeira Fração:");
    while True:
        try:
            n2 = int(input());
            if(n2 == 0):
                divZero();
            else:
                break;
        except ValueError:
            print("Operação inválida. Insira um número inteiro!");

    f1 = Fraction(n1, n2);

    print("Insira o numerador da segunda Fração:");
    while True:
        try:
            n1 = int(input());
            break;
        except ValueError:
            print("Operação inválida. Insira um número inteiro!");

    print("Insira o denominador da segunda Fração:");
    while True:
        try:
            n2 = int(input());
            if(n2 == 0):
                divZero();
            else:
                break;
        except ValueError:
            print("Operação inválida. Insira um número inteiro!");

    f2 = Fraction(n1, n2);

    print("Digite 1 para uma operação matemática e 2 para uma operação comparativa:")
    while True:
        while True:
            try:
                t = int(input());
                break;
            except ValueError:
                print("Digite um inteiro.")

        if(t != 2 and t != 1):
            print("Digite uma entrada válida.");
        else:
            break;

    limpa();
    if(t == 1):
        print("- Selecione a opção que deseja. - \n 1 -> Soma \n 2 -> Subtração \n 3 -> Multiplicação \n 4 -> Divisão");
        while True:
            while True:
                while True:
                    try:
                        t = int(input());
                        break;
                    except ValueError:
                        print("Digite um inteiro.")

                if(t < 1 or  t > 4):
                    print("Digite uma entrada válida.");
                else:
                    break;
            
            if(t == 4 and (f1.getNum() == 0 or f2.getNum() == 0)):
                divZero();
            else:
                break;

        match t:
            case 1:
                print(f1, " + ", f2, " = ", f1+f2, sep = "");
            case 2:
                print(f1, " - ", f2, " = ", f1-f2, sep = "");
            case 3:
                print(f1, " * ", f2, " = ", f1*f2, sep = "");
            case 4:
                print(f1, " / ", f2, " = ", f1/f2, sep = "");
    else:
        print("- Selecione a opção que deseja. - \n 1 -> Maior que \n 2 -> Maior ou igual que \n 3 -> Menor que \n 4 -> Menor ou igual que \n 5 -> Igual a \n 6 -> Diferente de" );
        while True:
            while True:
                try:
                    t = int(input());
                    break;
                except ValueError:
                    print("Digite um inteiro.")

            if(t < 1 or  t > 6):
                print("Digite uma entrada válida.");
            else:
                break;
        
        match t:
            case 1:
                print(f1, compara(f1>f2), "maior que ", f2, sep = "");
            case 2:
                print(f1, compara(f1>=f2), "maior ou igual que ", f2, sep = "");
            case 3:
                print(f1, compara(f1<f2), "menor que ", f2, sep = "");
            case 4:
                print(f1, compara(f1<=f2), "menor ou igual que  ", f2, sep = "");
            case 5:
                print(f1, compara(f1==f2), "igual à", f2, sep = "");
            case 6:
                print(f1, compara(f1>f2), "diferente de ", f2, sep = "");


r = 1;
while(r == 1):
    limpa();
    print("Bem vindo a calculadora de Frações!");
    main();
    print("Deseja fazer mais uma operação? Digite 1 para sim e 0 para não.")
    while True:
        while True:
            try:
                r = int(input());
                break;
            except ValueError:
                print("Digite um inteiro.")

        if(r != 0 and r != 1):
            print("Digite uma entrada válida.");
        else:
            break;

print("Encerramento do Programa");
