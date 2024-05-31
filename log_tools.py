from datetime import datetime
import inspect
from pathlib import Path


ROOT_DIR = Path(__file__).parent

def log_file():
    try:
        with open(file=ROOT_DIR/'log.txt', mode='r'):
            pass
    except FileNotFoundError:
        with open(ROOT_DIR/'log.txt', mode='w') as lg_file:
            lg_file.write('=-=-=-=-=-=-=-=--=-= LOG DE REGISTROS =-=-=-=-=-=-=-=-=-====')
            print('\nArquivo de Log criado com sucesso!\n')
    else:
        print('\nArquivo de log carregado com sucesso!\n')
        



def args_data_inspection(fnc):
    arg_inspection = inspect.getfullargspec(fnc)
    args_data = {
        'Argumentos Posicionais':arg_inspection.args,
        'Argumentos Padrão':arg_inspection.defaults,
        'Argumentos apenas por palavra-chave':arg_inspection.kwonlyargs,
        'Argumentos de variável de posição (*args)':arg_inspection.varargs,
        "Argumentos de variável de palavra-chave (**kwargs):": arg_inspection.varkw,
    }
    return args_data


def log_register(fnc):
    def wrapper(*args):
        dt_atual = datetime.now().strftime('DATA: %d/%m/%Y - HORA: %H:%M')
        function_name = fnc.__name__
        function_args_data = args_data_inspection(fnc)
        function_return = 'String'
        function_customer = fnc(*args)
        with open(file=ROOT_DIR/'log.txt', mode='a', encoding='UTF-8') as file:
            file.writelines([f'\n{dt_atual}\n', f'Cliente: {function_customer}\n' f'Nome da função: {function_name}\n', f'Retorno da Função: {function_return}\n'])
            file.writelines([ f'{key} - {value}\n' for (key,value) in function_args_data.items()])
        

    return wrapper

