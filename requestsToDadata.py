import sqlite3
import requests


class dadataRequest():
    def __init__(self):

        self.__connection = None
        self.__settingsExist = False

        self.__url = ''
        self.__token = ''
        self.__language = ''

        try:
            self.__connection = sqlite3.connect('settings.db')
        except sqlite3.Error as e:
            print("Error while opening/creating dataBase: ", e.args[0])
            exit(1)
        cursor = self.__connection.cursor()
        try:
            cursor.execute(f"""CREATE TABLE settings 
                            (url TEXT DEFAULT 'https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/address',
                            token TEXT, language TEXT DEFAULT ru)""")
            cursor.execute(f"""INSERT INTO settings (token)
                            VALUES (0)""")
            self.__connection.commit()
        except:
            self.__settingsExist = True

        cursor.execute("""SELECT url, token, language FROM settings""")
        url, token, language = cursor.fetchone()
        self.__url = url
        self.__token = token
        self.__language = language
        self.__headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": "Token " + token
        }

    def __del__(self):
        self.__connection.close()

    def dataInDataBaseIsValid(self) -> bool:
        try:
            self.suggest(query="москва, ленина")
        except:
            return False

        return True

    def suggest(self, query: str, count: int = 10):
        response = requests.post(self.__url, headers=self.__headers,
                                 json={"query": query, "count": count, "language": self.__language})
        response.raise_for_status()
        return response.json()["suggestions"]

    def getSettings(self) -> list:
        return [self.__url, self.__token, self.__language]

    def getToken(self) -> str:
        return self.__token

    def getLanguage(self) -> str:
        return self.__language

    def getUrl(self) -> str:
        return self.__url

    def setUrl(self, url: str):
        self.__url = url
        self.commitChanges()

    def setToken(self, token: str):
        self.__token = token
        self.__headers['Authorization'] = 'Token ' + self.__token
        self.commitChanges()


    def setLanguage(self, language: str):
        self.__language = language
        self.commitChanges()

    def setSettings(self, url: str, token: str, secret: str, language: str):
        self.__url = url
        self.__token = token
        self.__secret = secret
        self.__language = language
        self.commitChanges()

    def commitChanges(self):
        cursor = self.__connection.cursor()
        cursor.execute(
            f"""UPDATE settings SET url = '{self.__url}', token = '{self.__token}', language = '{self.__language}'""")
        self.__connection.commit()
