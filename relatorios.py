import datetime

# =-=-=-=-=-=- Parte 1 do desafio (Trabalhando com Decoradores) =-=-=-=-=-=-
def transacao_info(funcao):
    def wrapper(*args):
        print('Impressão do decorador!')
        data_atual = datetime.datetime.now().strftime("DATA: %d/%m/%Y / HORA: %H:%M")
        transacao = funcao(*args)
        if type(transacao) != tuple:
            print(f'Data e Hora da transação: {data_atual} / Tipo de transação: {transacao}')
            return transacao
        else:
            transacao_realizada = transacao[1]
            print(f'Data e Hora da transação: {data_atual} / Tipo de transação: {transacao_realizada}')
            return transacao

    return wrapper

# =-=-=-=-=-=- Parte 2 do desafio (Trabalhando com Geradores) =-=-=-=-=-=-
def registros_transacoes(conta, transacao=None):
    print('Impressão do gerador!')
    registros = conta.historico.registros
    match transacao:
        case None:
            for registro in registros:
                yield registro.transacao_realizada
        case _:
            for registro in registros:
                if registro.transacao_realizada['Tipo de Transação'] == transacao:
                    yield registro.transacao_realizada


# =-=-=-=-=-=- Parte 3 do desafio (Trabalhando com Iteradores) =-=-=-=-=-=-
class ContasRegistradas:
    def __init__(self, contas):
        self.contas = contas
        self.contador = 0

    
    def __iter__(self):
        return self
    

    def __next__(self):
        try:
            conta = self.contas[self.contador]
            self.contador+=1
            return conta.numero, conta.saldo, conta.agencia
        except IndexError:
            raise StopIteration
        



        
        
