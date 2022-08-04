from requestsToDadata import dadataRequest


def changeSetting(dadata: dadataRequest):
    print('Введите номер данных, которые хотите исправить, если хотите исправить всё сразу,'
          ' то введите 4, чтобы закончить изменения введите "закончить"')
    answer_from_user = input()
    if answer_from_user == 'закончить':
        return 0
    while not answer_from_user.isdigit() or (1 > int(answer_from_user) > 4):
        print(f'Вы не правильно ввели данные, попробуйте ещё раз, чтобы закончить изменения введите "закончить",'
              f' "выход" для заверщения программы ')
        answer_from_user = input()
        if answer_from_user.lower() == 'выход':
            exit(0)
        if answer_from_user.lower() == 'закончить':
            break
    answer_from_user = int(answer_from_user)

    if answer_from_user == 1:
        print('Введите новый url:')
        answer_from_user = input()
        dadata.setUrl(answer_from_user)
    elif answer_from_user == 2:
        print('Введите новый токен:')
        answer_from_user = input()
        dadata.setToken(answer_from_user)
    elif answer_from_user == 3:
        print('Введите язые "ru" или "en": ')
        answer_from_user = input()
        dadata.setLanguage(answer_from_user)
    elif answer_from_user == 4:
        print('Введите новые настройки "url, токен, язык", через пробел:')
        answer_from_user = input()
        url, token, language = answer_from_user.split()
        dadata.setSettings(url, token, language)
    else:
        return 0


def main():
    dadata = dadataRequest()

    dict_for_geolacation = {
        '0': 'Это точные координаты дома',
        '1': 'Координаты ближайшего дома',
        '2': 'Координаты улицы',
        '3': 'Координаты населенного пункта',
        '4': 'Координаты города',
        '5': 'Координаты не определенны'
    }

    while not dadata.dataInDataBaseIsValid():
        print("Данные в настройках не валидны, либо ещё не заполненны\nТекущие данные")
        url, token, language = dadata.getSettings()
        print(f'1)URL = {url}\n2)Token = {token}\n3)language = {language}')
        changeSetting(dadata)

    print('Здравствуйте, введите адрес \nНаберите "помощь", для инструкций\n"Выход" для завершения программы')
    user_input = input().lower()
    while user_input != 'exit' and user_input != 'close' and user_input != 'выход':
        if user_input == 'помощь':
            print("{:<25} {:<10}".format('exit, close, выход ', 'Выход'))
            print("{:<25} {:<10}".format('помощь', 'список доступных команд'))
            print("{:<25} {:<10}".format('настройки', 'Текущие настройи программы'))
            print('введите адрес \nНаберите "помощь", для инструкций\n"Выход" для завершения программы')
            user_input = input().lower()
            continue
        if user_input == 'настройки':
            print('Текущие настройки, чтобы что-то изменить введите "изменить"')
            url, token, language = dadata.getSettings()
            print(f'1)URL = {url}\n2)Token = {token}\n3)language = {language}')
            print('Введите адрес или одну из команд')
            user_input = input().lower()
            continue

        if user_input == 'изменить':
            changeSetting(dadata)
            print('Введите адрес или одну из команд')
            user_input = input().lower()
            continue

        result = dadata.suggest(user_input)
        if result:
            number_of_fdress = 1
            for record in result:
                print(f'{number_of_fdress}) {record["value"]}')
                number_of_fdress += 1

            print('\nВыберите нужный номер адреса, если нужного нет, то попробуйте уточнить запрос')
            number_of_fdress = input()
            if number_of_fdress.isdigit() and 11 > int(number_of_fdress) > 0:
                number_of_fdress = int(number_of_fdress)
                string = result[number_of_fdress - 1]['value']
                result = dadata.suggest(string, count=1)[0]
                print(dict_for_geolacation[result['data']['qc_geo']])
                print(f'Широта - {result["data"]["geo_lat"]}, Долгота - {result["data"]["geo_lon"]}'
                      f'\nПолный адрес {result["unrestricted_value"]}')
                print('Введите новый адрес или "выход", для завершения программы')
                user_input = input().lower()
            else:
                user_input = str(number_of_fdress).lower()
        else:
            print('По вашему запросу ничего не нашлось, попробуйте уточнить адрес или ввести его по другому')
            user_input = input().lower()



if __name__ == '__main__':
    main()
