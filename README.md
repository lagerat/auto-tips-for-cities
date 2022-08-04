# auto-tips-for-cities
## Геокодирование адреса
### Программа,позволяющая узнать координаты места, по адресу дома

## Установка
На вашем компьютере должны быть установлены:
 * python, версии 3 и выше. [Сайт для скачивания](https://www.python.org/downloads/)
    * Нажмите на желтую кнопку download, начнется скачивание установщика python
    * Запустите, поставьте галку в секции "Add Python to Path"
 * pip, начиная с Python версии 3.4, pip поставляется вместе с интерпретатором python, если ваша версия ниже, то установите pip отдельно
 

### Windows
* Скачайте архив, нажав на ` Code ` -> `Download ZIP`
* Распакуйте его в удобную для вас папку, откройте консоль `Cmd` в этой папке
* В консоле введите `pip -m venv venv`
* Далее вводим `venv/Scripts/activate.bat`, если слева появилась надпись `(venv)`, то всё хорошо
* После это пишем `pip install -r requirements.txt`

### Linux
* Скачайте архив, нажав на ` Code ` -> `Download ZIP`
* Распакуйте его в удобную для вас папку, откройте консоль в этой папке
* В консоле введите `pip -m venv venv`
* Далее вводим `source venv/bin/activate`, если слева появилась надпись `(venv)`, то всё хорошо
* После это пишем `pip install -r requirements.txt`

#### Запуск
`python main.py`
