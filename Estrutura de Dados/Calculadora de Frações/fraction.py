def gcd(a, b):
    if(b == 0): return a;
    return gcd(b, a%b);
    
#Definição da Classe
class Fraction:
    def __init__(self, num, den):
        temp = gcd(num, den);
        self.num = int(num/temp);
        self.den = int(den/temp);
        if(self.den < 0):
            self.num *= -1;
            self.den *= -1;
    
#Método para exibir as frações
    def __str__(self):
        return f"{self.num}/{self.den}";
    
#Métodos Getters
    def getNum(self):
        return self.num;

    def getDen(self):
        return self.den;

#Métodos Setters 
    def setNum(self, x):
        self.num = x;

    def setDen(self, x):
        if(x == 0):
            print("Não é possível atribuir esse valor ao denominador!");
        else:
            self.den = x;

#Métodos de operações matemáticas
    def __add__(self, other):
        a = (self.num*other.den)+(other.num*self.den);
        b = self.den*other.den;
        return Fraction(a, b);

    def __sub__(self, other):
        a = (self.num*other.den)-(other.num*self.den);
        b = self.den*other.den;
        return Fraction(a, b);

    def __mul__(self, other):
        a = self.num*other.num;
        b = self.den*other.den;
        return Fraction(a, b);

    def __truediv__(self, other):
        a = self.num*other.den;
        b = self.den*other.num;
        return Fraction(a, b);

#Métodos de Operações Lógicas
    def __gt__(self, other):
        res = self - other;
        return ((res.num/res.den) > 0);

    def __ge__(self, other):
        res = self - other;
        return ((res.num/res.den) >= 0);

    def __lt__(self, other):
        res = self - other;
        return ((res.num/res.den) < 0);

    def __le__(self, other):
        res = self - other;
        return ((res.num/res.den) <= 0);

    def __eq__(self, other):
        res = self - other;
        return ((res.num/res.den) == 0);

    def __ne__(self, other):
        res = self - other;
        return ((res.num/res.den) != 0);