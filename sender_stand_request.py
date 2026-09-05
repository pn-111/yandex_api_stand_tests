# Импортируем модуль configuration, который, мы создали выше - он содержит настройки подключения и путь к документации
import configuration
# Импортируем модуль requests, который предназначен для отправки HTTP-запросов
import requests
# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data


def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH,params={"count":20})

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)


# Создание нового пользователя
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

# Получение списка наборов по продуктам
def post_products_kits(products_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH, 
                         json=products_ids)
