def dividir(dividendo, divisor):
    if not (isinstance(dividendo, int) and isinstance(divisor, int)):
        raise ValueError('O método dedve receber inteiros')
    try:
        aux = dividendo / divisor
    except Exception:
        print(f'Não foi possível dividir{dividendo} por {divisor}')
    return aux

def testa_divisao(divisor):

    resultado = dividir(10, divisor)
    print(f'Resultado de 10 por {divisor} é {resultado}')


if __name__ == '__main__':

    # try:
    #     testa_divisao(0)
    # except Exception as E:
    #     print(E)
    # except AttributeError as E:
    #     print(E)
    # except ZeroDivisionError as E:
    #     print(E)

    try:
        print('here')
        raise ValueError
    except ValueError:
        print('now here')
    print('continue')
