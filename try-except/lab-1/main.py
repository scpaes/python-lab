from exceptions import SaldoInsuficienteError
class Client:
    def __init__(self, name, doc_number, job):
        self.name = name
        self.doc_number = doc_number
        self.job = job


class ContaCorrente:
    total_contas_criadas = 0
    taxa_operacao = None

    def __init__(self, cliente, agencia, numero, saldo):
        '''
            Para evitar a criação de atributos fora do método de inicialização da classe,
            definimos valores padrões zerados, para que estes atributos sejam alterados
            nos setters.
        '''
        self.__saldo = 0
        self.__agencia = 0
        self.__numero = 0

        self.cliente = cliente
        self.__set_agencia(agencia)
        self.__set_numero(numero)
        self.__set_saldo(saldo)

        ContaCorrente.total_contas_criadas += 1
        ContaCorrente.taxa_operacao = 30 / ContaCorrente.total_contas_criadas

    @property
    def agencia(self):
        return self.__agencia

    @property
    def saldo(self):
        return self.__saldo

    @property
    def numero(self):
        return self.__numero

    def __set_agencia(self, agencia):
        if not isinstance(agencia, int) or agencia <= 0:
            raise ValueError('Error. Agência deve ser do tipo inteiro e maior que zero.', agencia)
        self.__agencia = agencia

    def __set_numero(self, numero):
        if not isinstance(numero, int) or numero <= 0:
            raise ValueError('Erro. Número deve ser do tipo inteiro e maior que zero.', numero)
        self.__numero = numero

    def __set_saldo(self, saldo):
        breakpoint()
        if not isinstance(saldo, int) or saldo <= 0:
            raise ValueError('Error. O saldo deve ser do tipo inteiro e maior que zero.')
        self.__saldo = saldo

    def transferir(self, valor, favorecido):
        favorecido.depositar(valor)

    def sacar(self, valor):
        self.__set_saldo(self.saldo - valor)

    def depositar(self, valor):
        self.saldo += valor


def main():
    import sys

    contas = []
    while (True):
        try:
            nome = input('Nome do cliente: \n')
            agencia = int(input('Agência: \n'))
            numero = int(input('Número: \n'))
            saldo = int(input('Saldo: \n'))
            client = Client(nome, None, None)
            conta_conrrente = ContaCorrente(client, agencia, numero, saldo)
            contas.append(conta_conrrente)
        except ValueError as E:
            print(E.args)
        except KeyboardInterrupt:
            print(f'\n\n{len(contas)}, conta(s) criadas.')


# if __name__ == '__main__':
#     main()

client = Client('Test', None, None)
conta_corrent = ContaCorrente(client, 123, 123, 100)
conta_corrent.sacar(150)
print(conta_corrent.saldo)