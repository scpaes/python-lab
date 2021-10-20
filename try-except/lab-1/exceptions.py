class SaldoInsuficienteError(Exception):
    def __init__(self, message='', saldo=None, valor=None):
        self.saldo