from math import *
import sympy as sp


def derivate(expr, variables):
    for der_respect in variables:
        var = sp.Symbol(f'{der_respect}')
        funcion = sp.Derivative(expr, var, evaluate=True)
        print(f'Partial derivate df/d{der_respect} =  {funcion}')


if __name__ == '__main__':
    variables = ['x', 'y', 'z']
    expr = input("\nFunction to evaluate:    f(x,y,z)=")
    derivate(expr, variables)