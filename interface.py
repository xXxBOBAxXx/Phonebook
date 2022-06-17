import from_phonebook as data

def main_menu():
    print('Выберите команду:\n1-вывести телефонную книгу в терминал\n\
                            2-найти контакт\n\
                            3-создать новый контакт\n\
                            любая другая - выход из программы')
    try:
        result_request = int(input())
    except:
        return exit()
    return result_request

def action_contact():
    print('1 - изменить контакт\n\
            2 - удалить контакт\n\
            3 - поделиться контактом\n\
            0 - выйти в главное меню\n\
            любая другая - выход из программы')
    print('Выберите дальнейшее действие с контактом: ')
    try:
        result_request = int(input())
    except:
        return exit()
    return result_request if 0 <= result_request <= 3 else exit()
