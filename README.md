# auto-tips-for-cities
## Геокодирование адреса
### Программа,позволяющая узнать координаты места, по адресу дома

## Установка
На вашем компьютере должны быть установлены:
 * python, версии 3 и выше. [Сайт для скачивания](https://www.python.org/downloads/), если у вас linux скачайте из своего дистрибутива
    * Нажмите на желтую кнопку download, начнется скачивание установщика python
    * Запустите, поставьте галку в секции "Add Python to Path"
 * pip, начиная с Python версии 3.4, pip поставляется вместе с интерпретатором python, если ваша версия ниже, то установите pip отдельно
 

### Windows
* Скачайте архив, нажав на ` Code ` -> `Download ZIP`
* Распакуйте его в удобную для вас папку, откройте консоль `Cmd` в этой папке
* В консоли введите `pip -m venv venv`
* Далее, активируем окружение `venv/Scripts/activate.bat`, если слева появилась надпись `(venv)`, то всё хорошо
* После этого пишем `pip install -r requirements.txt`

### Linux
* Скачайте архив, нажав на ` Code ` -> `Download ZIP`
* Распакуйте его в удобную для вас папку, откройте консоль в этой папке
* В консоли введите `pip -m venv venv`
* Далее, активируем окружение `source venv/bin/activate`, если слева появилась надпись `(venv)`, то всё хорошо
* После этого пишем `pip install -r requirements.txt`

#### Запуск
Для использования программы обязательно зарегистрируйтесь на сайте [https://dadata.ru/](https://dadata.ru/), в личном кабинете будет APi-ключ, сохраните его.
В консоли, с активированным окружением, вводим `python main.py`
При первом запуске программа уведомит вас, что она не настроена, вам нужно добавить Token, вставив свой Api-ключ для дальнейшей работы программы
