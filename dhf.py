from datetime import datetime


data_atual = 23 # Este é o valor que simula a data do dia atual para manipular as funções de transação




class Transacao:
    def __init__(self, tipo_transacao):
        self.tipo_transacao = tipo_transacao
        self.data_atual = datetime.now().strftime("DATA: %d/%m/%Y - HORÁRIO: %H:%M")

    def __str__(self):
        return f"\nTipo de transação: {self.tipo_transacao} / Data da Transação: {self.data_atual}"


class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.transacoes = []
        self.ultimo_registro = ''
        self.limite_transacoes = 0

    def realizar_transacao(self, tipo):
        if self.ultimo_registro == '' or data_atual != self.ultimo_registro:
            self.ultimo_registro = data_atual
            self.limite_transacoes = 0
        
        if self.ultimo_registro == data_atual and self.limite_transacoes < 10:
            self.transacoes.append(Transacao(tipo))
            self.limite_transacoes += 1
            self.ultimo_registro = data_atual
            print('Transação concluída com sucesso.')
            print(self.limite_transacoes, self.ultimo_registro)

        else:
            print('Limite de transações alcançado! Tente novamente no outro dia!')

    def exibir_extrato_transações(self):
        print('\n\n=-=-=-=-=-=-=-=-=-=-= Extrato das Transações =-=-=-=-=-=-=-=-==-=\n\n')
        print(f"Cliente: {self.nome}\nIdade do cliente: {self.idade}\n")
        print('[                 TRANSAÇÕES                     ]')
        for transacao in self.transacoes:
            print(transacao)
        print('\n\n=-=-=-=-=-=-=-=-=-=-= Fim dos Extratos =-=-=-=-=-=-=-=-=-=-=-==-=\n\n')


def menu(opcoes: list):
    print('=-=-=-=-=- MENU DE OPÇÕES =-=-=-=-==-=')
    for i, opc in enumerate(opcoes):
        print(f"[{i}] - [{opc}]")
    print('\nOu digite "sair" para finalizar!')
    print('=-=-=-=-=-=-=-=-=-=-==-=-==-=-=-=-=-==')
    escolha_status = False
    usuario = input('\nDigite a opção desejada: ').strip()
    if usuario =='sair':
        return 'Finalizar'
    else:
        try:
            escolha = opcoes[int(usuario)]
        except Exception:
            return escolha_status
        else:
            return escolha






clientes = [Cliente('Felipe', 35), Cliente('Luigi', 4)]


while True:
    usuario_menu = menu(['Realizar Transação', 'Exibir Extratos', 'Alterar Data'])

    match usuario_menu:
        case 'Finalizar':
            break
        case False:
            print('\nOpção não encontrada!! Tente novamente!\n')
            continue

        case 'Alterar Data':
            nova_data = input('Digite a nova data: ')
            data_atual = nova_data
            print(f'Data atual alterada para: {data_atual}')
        
        case 'Realizar Transação':
            operacao_realizada = ''

            index = ''

            transacao = input('Digite a transação: ').strip()

            if transacao =='sair':
                break
            else:
                cliente_operando = input('Digite o nome do cliente: ')
                for cliente in clientes:
                    try:
                        if cliente.nome == cliente_operando:
                            operacao_realizada = True
                            index = clientes.index(cliente)
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        operacao_realizada = False

                print(operacao_realizada)

                match operacao_realizada:
                    case True:
                        clientes[index].realizar_transacao(transacao)
                    case False:
                        print('A operação falhou! CLiente não Encontrado!')

        case 'Exibir Extratos':
            cliente_operando = input('Informe o nome do Cliente: ').strip()
            for cliente in clientes:
                if cliente.nome == cliente_operando:
                    cliente.exibir_extrato_transações()

