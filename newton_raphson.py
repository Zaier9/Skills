#Implementando el método Newton en Python
#El método de Newton-Raphson (tambien conocido como metodo de Newton), es una forma de encontrar rápidamente una aproximación para la raíz de una funcion real

from __future__ import annotations

from decimal import Decimal
from math import *
from sympy import diff


def newton_raphson(
    func: str, a: float | Decimal, precision: float = 10 ** -10
) -> float:
    """Encuentra la raiz desde el punto 'a' en adelante mediante el método de Newton-Raphson
    >>> newton_raphson("sin(x)", 2)
    3.1415926536808043
    >>> newton_raphson("x**2 - 5*x +2", 0.4)
    0.4384471871911695
    >>> newton_raphson("x**2 - 5", 0.1)
    2.23606797749979
    >>> newton_raphson("log(x)- 1", 2)
    2.718281828458938
    """
    x = a
    while True:
        x = Decimal(x) - (Decimal(eval(func)) / Decimal(eval(str(diff(func)))))
        # Este numero dicta la precision de la respuesta
        if abs(eval(func)) < precision:
            return float(x)

#Vamos a ejecutar
if __name__ == '__main__':
    #Encuentra la raíz de la función trigonométrica
    #Encuentra el valor de pi
    print(f"La raíz de sin(x) = 0 es {newton_raphson('sin(x)', 2)}")
    #Encuentra la raiz del polinomio
    print(f"La raíz de x**2 - 5*x + 2 = 0 es {newton_raphson('x**2 - 5*x + 2', 0.4)}")
    #Encuentra la raiz cuadrada de 5
    print(f"La raíz de log(x) - 1 = 0 is {newton_raphson('log(x) - 1', 2)}")
    #Raices exponenciales
    print(f"La raiz de exp(x) - 1 = 0 es {newton_raphson('exp(x) - 1', 0)}")