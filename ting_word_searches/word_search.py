def exists_word(word, instance):
    result = []
    for index in range(len(instance)):
        occurrence = []
        file = instance.search(index)
        for index, line in enumerate(file['linhas_do_arquivo']):
            if word.casefold() in line.casefold():
                occurrence.append({'linha': index + 1})
        if len(occurrence) > 0:
            result.append({
                'palavra': word,
                'arquivo': file['nome_do_arquivo'],
                'ocorrencias': occurrence
            })
    return result

    # https://stackoverflow.com/questions/319426/how-do-i-do-a-case-insensitive-string-comparison


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
