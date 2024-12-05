from math import gcd

class Fraction:
    def __init__(self, nomirateur=0, dinomirateur=1):
        if dinomirateur == 0:
            raise ValueError("Le dénominateur ne peut pas être zéro.")
        self.__nomirateur = nomirateur
        self.__dinomirateur = dinomirateur
        self.reduire()  # Simplifie la fraction dès la création

    @property
    def nomirateur(self):
        return self.__nomirateur

    @nomirateur.setter
    def nomirateur(self, value):
        self.__nomirateur = value

    @property
    def dinomirateur(self):
        return self.__dinomirateur

    @dinomirateur.setter
    def dinomirateur(self, value):
        if value != 0:
            self.__dinomirateur = value
        else:
            raise ValueError("le dinomirateur doit etre different a 0")

    @property
    def valeur(self):
        return self.__nomirateur / self.__dinomirateur  # Calcul de la valeur de la fraction

    def __str__(self):
        self.reduire()
        return f"{self.__nomirateur} / {self.__dinomirateur}"

    def reduire(self):
        div = gcd(self.__nomirateur, self.__dinomirateur)
        self.__nomirateur //= div
        self.__dinomirateur //= div

    def __add__(self, other):
        n = self.__nomirateur * other.__dinomirateur + self.__dinomirateur * other.__nomirateur
        d = self.__dinomirateur * other.__dinomirateur
        return Fraction(n, d)

    def __sub__(self, other):
        n = self.__nomirateur * other.__dinomirateur - self.__dinomirateur * other.__nomirateur
        d = self.__dinomirateur * other.__dinomirateur
        return Fraction(n, d)

    def __mul__(self, other):
        n = self.nomirateur * other.__nomirateur
        d = self.dinomirateur * other.__dinomirateur
        return Fraction(n, d)

    def __truediv__(self, other):
        n = self.__nomirateur * other.__dinomirateur
        d = self.__dinomirateur * other.__nomirateur
        return Fraction(n, d)

    def __floordiv__(self, other):
        n = self.__nomirateur * other.__dinomirateur
        d = self.__dinomirateur * other.__nomirateur
        return Fraction(n, d)

    def __gt__(self, other):
        return self.valeur > other.valeur  # Utilise la propriété 'valeur' pour comparer

    def __ge__(self, other):
        return self.valeur >= other.valeur

    def __lt__(self, other):
        return self.valeur < other.valeur

    def __le__(self, other):
        return self.valeur <= other.valeur

    def __ne__(self, other):
        return self.valeur != other.valeur

    def __eq__(self, other):
        return self.valeur == other.valeur

    def to_dict(self):
        return {"nomirateur": self.__nomirateur, "dinomirateur": self.__dinomirateur}


#*******************************************************************************************
try :
    f1 = Fraction(3, 0)
except ValueError as erreur :
    print(f"Erreur !!! { erreur}")
    f1 = Fraction(1, 1)


f2 = Fraction( 1, 4 )
print(f"Fraction 1 : {f1}")
print(f"Fraction 2 : {f2}")
print("______________arithmiatique : ___________________")

print(f"addition       ----->  {f1 + f2}")
print(f"sustraction    ----->  {f1 - f2}")
print(f"multiplication ----->  {f1 * f2}")
print(f"division       ----->  {f1 / f2}")

print("______________Comparaison : _____________________")

print(f"{f1} == {f2}   ----->  {f1 == f2}")
print(f"{f1} != {f2}   ----->  {f1 != f2}")
print(f"{f1} > {f2}    ----->  {f1 > f2}")
print(f"{f1} >= {f2}   ----->  {f1 >= f2}")
print(f"{f1} < {f2}    ----->  {f1 < f2}")
print(f"{f1} <= {f2}   ----->  {f1 <= f2}")
f1 += f2
print(f1)
print(f1.to_dict())