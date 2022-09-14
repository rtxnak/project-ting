from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    is_duplicate_file = False
    # Checking if path_file is a duplicate
    instance_length = instance.__len__()
    for i in range(instance_length):
        searched_dict = instance.search(i)
        if path_file == searched_dict['nome_do_arquivo']:
            is_duplicate_file = True

    # Creating dictionary and enqueue on instance
    if not is_duplicate_file:
        txt_importation = txt_importer(path_file)

        insert_dict = {
                'nome_do_arquivo': path_file,
                'qtd_linhas': len(txt_importation),
                'linhas_do_arquivo': txt_importation
        }

        instance.enqueue(insert_dict)
        print(f'{insert_dict}', file=sys.stdout)


def remove(instance):
    # Checking that there are no items in the queue
    instance_length = instance.__len__()
    if instance_length == 0:
        print(f'Não há elementos', file=sys.stdout)
    else:
        # Dequeuing first item from the queue
        item_dequeue = instance.dequeue()
        path_file = item_dequeue['nome_do_arquivo']
        print(f'Arquivo {path_file} removido com sucesso', file=sys.stdout)


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
